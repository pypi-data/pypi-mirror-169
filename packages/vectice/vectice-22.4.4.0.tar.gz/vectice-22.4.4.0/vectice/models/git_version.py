from __future__ import annotations

import imp
import logging
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Tuple

from vectice.utils.ipykernal_hook import notebook_path, get_absolute_path, notebook_name

LOGGER = logging.getLogger("GitVersion")


def _is_git_repo(path: str = ".", search_parent_directories: bool = True) -> bool:
    from git import Repo, InvalidGitRepositoryError

    try:
        Repo(path, search_parent_directories=search_parent_directories)
        return True
    except InvalidGitRepositoryError:
        return False


def _main_is_frozen() -> bool:
    return (
        hasattr(sys, "frozen") or hasattr(sys, "importers") or imp.is_frozen("__main__")  # new py2exe  # old py2exe
    )  # tools/freeze


def _get_executable_path() -> str:
    if _main_is_frozen():
        return sys.executable
    main_module = sys.modules["__main__"]
    if not hasattr(main_module, "__file__") or main_module.__file__ is None:
        return sys.argv[0]
    else:
        result = main_module.__file__
        if result is None:
            result = ""
        return result


def _relative_path(parent_path, child_path) -> str:
    parent_path = Path(os.path.abspath(parent_path))
    child_path = Path(os.path.abspath(child_path))
    try:
        return str(child_path.relative_to(parent_path)).replace("\\", "/")
    except ValueError:
        return str(child_path)


def _extract_git_version(
    path: str = ".", search_parent_directories: bool = True, check_remote_repository: bool = True
) -> Optional[GitVersion]:
    try:
        from git import Repo, InvalidGitRepositoryError, NoSuchPathError
    except ModuleNotFoundError:
        return None

    repo = None
    if _check_if_collab():
        try:
            path = get_absolute_path()
            repo = Repo(path=path, search_parent_directories=search_parent_directories)
        except Exception as e:
            logging.warning(f"Extract git version failed due to {e}")
            return None

    try:
        if repo is None:
            repo = Repo(path, search_parent_directories=search_parent_directories)
        repository_name = repo.remotes.origin.url.split(".git")[0].split("/")[-1]
        try:
            branch_name = repo.active_branch.name
        except TypeError as e:
            logging.warning(f"Extract git version failed due to {e}")
            return None
        commit_hash = repo.head.object.hexsha
        commit_comment = repo.head.object.message
        commit_author_name = repo.head.object.author.name
        commit_author_email = repo.head.object.author.email
        if "ipykernel_launcher.py" in _get_executable_path() and not _check_if_collab():
            entrypoint = _relative_path(os.path.dirname(repo.git_dir), notebook_path())
        # TODO clean up
        elif _check_if_collab():
            entrypoint = get_absolute_path()
            entrypoint = entrypoint.split(str(repo.common_dir).split("/")[-2])[-1]
            entrypoint = entrypoint[1:]
        else:
            entrypoint = _relative_path(os.path.dirname(repo.git_dir), _get_executable_path())
        try:
            if check_remote_repository:
                repo.active_branch.commit.tree.join(entrypoint)
        except KeyError as e:
            logging.warning(f"Extract git version failed due to {e}")
            return None
        is_dirty = repo.is_dirty()
        uri = repo.remotes.origin.url
        return GitVersion(
            repository_name,
            branch_name,
            commit_hash,
            commit_comment,
            commit_author_name,
            commit_author_email,
            is_dirty,
            uri,
            entrypoint,
        )
    except InvalidGitRepositoryError as e:
        logging.warning(f"Extract git version failed due to {e}")
        return None
    except NoSuchPathError:
        raise ValueError("Extract git version as the path is not correct. Please check the path.")


def _extract_github_information_from_uri(uri: str) -> Optional[Tuple[str, str, Optional[str], Optional[str]]]:
    if "tree" in uri or "blob" in uri:
        match = re.search("(?:https://github.com/|git@github.com:)([a-zA-Z0-9-]+)/(.+)(?:/tree/|/blob/)(.+)?", uri)
    elif "commit" in uri:
        match = re.search("(?:https://github.com/|git@github.com:)([a-zA-Z0-9-]+)/(.+)/commit/(.+)?", uri)
        if match:
            return match.group(1), match.group(2), None, match.group(3) if len(match.groups()) > 2 else None
        else:
            return None
    else:
        match = re.search("(?:https://github.com/|git@github.com:)([a-zA-Z0-9-]+)/(.+)?", uri)
    if match:
        return match.group(1), match.group(2), match.group(3) if len(match.groups()) > 2 else None, None
    else:
        return None


