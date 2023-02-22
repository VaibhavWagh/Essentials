#vlookup script mainly for mapping information to IDS or any matching column
#Usage: python3 vlookup.py IDs.txt Target_Metadata.txt Mapped_File.txt
#PS: The column name should be identical
#Filetypes TSV files


import sys
import numpy as np
import pandas as pd

inputfile1 =sys.argv[1]
inputfile2 =sys.argv[2]

outputfile =sys.argv[3]

print( "This script will map information from ",inputfile2,"on",inputfile1)
table1=pd.read_csv(inputfile1,sep="\t")#,header=None,sep='\t')
table2=pd.read_csv(inputfile2,sep="\t")#,header=None,sep='\t')

print("IDs Input file",table1.head(5))
print("Information Input file",table2.head(5))
result = pd.merge(table1,table2, how='left')
#print(result.head(10))
result=result.fillna("NA")
result.to_csv(outputfile, index=None, sep='\t')
print(result.head(10))
print("Completed Successfully and written into",outputfile)
