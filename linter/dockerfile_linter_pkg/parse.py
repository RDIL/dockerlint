def is_base_image_definition(line):
    """Returns if the line is a FROM node."""

    return line.startswith("FROM ")