def _extract_bitbucket_cloud_information_from_uri(
    uri: str, domain: Optional[str] = None
) -> Optional[Tuple[Optional[str], str, str, Optional[str], Optional[str]]]:
    """
    Naming conventions https://somecompany.com/ or https://somecompany.com/bitbucket/
    """
    if uri.startswith("https://bitbucket.org") or uri.startswith("git@bitbucket.org"):
        if "src" in uri or "branch" in uri:

            match = re.search(
                "(?:https://bitbucket.org/|git@bitbucket.org:)([a-zA-Z0-9-]+)/(.+)(?:/src/|/branch/)(.+)?",
                uri,
            )

        elif "commits" in uri:
            match = re.search(
                "(?:https://bitbucket.org/|git@bitbucket.org:)([a-zA-Z0-9-]+)/(.+)/commits/(.+)?",
                uri,
            )
            if match:
                return None, match.group(1), match.group(2), None, match.group(3)
            else:
                return None
        else:
            match = re.search("(?:https://bitbucket.org/|git@bitbucket.org:)([a-zA-Z0-9-]+)/(.+)?", uri)

        if match:
            return None, match.group(1), match.group(2), match.group(3) if len(match.groups()) > 2 else None, None
        else:
            return None
    elif domain is not None:
        if "src" in uri or "branch" in uri:
            match = re.search(f"{domain}/projects/([a-zA-Z0-9-]+)/repos/(.+)(?:/src/|/branch/)(.+)?", uri)
        elif "commits" in uri:
            match = re.search(f"{domain}/projects/([a-zA-Z0-9-]+)/repos/(.+)/commits/(.+)?", uri)
            if match:
                return domain, match.group(1), match.group(2), None, match.group(3)
            else:
                return None
        else:
            match = re.search(f"{domain}/projects/([a-zA-Z0-9-]+)/repos/(.+)?", uri)
        if match:
            return domain, match.group(1), match.group(2), match.group(3) if len(match.groups()) > 2 else None, None
        else:
            return None
    else:
        return None


def _extract_gitlab_information_from_uri(
    uri: str, domain: Optional[str] = None
) -> Optional[Tuple[Optional[str], str, str, Optional[str], Optional[str]]]:
    if uri.startswith("https://gitlab.com") or uri.startswith("git@gitlab.com"):
        if "tree" in uri or "blob" in uri:
            match = re.search(
                "(?:https://gitlab.com/|git@gitlab.com:)([a-zA-Z0-9-]+)/(.+)(?:/-/blob/|/tree/)(.+)?", uri
            )
        elif "commit" in uri:
            match = re.search("(?:https://gitlab.com/|git@gitlab.com:)([a-zA-Z0-9-]+)/(.+)/-/commit/(.+)?", uri)
            if match:
                return None, match.group(1), match.group(2), None, match.group(3) if len(match.groups()) > 2 else None
            else:
                return None
        else:
            match = re.search("(?:https://gitlab.com/|git@gitlab.com:)([a-zA-Z0-9-]+)/(.+)?", uri)
        if match:
            return None, match.group(1), match.group(2), match.group(3) if len(match.groups()) > 2 else None, None
        else:
            return None
    elif domain is not None:
        if "tree" in uri or "blob" in uri:
            match = re.search(f"{domain}/([a-zA-Z0-9-]+)/([a-zA-Z0-9-]+)(?:/-/blob/|/tree/)(.+)?", uri)
        else:
            match = re.search(f"{domain}/([a-zA-Z0-9-]+)/(.+)?", uri)
        if match:
            return domain, match.group(1), match.group(2), match.group(3) if len(match.groups()) > 2 else None, None
        else:
            return None
    else:
        return None


def _create_git_version_from_uri(
    uri: str, script_relative_path: Optional[str] = None, login_or_token=None, password=None, jwt=None
) -> Optional[GitVersion]:
    from github import Github

    g = Github(login_or_token=login_or_token, password=password, jwt=jwt)
    result = _extract_github_information_from_uri(uri)
    if result is None:
        return None
    organisation, repository_name, branch, commit = result
    github_repository = g.get_repo(f"{organisation}/{repository_name}")
    if commit:
        github_commit = github_repository.get_commit(commit)
        branch_name = branch
        github_branch = None
    else:
        if branch is None:
            branch_name = github_repository.default_branch
        else:
            branch_name = branch
        github_branch = github_repository.get_branch(branch_name)
        github_commit = github_branch.commit
    if github_branch is None and github_commit is None:
        raise RuntimeError(f"invalid branch name {branch_name}")
    if script_relative_path and not _is_file_in_git(github_repository, script_relative_path, branch_name):
        return None
    return GitVersion(
        repository_name,
        branch_name,
        github_commit.sha,
        github_commit.commit.message,
        github_commit.commit.author.name,
        github_commit.commit.author.email,
        False,
        f"https://www.github.com/{organisation}/{repository_name}",
        script_relative_path,
    )


