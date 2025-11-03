# Data Download Instructions

## Large Dataset Files

Due to GitHub file size limitations, some large CSV files are not included in this repository. To run the complete analysis, you'll need to download these files from Statistics Canada:

### Required Downloads:

1. **Death_By_Cause.csv** (100.34 MB)
   - Source: Statistics Canada - Leading causes of death
   - URL: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310039401
   - Place in: `data/Death_By_Cause.csv`

2. **Perceived_Health_Canada_2015.csv** (62.99 MB)  
   - Source: Statistics Canada - Perceived health by province and sex
   - URL: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310009602
   - Place in: `data/Perceived_Health_Canada_2015.csv`

### Included Files:
- ✅ `BMI.csv` (6.11 MB) - Body mass index data
- ✅ `Life_Expectancy_Canada_2000_to_2007.csv` (4.98 MB) - Life expectancy data
- ✅ `cleaned_bmi_data.csv` (0.01 MB) - Processed BMI data

### Quick Setup:
1. Create the `data/` directory if it doesn't exist
2. Download the two large files from the URLs above
3. Place them in the `data/` directory
4. Run the Jupyter notebook

The analysis will work with the included smaller datasets, but for complete results, all files are recommended.