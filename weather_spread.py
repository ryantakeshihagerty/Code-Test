import os.path
import sys
import pandas as pd

# Check command line arguments for filename, default to 'w_data.dat' if not provided
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = 'w_data.dat'

# Check that file is present
if os.path.exists(filename):
    # Add relevant data (day, max temp, min temp) to dataframe
    # Skipping 2 rows to account for the lines with '<pre>' and 'MMU June 2002'
    df = pd.read_fwf(filename, colspecs=[(2, 5), (5, 11), (11, 17)], skiprows=2, header=2)

    # Add empty column to store temperature spread
    df['spread'] = ""

    # Clean data
    df = df[df['Dy'].apply(lambda x: str(x).isdigit())]  # Drop all rows that aren't valid dates
    df['MxT'] = df['MxT'].str.replace('*', '')  # Get rid of '*'
    df['MnT'] = df['MnT'].str.replace('*', '')

    min_temp_spread = float("inf")  # Set initial min as arbitrarily large value

    # Calculate temperature spread for each day
    for index, row in df.iterrows():
        row['spread'] = float(row['MxT']) - float(row['MnT'])  # Store temp spread for this day

        # Keep track of the current min
        if row['spread'] < min_temp_spread:
            min_temp_spread = row['spread']
            min_spread_day = row['Dy']

    # Output day with smallest spread
    print("Day with smallest temperature spread: " + str(min_spread_day))
    print("Temperature spread: " + str(min_temp_spread))

else:
    print("ERROR: File \"" + filename + "\" not found")
