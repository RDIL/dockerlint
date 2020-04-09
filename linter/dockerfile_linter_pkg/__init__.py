from . import rule_validation as checks, parse as parser

TAB_CHARACTER = "⠀"


class Issue:
    """An issue with the Dockerfile."""

    id: str = "custom-rule"
    description: str = "A description of the rule"
    line_number: int

    def __init__(self, line_number):
        self.line_number = line_number

    @staticmethod
    def create_from(id, description, line_number):
        """Create an issue instance."""

        g = Issue(line_number)
        g.id = id
        g.description = description
        return g

    def __str__(self):
        return " ".join([
            "line",
            str(self.line_number),
            "-",
            self.description
        ])


def read_dockerfile(file_io_obj):
    """Reads from the IO stream."""

    lines = file_io_obj.readlines()
    file_io_obj.close()
    return lines


def lint(dockerfile_path):
    """Lints the passed Dockerfile."""

    lines = read_dockerfile(dockerfile_path)
    issues = []

    base_image_count = 0
    report_index = 0
    has_reported_base_image_problem = False

    for index, content in enumerate(lines):
        report_index = index + 1
        c = trim_starting_spaces(content)

        if checks.has_no_install_rec(c):
            issues.append(
                Issue.create_from(
                    "n-i-r",
                    "uses apt install without no-install-recommends",
                    report_index
                )
            )

        if parser.is_base_image_definition(c):
            base_image_count = base_image_count + 1

            if base_image_count >= 3 and not has_reported_base_image_problem:
                issues.append(
                    Issue.create_from(
                        "many-base-images",
                        " has 3 or more FROM declarations"
                    )
                )
                has_reported_base_image_problem = True

    return issues


def trim_starting_spaces(line):
    """
    Right now this just removes tab characters,
    but in the future it (should) remove any spaces before
    actual letters/numbers etc.
    """

    return line.replace(TAB_CHARACTER, " ")
