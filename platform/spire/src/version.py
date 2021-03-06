import command
from resources import get_resource


def get_git_version():
    return get_resource("GIT_VERSION").decode().rstrip()


def get_apt_branch():
    return get_resource("APT_BRANCH").decode().rstrip()


def get_apt_url():
    return get_resource("APT_URL").decode().rstrip()


@command.wrap
def display_version():
    "display version info"
    git_version = get_git_version()
    print("Git commit hash:", git_version)

    apt_branch = get_apt_branch()
    print("Apt branch:", apt_branch)

    apt_url = get_apt_url()
    print("Apt URL:", apt_url)


main_command = display_version
