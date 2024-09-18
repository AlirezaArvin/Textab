## Introduction
This script processes the output of meta-analysis objects generated using the `{meta}` package in R and exports the following statistics as tabular data in CSV format:
1. Title of the meta-analysis object
2. Number of studies included in the analysis
3. Pulled effect size with 95% confidence intervall
4. P-value of the pulled effect size
5. I² statistic

## Input
The input file must be in `.txt` format and contain the content of a meta object. To generate this file, you can use the following code in R:  
```R
sink("input.txt")
# Replace with the names of your meta objects
meta_object_name
sink()
```
This code exports the results of the meta-analysis stored in the meta objects to a `.txt` file named `input.txt`, which will be saved in your R working directory.  

## Getting started
To use the script, simply follow these two steps:  

**1. Replace the Input File Path:** Locate the line at the beginning of the script that specifies the path for the input file and replace `Enter the path for your txt file here.` with the actual path to your file:  
```Python
with open("Enter the path for your txt file here.") as f:
```
**Note:** The path should be formatted like this: `C:\\folder1\\folder2\\input.txt`. Use double backslashes `(\\)` instead of single backslashes in the path.

**2. Specify the Output File Path:** Locate the line at the end of the script that specifies the path for the output CSV file and replace `Enter the desired path to export and save the resulting CSV file.` with your desired path:  
```Python
result = open("Enter the desired path to export and save the resulting CSV file.", 'w')
```
**Note:** The path should be formatted like this: `C:\\folder1\\folder2\\output.csv`. You may choose any name for the CSV file, but ensure that it ends with the `.csv` extension.
