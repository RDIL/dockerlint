def has_no_install_rec(line):
    return (
        "apt" in line and
        "install" in line and
        not (
            "--no-install-recommends" in line or
            "-q" in line
        )
    )
