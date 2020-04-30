from dockerfile_parser_pkg import Node


def has_no_install_rec(line: str) -> bool:
    """
    Checks if the line doesn't have
    --no-install-recommends when it should be present.
    """

    return (
        "apt" in line
        and "install" in line
        and not ("--no-install-recommends" in line or "-q" in line)
    )
