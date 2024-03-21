import asyncio
import shlex
from typing import Tuple

import git
from git.exc import GitCommandError, InvalidGitRepositoryError

import config

from ..logging import LOGGER

def install_requirements(cmd: str) -> Tuple[str, str, int, int]:
    """
    Install Python requirements from a given command.

    Returns a tuple containing stdout, stderr, return code, and process ID.
    """
    async def run_cmd():
        args = shlex.split(cmd)
        try:
            process = await asyncio.create_subprocess_exec(
                *args,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
        except FileNotFoundError as e:
            return "", str(e), -1, -1

        stdout, stderr = await process.communicate()
        return (
            stdout.decode("utf-8", "replace").strip(),
            stderr.decode("utf-8", "replace").strip(),
            process.returncode,
            process.pid,
        )

    return asyncio.get_event_loop().run_until_complete(run_cmd())

def git():
    """
    Fetch updates from the upstream repository and install requirements.
    """
    REPO_LINK = config.UPSTREAM_REPO
    GIT_TOKEN = config.GIT_TOKEN

    if GIT_TOKEN:
        GIT_USERNAME = REPO_LINK.split("com/")[1].split("/")[0]
        TEMP_REPO = REPO_LINK.split("https://")[1]
        UPSTREAM_REPO = f"https://{GIT_USERNAME}:{GIT_TOKEN}@{TEMP_REPO}"
    else:
        UPSTREAM_REPO = REPO_LINK

    try:
        repo = git.Repo()
        LOGGER(__name__).info("Git Client Found [VPS DEPLOYER]")
    except GitCommandError:
        LOGGER(__name__).info("Invalid Git Command")
    except InvalidGitRepositoryError:
        repo = git.Repo.init()

        if "origin" in repo.remotes:
            origin = repo.remote("origin")
        else:
            origin = repo.create_remote("origin", UPSTREAM_REPO)

        origin.fetch()

        repo.create_head(
            config.UPSTREAM_BRANCH,
            origin.refs[config.UPSTREAM_BRANCH],
        )

        repo.heads[config.UPSTREAM_BRANCH].set_tracking_branch(
            origin.refs[config.UPSTREAM_BRANCH]
        )

        repo.heads[config.UPSTREAM_BRANCH].checkout(True)

        try:
            repo.create_remote("origin", config.UPSTREAM_REPO)
        except BaseException:
            pass

        nrs = repo.remote("origin")
        nrs.fetch(config.UPSTREAM_BRANCH)

        try:
            nrs.pull(config.UPSTREAM_BRANCH)
        except GitCommandError:
            repo.git.reset("--hard", "FETCH_HEAD")

        install_req("pip3 install --no-cache-dir -r requirements.txt")

        LOGGER(__name__).info("Fetching updates from upstream repository...")
