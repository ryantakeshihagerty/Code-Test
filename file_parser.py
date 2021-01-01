import linecache


def find_header_row(file, headers):
    """Return line number that contains the column headers."""
    with open(file) as data_file:
        for i, line in enumerate(data_file):
            current_line = line.split()
            if current_line == headers:
                return i + 1


def get_col_widths(file, header_row):
    """Return list of tuples containing fixed-width fields for each column."""
    # Get the header row from file
    header = linecache.getline(file, header_row)

    num_of_columns = len(header.split())

    col_widths = []
    beg = 0

    while len(col_widths) < num_of_columns:
        # Find first char of current column
        while header[beg] == ' ':
            beg += 1
        end = beg

        # Special case if on last column
        if len(col_widths) == num_of_columns - 1:
            col_widths.append((beg, len(header) - 1))
            break

        # Keep incrementing end ptr until whitespace reached
        while header[end] != ' ':
            end += 1

        # Keep incrementing until first char of next col reached
        while header[end] == ' ':
            end += 1

        col_widths.append((beg, end))
        beg = end

    return col_widths
