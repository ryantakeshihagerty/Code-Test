import os.path
import sys
import pandas as pd

# Check command line arguments for filename, default to 'soccer.dat' if not provided
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = 'soccer.dat'

# Check that file is present
if os.path.exists(filename):
    # Add relevant data (team, points for, points against) to dataframe
    # Skipping 1st row with '<pre>'
    df = pd.read_fwf(filename, colspecs=[(7, 23), (43, 50), (50, 56)], skiprows=1, header=1)

    # Add empty column to store goal differences
    df['diff'] = ""

    # Clean data
    df['F'] = df['F'].str.extract('(\d+)', expand=False)  # Remove non-integer values (e.g. '-')
    df = df.dropna()  # Remove entries with NaN

    min_goal_diff = sys.maxsize  # Set initial min as arbitrarily large value

    # Calculate goal difference for each team
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
