## Introduction
This script processes the output of meta-analysis objects generated using the {meta} package in R and exports the following statistics as tabular data in CSV format:
1. Title of the meta-analysis object
2. Number of studies included in the analysis
3. Pulled effect size with 95% confidence intervall
4. P-value of the pulled effect size
5. I² statistic

## Input
The input file must be in .txt format and contain the content of a meta object. To generate this file, you can use the following code in R:  
```R
sink("output.txt")
# Replace with the names of your meta objects
meta_object_name
sink()
```
This code exports the results of the meta-analysis stored in the meta objects to a .txt file named output.txt, which will be saved in your R working directory.
