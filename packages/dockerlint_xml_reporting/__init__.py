from junit_xml import TestSuite, TestCase, to_xml_report_string


def create_xml_report(failures, dockerfile_path):
    """Make a full XML report file."""

    test_case = TestCase(
        "Lint " + dockerfile_path,
        classname="dockerlint.main",
    )
    for f in failures:
        test_case.add_failure_info(message=f.__str__())
    ts = TestSuite("dockerlint", test_cases=[test_case])
    return to_xml_report_string([ts])
