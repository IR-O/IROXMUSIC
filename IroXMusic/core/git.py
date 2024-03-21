import asyncio
import shlex
from typing import Tuple

import git
from git.exc import GitCommandError, InvalidGitRepositoryError
import config

async def clone_repository(repo_url: str, local_path: str) -> Tuple[bool, str]:
    try:
        git.Repo.clone_from(repo_url, local_path)
        return True, "Repository cloned successfully."
    except (GitCommandError, InvalidGitRepositoryError) as e:
        return False, f"Error cloning repository: {str(e)}"

async def main():
    repo_url = config.REPO_URL
    local_path = config.LOCAL_PATH

    success, message = await clone_repository(repo_url, local_path)
    if success:
        print(message)
    else:
        print(message)
        await asyncio.sleep(5)  # wait for 5 seconds before exiting

if __name__ == "__main__":
    asyncio.run(main())
