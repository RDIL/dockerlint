import sys
import os.path
from . import rule_validation as checks

TAB_CHARACTER = "⠀"


class Issue:
    id: str = "custom-rule"
    description: str = "A description of the rule"
    line_number: int

    def __init__(self, line_number):
        self.line_number = line_number

    @staticmethod
    def create_from(id, description, line_number):
        g = Issue(line_number)
        g.id = id
        g.description = description
        return g

    def __str__(self):
        return " ".join([
            str(self.line_number),
            "-",
            self.description,
            self.id
        ])


def read_dockerfile(dockerfile_path):
    if not os.path.exists(dockerfile_path):
        print("FAIL    Specified Dockerfile doesn't exist!")
        sys.exit(1)

    filehandler = open(dockerfile_path, mode="r")
    lines = filehandler.readlines()
    filehandler.close()
    return lines


def lint(dockerfile_path):
    lines = read_dockerfile(dockerfile_path)
    issues = []
    for index, content in enumerate(lines):
        c = trim_starting_spaces(content)
        report_index = index + 1
        if checks.has_no_install_rec(c):
            issues.append(
                Issue.create_from(
                    "n-i-r",
                    " uses apt install without no-install-recommends",
                    report_index
                )
            )
    return issues


# todo
def trim_starting_spaces(line):
    return line.replace(TAB_CHARACTER, " ")
