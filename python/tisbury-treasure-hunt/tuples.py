"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    return record[1]


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """

    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """

    coordinate_azara = azara_record[1]
    coordinate_rui = rui_record[1]

    return convert_coordinate(coordinate_azara) == coordinate_rui


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible),
    or the string "not a match" (if incompatible).
    """

    if not compare_records(azara_record, rui_record):
        return "not a match"

    treasure, coordinate_azara = azara_record
    location, coordinate_rui, quadrant = rui_record

    return (treasure, coordinate_azara, location, coordinate_rui, quadrant)


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """

    cleaned_records = map(clean_combined_record, combined_record_group)

    return "".join(cleaned_records)


def clean_combined_record(record):
    """Clean up a record by removing the unwanted duplicate coordinate.

    Args:
        record (tuple): Everything from both participants.

    Returns:
        str: Cleaned record followed by a newline.
    """
    treasure, _, location, coordinate_rui, quadrant = record
    cleaned_record = (treasure, location, coordinate_rui, quadrant)

    return f"{cleaned_record}\n"
