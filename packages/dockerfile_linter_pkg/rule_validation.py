from dockerfile_parser_pkg import Node


def has_no_install_rec(node: Node) -> bool:
    """
    Checks if the line doesn't have
    --no-install-recommends when it should be present.
    """
    ct = node.content

    return (
        node.variant == "RUN"
        and "apt" in ct
        and "install" in ct
        and not ("--no-install-recommends" in ct or "-q" in ct)
    )
