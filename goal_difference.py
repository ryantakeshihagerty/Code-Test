import os.path
import sys
import pandas as pd
import file_parser as fp

# Headers for weather data file
headers = ['Team', 'P', 'W', 'L', 'D', 'F', 'A', 'Pts']

# Check command line arguments for filename, default to 'soccer.dat' if not provided
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = 'soccer.dat'

# Check that file is present
if os.path.exists(filename):
    # Read file into pandas dataframe
    header_line = fp.find_header_row(filename, headers)
    widths = fp.get_col_widths(filename, header_line)
    df = pd.read_fwf(filename, colspecs=widths, skiprows=header_line-1)

    # Clean data
    df = df[['Team', 'F', 'A']]  # Keep only relevant columns
    df['F'] = df['F'].str.extract('(\d+)', expand=False)  # Remove non-integer values
    df = df.dropna()  # Remove entries with NaN

    # Calculate goal difference for each team
    df['diff'] = ""  # Add empty column to store goal differences
    min_goal_diff = sys.maxsize  # Set initial min as arbitrarily large value
    for index, row in df.iterrows():
        row['diff'] = abs(int(row['F']) - int(row['A']))  # Store goal difference for this team

        # Keep track of the current min
        if row['diff'] < min_goal_diff:
            min_goal_diff = row['diff']
            min_team = row['Team']

    # Output team with smallest goal difference
    print("Team with smallest goal difference: " + str(min_team))
    print("Goal difference: " + str(min_goal_diff))

else:
    print("ERROR: File \"" + filename + "\" not found")
