import os.path
import sys
import pandas as pd
import file_parser as fp

# Headers for weather data file
headers = ['Dy', 'MxT', 'MnT', 'AvT', 'HDDay', 'AvDP', '1HrP', 'TPcpn', 'WxType', 'PDir', 'AvSp', 'Dir', 'MxS',
           'SkyC', 'MxR', 'MnR', 'AvSLP']

# Check command line arguments for filename, default to 'w_data.dat' if not provided
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = 'w_data.dat'

# Check that file is present
if os.path.exists(filename):
    # Read file into pandas dataframe
    header_line = fp.find_header_row(filename, headers)
    widths = fp.get_col_widths(filename, header_line)
    # read_fwf doesn't count blank lines, so account for that
    df = pd.read_fwf(filename, colspecs=widths, skiprows=header_line-1)

    # Clean data
    df = df[['Dy', 'MxT', 'MnT']]  # Keep only relevant columns
    df = df[df['Dy'].apply(lambda x: str(x).isdigit())]  # Drop all rows that aren't valid dates
    df['MxT'] = df['MxT'].str.extract('([0-9]+[.]*[0-9]*)')
    df['MnT'] = df['MnT'].str.extract('([0-9]+[.]*[0-9]*)')

    # Calculate temperature spread for each day
    df['spread'] = ""  # Add empty column to store temperature spread
    min_temp_spread = float("inf")  # Set initial min as arbitrarily large value
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