def _create_bitbucket_version_from_uri(
    uri: str,
    script_relative_path: Optional[str] = None,
    username: Optional[str] = None,
    password: Optional[str] = None,
    oauth2_token: Optional[dict] = None,
    domain: Optional[str] = None,
) -> Optional[GitVersion]:
    from atlassian.bitbucket.cloud import Cloud  # type: ignore
    from atlassian import Bitbucket  # type: ignore

    logging.getLogger("atlassian").setLevel(logging.FATAL)  # Mutes the file check logging
    result = _extract_bitbucket_cloud_information_from_uri(uri, domain)
    if result is None:
        return None
    url, workspace_name, repository_name, branch_name, commit = result
    if url:
        try:
            bitbucket = Bitbucket(url=url, username=username, password=password, oauth2=oauth2_token, verify_ssl=True)
            bit_repository = [
                repo for repo in list(bitbucket.repo_list(workspace_name)) if repo.get("name") == repository_name
            ]
            if len(bit_repository) == 1:
                bit_repository = bit_repository[0]
            else:
                raise ValueError("Please check the repository provided.")
            if commit:
                commits = [comm for comm in bitbucket.get_commits(workspace_name, bit_repository["slug"]) if comm.get("id") == commit]  # type: ignore[call-overload]
                if len(commits) == 1:
                    bit_commit = commits[0]
                else:
                    raise ValueError("Please check the commit provided.")
            elif branch_name and commit is None:
                branch = [
                    branch
                    for branch in bitbucket.get_branches(bit_repository["project"]["key"], bit_repository["slug"])  # type: ignore[call-overload]
                    if branch["displayId"] == branch_name
                ]
                if len(branch) == 1:
                    branch = branch[0]
                    branch_name = branch["displayId"]  # type: ignore[call-overload]
                else:
                    raise ValueError("Please check the branch provided.")
                bit_commit = branch["metadata"]["com.atlassian.bitbucket.server.bitbucket-branch:latest-commit-metadata"]  # type: ignore[call-overload]
            else:
                branch = list(bitbucket.get_branches(workspace_name, bit_repository["slug"], limit=1))[0]  # type: ignore[call-overload]
                branch_name = branch["displayId"]  # type: ignore[call-overload]
                bit_commit = branch["metadata"]["com.atlassian.bitbucket.server.bitbucket-branch:latest-commit-metadata"]  # type: ignore[call-overload]
            if branch_name and script_relative_path:
                relative_path = f"{script_relative_path}?at={branch_name}"
            else:
                relative_path = None
        except Exception as e:
            raise RuntimeError(f"{e}")
        return GitVersion(
            repository_name,
            branch_name,
            bit_commit["id"],
            bit_commit["committer"]["name"],
            bit_commit["message"],
            bit_commit["author"]["emailAddress"],
            False,
            f"{url}/projects/{workspace_name}/repos/{repository_name}",
            relative_path if relative_path else "",
        )
    else:
        try:
            cloud = Cloud(oauth2=oauth2_token, cloud=True)
            workspace = cloud.workspaces.get(workspace_name)

            bit_repository = workspace.repositories.get(repository_name)
            if commit:
                commits = [comm for comm in bit_repository.get("commits").get("values") if comm.get("hash") == commit]  # type: ignore[attr-defined]
                if len(commits) == 1:
                    commit = commits[0]
                else:
                    raise ValueError("Please check the commit provided.")
            elif branch_name and commit is None:
                bit_branch = bit_repository.get(f"refs/branches/{branch_name}")  # type: ignore[attr-defined]
                branch_name = bit_branch["name"]
                commit = bit_branch["target"]
            else:
                main_branch = bit_repository.data["mainbranch"]  # type: ignore[attr-defined]
                branch_name = main_branch["name"]
                bit_branch = bit_repository.get(f"refs/branches/{branch_name}")  # type: ignore[attr-defined]
                commit = bit_branch["target"]
            if script_relative_path and commit:
                bit_repository.get(f"src/{commit['hash']}/{script_relative_path}")  # type: ignore[attr-defined, index]

            if branch_name and script_relative_path:
                relative_path = f"/{script_relative_path}?at={branch_name}"
            else:
                relative_path = None
        except Exception as e:
            raise RuntimeError(f"{e}")
        return GitVersion(
            repository_name,
            branch_name,
            commit["hash"],  # type: ignore[index]
            commit["message"],  # type: ignore[index]
            commit["author"]["user"]["display_name"],  # type: ignore[index]
            commit["author"]["raw"],  # type: ignore[index]
            False,
            f"https://bitbucket.org/{workspace_name}/{repository_name}",
            relative_path if relative_path else "",
        )


