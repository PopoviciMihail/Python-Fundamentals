"""
Check if new release is available in GitHub and compare it with the installed version

repository = "openai/openai-python"
installed_version = "1.1.0"
print(check_new_release(repository, installed_version))
"""

from datetime import datetime

import requests
from requests import HTTPError


class ReleaseNotAvailableError(Exception):
    def __init__(self, message: str = "Release not available") -> None:
        self.message = message
        super().__init__(self.message)


def check_new_release(repository: str, installed_version: str) -> bool:
    """
    Check new release
    :param repository: Repository name
    :param installed_version: Installed version
    :return: True if a new release is available (False otherwise)
    """
    new_release_flag = False
    response = requests.get(f"https://api.github.com/repos/{repository}/releases")

    try:
        response.raise_for_status()
        data = response.json()

        releases = [r for r in data if not r["draft"] and not r["prerelease"]]
        if not releases:
            raise ReleaseNotAvailableError

        latest = releases[0]
        release_name = latest["name"]

        if new_release_flag := (release_name != installed_version):
            print(
                f"New release {release_name} published at {datetime.fromisoformat(latest['published_at'][0:-1])} is available."
            )

    except (HTTPError, ReleaseNotAvailableError) as ex:
        print(ex)

    return new_release_flag


if __name__ == "__main__":
    repository = "openai/openai-python"
    installed_version = "v1.12.2"
    print(check_new_release(repository, installed_version))
