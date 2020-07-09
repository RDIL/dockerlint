def has_no_install_rec(line):
    """
    Checks if the line doesn't have
    --no-install-recommends when it should be present.
    """

    return (
        "apt" in line
        and "install" in line
        and not ("--no-install-recommends" in line or "-q" in line)
    )


def using_apt_get_on_parrotsec(line):
    """
    Checks if your image uses parrotsec and uses apt-get.
    This is discouraged - you should use apt instead.
    """
    return "apt-get" in line


def using_dist_upgrade_on_parrotsec(line):
    """
    Checks if your image uses parrotsec and uses apt dist-upgrade.
    This is discouraged - you should use the parrot-upgrade command.
    """
    return "apt" in line and "dist-upgrade" in line
