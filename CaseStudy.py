import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

# ==========================================================
# FILE PATHS
# ==========================================================

folder = r"C:\Users\rajar\OneDrive\Desktop\Financial Crisis Paper\Case Study Malaysia\Final Excel Files for Case Study"

shariah_file = folder + r"\Shariah_Firms_2005_2025.xlsx"
conv_file = folder + r"\Conventional_Firms_2005_2025.xlsx"

# ==========================================================
# LOAD DATA
# ==========================================================

shariah = pd.read_excel(shariah_file)
conv = pd.read_excel(conv_file)

# Convert numeric
for df in [shariah, conv]:
    df["ROE"] = pd.to_numeric(df["ROE"], errors="coerce")
    df["EPS"] = pd.to_numeric(df["EPS"], errors="coerce")

# ==========================================================
# SETTINGS
# ==========================================================

periods = ["Pre-GFC", "GFC", "Pre-COVID", "COVID"]
variables = ["ROE", "EPS"]

# ==========================================================
# TABLE 7: DESCRIPTIVE STATISTICS (UNCHANGED)
# ==========================================================

def descriptive(df, group_name):

    rows = []

    for var in variables:
        for period in periods:

            data = df[df["PERIOD"] == period][var].dropna()

            rows.append([
                group_name,
                var,
                period,
                len(data),
                round(data.mean(), 4) if len(data) > 0 else np.nan,
                round(data.median(), 4) if len(data) > 0 else np.nan,
                round(data.min(), 4) if len(data) > 0 else np.nan,
                round(data.max(), 4) if len(data) > 0 else np.nan,
                round(data.std(), 4) if len(data) > 0 else np.nan
            ])

    return pd.DataFrame(rows, columns=[
        "Group",
        "Variable",
        "Period",
        "N",
        "Mean",
        "Median",
        "Minimum",
        "Maximum",
        "Std Dev"
    ])

shariah_desc = descriptive(shariah, "Shariah")
conv_desc = descriptive(conv, "Conventional")

descriptive_table = pd.concat([shariah_desc, conv_desc], ignore_index=True)

# ==========================================================
# TABLE 8A: T-TEST RESULTS (ROE ONLY)
# ==========================================================

ttest_roe = []

for period in periods:

    sh = shariah[shariah["PERIOD"] == period]["ROE"].dropna()
    cv = conv[conv["PERIOD"] == period]["ROE"].dropna()

    t_stat, p_val = ttest_ind(sh, cv, equal_var=False, nan_policy="omit")

    ttest_roe.append([
        period,
        len(sh),
        len(cv),
        round(sh.mean(), 4),
        round(cv.mean(), 4),
        round(t_stat, 4),
        round(p_val, 4),
        "Reject H0" if p_val < 0.05 else "Fail to Reject H0"
    ])

ttest_roe_table = pd.DataFrame(ttest_roe, columns=[
    "Period",
    "N (Shariah)",
    "N (Conventional)",
    "Mean (Shariah)",
    "Mean (Conventional)",
    "t-Statistic",
    "p-Value",
    "Decision"
])

# ==========================================================
# TABLE 8B: T-TEST RESULTS (EPS ONLY)
# ==========================================================

ttest_eps = []

for period in periods:

    sh = shariah[shariah["PERIOD"] == period]["EPS"].dropna()
    cv = conv[conv["PERIOD"] == period]["EPS"].dropna()

    t_stat, p_val = ttest_ind(sh, cv, equal_var=False, nan_policy="omit")

    ttest_eps.append([
        period,
        len(sh),
        len(cv),
        round(sh.mean(), 4),
        round(cv.mean(), 4),
        round(t_stat, 4),
        round(p_val, 4),
        "Reject H0" if p_val < 0.05 else "Fail to Reject H0"
    ])

ttest_eps_table = pd.DataFrame(ttest_eps, columns=[
    "Period",
    "N (Shariah)",
    "N (Conventional)",
    "Mean (Shariah)",
    "Mean (Conventional)",
    "t-Statistic",
    "p-Value",
    "Decision"
])

# ==========================================================
# EXPORT TO EXCEL
# ==========================================================

output_file = folder + r"\Case_Study_Final_Tables.xlsx"

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:

    descriptive_table.to_excel(writer, sheet_name="Table 7 Descriptive Stats", index=False)

    ttest_roe_table.to_excel(writer, sheet_name="Table 8A ROE T-Test", index=False)

    ttest_eps_table.to_excel(writer, sheet_name="Table 8B EPS T-Test", index=False)

print("==================================================")
print("TABLES GENERATED SUCCESSFULLY:")
print("1. Descriptive Statistics (unchanged)")
print("2. ROE T-Test Table")
print("3. EPS T-Test Table")
print("SAVED AT:")
print(output_file)
print("==================================================")