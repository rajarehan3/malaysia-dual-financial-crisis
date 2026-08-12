# The Malaysian Dual Financial System Under Stress

## Replication Code

This repository contains the Python replication code for the empirical study:

**"The Malaysian Dual Financial System Under Stress: An Empirical Case Study of Shariah and Conventional Firms During the Global Financial Crisis and COVID-19"**

## Study Overview

The study examines the earnings performance of Shariah-compliant and conventional firms in Malaysia during the Global Financial Crisis (2008–2009) and the COVID-19 pandemic.

The empirical analysis uses Return on Equity (ROE) and Earnings per Share (EPS) as the main profitability measures. Descriptive statistics and independent-samples t-tests are conducted for the pre-crisis and crisis periods.

## Source Code

The main Python script is:

`CaseStudy.py`

The script generates the descriptive statistics and independent-samples t-test results reported in the study.

## Analysis Outputs

The `CaseStudy.py` script generates:

- Descriptive statistics for ROE and EPS for Shariah-compliant and conventional firms.
- Independent-samples t-test results for ROE.
- Independent-samples t-test results for EPS.
- An Excel file containing the resulting statistical tables.

## Data Availability

The underlying financial data were obtained from the Bloomberg database. The processed dataset used for the empirical analysis is available through the Open Science Framework (OSF):

http://osf.io/dw4x3

The datasets are not included in this GitHub repository.

## Software Requirements

The analysis was conducted using Python.

The required Python packages are listed in `requirements.txt`:

- pandas
- numpy
- scipy
- openpyxl

To install the required packages, run:

```bash
pip install -r requirements.txt
