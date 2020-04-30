from . import rule_validation as checks
import dockerfile_parser_pkg as parser
from textwrap import dedent

TAB_CHARACTER = "⠀"


class Issue:
    """An issue with the Dockerfile."""

    id: str = "custom-rule"
    description: str = "A description of the rule"

    def __init__(self, line_number):
        self.line_number = line_number

    @staticmethod
    def create_from(id: str, description: str, line_number=None):
        """Create an issue instance."""

        g = Issue(line_number)
        g.id = id
        g.description = description
        return g

    def __str__(self) -> str:
        """Convert this issue to a human-readable string."""

        if self.line_number is None:
            return self.description

        return " ".join(
            ["line", str(self.line_number), "-", self.description]
        )


def read_dockerfile(file_io_obj) -> list:
    """Reads from the IO stream."""

    lines = dedent(file_io_obj.read().replace(TAB_CHARACTER, " ")).split("\n")
    file_io_obj.close()
    return lines


def lint(dockerfile_path) -> list:
    """Lints the passed Dockerfile."""

    lines = read_dockerfile(dockerfile_path)
    issues = []

    base_image_count = 0
    label_count = 0
    has_reported_base_image_problem = False
    has_reported_label_problem = False

    for index, content in enumerate(lines):
        report_index = index + 1
        c = content

        if checks.has_no_install_rec(c):
            issues.append(
                Issue.create_from(
                    "lacks-no-install-recommends",
                    "uses apt install without no-install-recommends",
                    report_index,
                )
            )

        if parser.is_base_image_definition(c):
            base_image_count = base_image_count + 1

            if base_image_count >= 3 and not has_reported_base_image_problem:
                issues.append(
                    Issue.create_from(
                        "too-many-base-images",
                        "has 3 or more FROM declarations",
                        None,
                    )
                )
                has_reported_base_image_problem = True

        if parser.is_label_definition(c):
            label_count = label_count + 1

            if label_count >= 20 and not has_reported_label_problem:
                issues.append(
                    Issue.create_from(
                        "too-many-labels", "has 20 or more LABELs", None
                    )
                )
                has_reported_label_problem = True

    if len(lines) >= 750:
        issues.append(
            Issue.create_from(
                "long-dockerfile", "has 750 or more lines - wowza!", None
            )
        )

    return issues
