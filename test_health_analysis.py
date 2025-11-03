"""
Test file for health outcomes analysis functions
"""
import pytest
import pandas as pd
import numpy as np
import os

def test_data_files_exist():
    """Test that required data files exist"""
    required_files = [
        'data/BMI.csv',
        'data/Life_Expectancy_Canada_2000_to_2007.csv',
        'data/cleaned_bmi_data.csv'
    ]
    
    for file_path in required_files:
        assert os.path.exists(file_path), f"Required data file {file_path} not found"

def test_bmi_data_structure():
    """Test that BMI data has expected structure"""
    if os.path.exists('data/BMI.csv'):
        bmi_data = pd.read_csv('data/BMI.csv')
        
        # Check that we have data
        assert not bmi_data.empty, "BMI data should not be empty"
        
        # Check for expected columns (adjust based on your actual column names)
        expected_columns = ['REF_DATE', 'GEO', 'Sex']
        for col in expected_columns:
            assert col in bmi_data.columns, f"Expected column {col} not found"

def test_visualizations_exist():
    """Test that visualization files were generated"""
    viz_files = [
        'visualizations/average_obesity_rate_by_province.png',
        'visualizations/correlation_matrix_health_indicators.png',
        'visualizations/life_expectancy_by_province.png',
        'visualizations/mortality_rates_heatmap.png',
        'visualizations/perceived_health_by_province.png'
    ]
    
    for viz_file in viz_files:
        assert os.path.exists(viz_file), f"Visualization file {viz_file} not found"

def test_correlation_calculation():
    """Test correlation calculation logic"""
    # Sample data for testing
    test_data = pd.DataFrame({
        'Life_Expectancy': [80, 78, 82, 75],
        'Obesity_Rate': [15, 20, 12, 25],
        'Perceived_Health': [45, 40, 50, 35]
    })
    
    correlation = test_data.corr()
    
    # Check that correlation matrix is properly formatted
    assert correlation.shape == (3, 3), "Correlation matrix should be 3x3"
    assert not correlation.isna().any().any(), "Correlation matrix should not contain NaN values"