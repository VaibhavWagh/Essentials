#USAGE: python3 column_extract.py Huge_data_file.txt Column_headers.tsv Output_file.txt
import pandas as pd
import sys
import os

Input_file1 =sys.argv[1]
Input_file2 =sys.argv[2]
Output_file =sys.argv[3]

# Read the tab-separated file into a pandas DataFrame
#this Input_file1 can be set for a compresed gzip file i.e. .gzip or .gz extensions #please add/remove the compression argument in case you are using uncompressed files.

df = pd.read_csv(Input_file1, delimiter='\t', low_memory=False)#,compression='gzip'

# Read the column header list from the txt file
with open(Input_file2, 'r') as f:
    headers = [line.strip() for line in f.readlines()]

# Select only the above columns from the df that match the column header list
selected_columns = df.loc[:10, headers[:]]

# Write the selected columns to a new tab-separated file
selected_columns.to_csv(Output_file, sep='\t', index=False)

print("Successful")