def _create_gitlab_version_from_uri(
    uri: str,
    script_relative_path: Optional[str] = None,
    private_token: Optional[str] = None,
    oauth_token: Optional[str] = None,
    domain: Optional[str] = None,
) -> Optional[GitVersion]:
    from gitlab import Gitlab

    result = _extract_gitlab_information_from_uri(uri, domain)
    if result is None:
        return None
    url, organisation, repository_name, branch_name, commit = result
    if url is None:
        url = "https://gitlab.com/"
    job_token = os.environ.get("CI_JOB_TOKEN") if os.environ.get("CI_JOB_TOKEN") else None
    try:
        git_lab = Gitlab(url, private_token=private_token, oauth_token=oauth_token, job_token=job_token)
        gitlab_project = git_lab.projects.get(f"{organisation}/{repository_name}")
        if commit:
            gitlab_commit_base = gitlab_project.commits.get(commit)
            gitlab_branch = gitlab_commit_base.refs("branch")
            if len(gitlab_branch) > 0:
                branch_name = gitlab_branch[0]["name"]  # type: ignore
            else:
                raise ValueError("Branch not found.")
            gitlab_commit = gitlab_commit_base.attributes
        else:
            gitlab_commit = None
        if branch_name is None:
            branch = str(gitlab_project.attributes.get("default_branch"))
        else:
            branch = branch_name
        gitlab_branch_base = gitlab_project.branches.get(branch)
        if gitlab_branch_base is None:
            raise RuntimeError(f"Invalid branch name {branch}")
        if gitlab_commit is None:
            gitlab_commit = gitlab_branch_base.attributes.get("commit")
        if gitlab_commit is None:
            raise RuntimeError("No commit was found.")
    except Exception as e:
        raise RuntimeError(f"{e}")
    return GitVersion(
        repository_name,
        branch,
        gitlab_commit["id"],
        gitlab_commit["message"],
        gitlab_commit["author_name"],
        gitlab_commit["author_email"],
        False,
        f"https://www.gitlab.com/{organisation}/{repository_name}",
        script_relative_path,
    )


def _is_file_in_git(
    github_repository=None, script_relative_path: Optional[str] = None, reference: Optional[str] = None
) -> bool:
    if not script_relative_path:
        return False
    elif script_relative_path and github_repository:
        try:
            script_relative_path = script_relative_path.replace("%20", " ")
            github_repository.get_contents(script_relative_path, reference)
        except Exception as e:
            if e.args[0] == 403 and e.args[1].get("errors")[0].get("code") == "too_large":
                return True
            return False
        return True
    else:
        return False


def _check_if_collab():
    try:
        if "fileId" in notebook_name():
            return True
    except Exception:
        return False


@dataclass
class GitVersion:
    repositoryName: str
    branchName: Optional[str]
    commitHash: str
    commitComment: str
    commitAuthorName: str
    commitAuthorEmail: str
    isDirty: bool
    uri: str
    entrypoint: Optional[str] = None

    @classmethod
    def create(
        cls, path: str = ".", search_parent_directories: bool = True, check_remote_repository: bool = True
    ) -> Optional[GitVersion]:
        code_artifact = _extract_git_version(path, search_parent_directories, check_remote_repository)
        return code_artifact

    @classmethod
    def create_from_github_uri(
        cls, uri: str, script_relative_path: Optional[str] = None, login_or_token=None, password=None, jwt=None
    ) -> Optional[GitVersion]:
        return _create_git_version_from_uri(uri, script_relative_path, login_or_token, password, jwt)

    @classmethod
    def create_from_bitbucket_uri(
        cls,
        uri: str,
        script_relative_path: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        oauth2_token: Optional[dict] = None,
        domain: Optional[str] = None,
    ) -> Optional[GitVersion]:
        return _create_bitbucket_version_from_uri(uri, script_relative_path, username, password, oauth2_token, domain)

    @classmethod
    def create_from_gitlab_uri(
        cls,
        uri: str,
        script_relative_path: Optional[str] = None,
        private_token: Optional[str] = None,
        oauth_token: Optional[str] = None,
        domain: Optional[str] = None,
    ) -> Optional[GitVersion]:
        return _create_gitlab_version_from_uri(uri, script_relative_path, private_token, oauth_token, domain)
