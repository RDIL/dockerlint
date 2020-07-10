from . import rule_validation as checks, parser
from textwrap import dedent

TAB_CHARACTER = "⠀"


class Issue:
    """An issue with the Dockerfile."""

    description = "A description of the rule"

    def __init__(self, line_number):
        self.line_number = line_number

    @staticmethod
    def create_from(description, line_number=None):
        """Create an issue instance."""

        g = Issue(line_number)
        g.description = description
        return g

    def __str__(self):
        """Convert this issue to a human-readable string."""

        if self.line_number is None:
            return self.description

        return " ".join(
            ["line", str(self.line_number), "-", self.description]
        )


def read_dockerfile(file_io_obj):
    """Reads from the IO stream."""

    lines = dedent(file_io_obj.read().replace(TAB_CHARACTER, " ")).split("\n")
    file_io_obj.close()
    return lines


def lint(dockerfile_path):
    """Lints the passed Dockerfile."""

    lines = read_dockerfile(dockerfile_path)
    issues = []

    # has continuation marker (backslash)
    cont_marker = False
    # number of FROM nodes
    base_image_count = 0
    # number of LABELs in general
    label_count = 0
    has_reported_base_image_problem = False
    has_reported_label_problem = False
    parrotsec = "parrotsec" in "\n".join(lines).lower()

    for index, content in enumerate(lines):
        report_index = index + 1
        c = content
        cont_marker = c.endswith("\\") or c.endswith("\\ ")

        if c == "" or c.startswith("#"):
            cont_marker = False

        if checks.has_no_install_rec(c):
            issues.append(
                Issue.create_from(
                    "uses apt install without no-install-recommends",
                    report_index,
                )
            )

        if parser.is_base_image_definition(c):
            base_image_count = base_image_count + 1

            if base_image_count >= 3 and not has_reported_base_image_problem:
                issues.append(
                    Issue.create_from(
                        "has 3 or more FROM declarations", None,
                    )
                )
                has_reported_base_image_problem = True

        if parser.is_label_definition(c, cont_marker):
            label_count = label_count + 1

            if label_count >= 20 and not has_reported_label_problem:
                issues.append(
                    Issue.create_from("has 20 or more LABELs", None)
                )
                has_reported_label_problem = True

        if parrotsec:
            if checks.using_apt_get_on_parrotsec(c):
                issues.append(
                    Issue.create_from(
                        "uses apt-get instead of apt on parrotsec",
                        report_index,
                    )
                )

            if checks.using_dist_upgrade_on_parrotsec(c):
                issues.append(
                    Issue.create_from(
                        "uses apt dist-upgrade instead of parrot-upgrade",
                        report_index,
                    )
                )

    if len(lines) >= 750:
        issues.append(
            Issue.create_from("has 750 or more lines - wowza!", None)
        )

    return issues
