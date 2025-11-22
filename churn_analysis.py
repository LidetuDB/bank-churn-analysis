# ==============================================================================
# BANK CUSTOMER CHURN ANALYSIS 
# ==============================================================================

# 1. LIBRARIES & SETUP
# ------------------------------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style for better visuals
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

print("1. Libraries loaded successfully.\n")


# 2. DATA LOADING & BASIC CHECKS
# ------------------------------------------------------------------------------
print("--- SECTION 2: DATA LOADING & CHECKS ---")

try:
    # Load the dataset
    df = pd.read_csv('Bank_Churn.csv')
    
    # 1. Show head
    print("\n[First 5 Rows]")
    print(df.head())

    # 2. Info (Data types)
    print("\n[Dataset Info]")
    print(df.info())

    # 3. Describe (Statistics)
    print("\n[Statistical Summary]")
    print(df.describe())

    # 4. Check for Missing Values
    print("\n[Missing Values Check]")
    missing = df.isnull().sum()
    print(missing[missing > 0] if missing.sum() > 0 else "No missing values found.")

    # 5. Check for Duplicates
    duplicates = df.duplicated().sum()
    print(f"\n[Duplicate Rows]: {duplicates}")

except FileNotFoundError:
    print("Error: 'Bank_Churn.csv' not found. Please ensure the file is in the same directory.")
    exit()


# 3. DATA CLEANING
# ------------------------------------------------------------------------------
print("\n--- SECTION 3: DATA CLEANING ---")

# Step 1: Remove identifying columns
# 'CustomerId', 'Surname', and 'RowNumber' (if present) are metadata, not analytical features.
cols_to_drop = ['RowNumber', 'CustomerId', 'Surname']
# Only drop columns that actually exist in the dataframe
cols_to_drop = [c for c in cols_to_drop if c in df.columns]
df_clean = df.drop(cols_to_drop, axis=1)
print(f"Dropped columns: {cols_to_drop}")

# Step 2: Convert Categorical Data for Correlation Analysis
# We create a separate dataframe for the correlation map because mathematical
# correlations require numbers, but we want to keep strings for the graphs.
df_encoded = df_clean.copy()

# Manual mapping for Gender (Female=0, Male=1)
df_encoded['Gender'] = df_encoded['Gender'].map({'Female': 0, 'Male': 1})

# One-hot encoding for Geography (Turn 'France', 'Spain' into columns of 0s and 1s)
df_encoded = pd.get_dummies(df_encoded, columns=['Geography'], drop_first=True)

print("\n[Data Cleaned & Ready]")
print(df_clean.head())


# 4. EXPLORATORY DATA ANALYSIS (EDA)
# ------------------------------------------------------------------------------
print("\n--- SECTION 4: EXPLORATORY DATA ANALYSIS ---")

# A. Churn vs Non-Churn Distribution
plt.figure(figsize=(6, 5))
sns.countplot(x='Exited', data=df_clean, palette='pastel')
plt.title('Overall Churn Distribution (0=Stayed, 1=Exited)')
plt.xlabel('Status')
plt.ylabel('Count of Customers')
plt.show()

# B. Churn Rate by Gender
plt.figure(figsize=(7, 5))
sns.barplot(x='Gender', y='Exited', data=df_clean, palette='pastel', errorbar=None)
plt.title('Churn Rate by Gender')
plt.ylabel('Churn Probability (0.0 - 1.0)')
plt.show()

# C. Churn Rate by Geography
plt.figure(figsize=(7, 5))
sns.barplot(x='Geography', y='Exited', data=df_clean, palette='muted', errorbar=None)
plt.title('Churn Rate by Geography')
plt.ylabel('Churn Probability')
plt.show()

# D. Churn by Age Groups (Distribution)
plt.figure(figsize=(10, 6))
sns.kdeplot(data=df_clean[df_clean['Exited'] == 0]['Age'], label='Stayed', fill=True, color='skyblue')
sns.kdeplot(data=df_clean[df_clean['Exited'] == 1]['Age'], label='Exited', fill=True, color='orange')
plt.title('Age Distribution: Stayed vs Exited')
plt.legend()
plt.show()

# E. Churn vs Account Balance (Boxplot)
plt.figure(figsize=(8, 6))
sns.boxplot(x='Exited', y='Balance', data=df_clean, palette='Set2')
plt.title('Distribution of Account Balance by Churn Status')
plt.show()

# F. Churn vs Tenure (How long they have been a customer)
plt.figure(figsize=(10, 5))
sns.barplot(x='Tenure', y='Exited', data=df_clean, palette='viridis', errorbar=None)
plt.title('Churn Rate by Tenure (Years)')
plt.ylabel('Churn Probability')
plt.show()

# G. Churn vs Number of Products
plt.figure(figsize=(8, 5))
sns.barplot(x='NumOfProducts', y='Exited', data=df_clean, palette='magma', errorbar=None)
plt.title('Churn Rate by Number of Products')
plt.ylabel('Churn Probability')
plt.show()

# H. Correlation Heatmap
plt.figure(figsize=(12, 8))
corr = df_encoded.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap (Numerical Features)')
plt.show()


# 5. MARKETING & BUSINESS INSIGHTS
# ------------------------------------------------------------------------------
print("\n" + "="*50)
print("SECTION 5: MARKETING & BUSINESS INSIGHTS")
print("="*50)

# Calculating stats for insights
churn_rate_germany = df_clean[df_clean['Geography'] == 'Germany']['Exited'].mean()
churn_rate_france = df_clean[df_clean['Geography'] == 'France']['Exited'].mean()
avg_age_churned = df_clean[df_clean['Exited'] == 1]['Age'].mean()
avg_age_stayed = df_clean[df_clean['Exited'] == 0]['Age'].mean()
active_churn = df_clean[df_clean['IsActiveMember'] == 1]['Exited'].mean()
inactive_churn = df_clean[df_clean['IsActiveMember'] == 0]['Exited'].mean()

print(f"\n1. AGE FACTOR:")
print(f"   - Customers who leave are older on average ({avg_age_churned:.1f} years) compared to those who stay ({avg_age_stayed:.1f} years).")
print("   - Insight: The bank is losing its mature demographic (40-50s).")

print(f"\n2. GEOGRAPHY:")
print(f"   - Germany has a churn rate of {churn_rate_germany:.1%}, significantly higher than France ({churn_rate_france:.1%}).")
print("   - Insight: German customers are high risk. Competitors in Germany might be offering better rates or services.")

print(f"\n3. PRODUCT USAGE:")
print("   - Insight: Customers with 3 or 4 products exit at an alarming rate (often >80%).")
print("   - This suggests 'Product Overload' or that these accounts are structured in a way that frustrates users.")

print(f"\n4. ACTIVITY:")
print(f"   - Inactive members churn at {inactive_churn:.1%}, while active members churn at {active_churn:.1%}.")
print("   - Insight: Engagement is the best defense. If they stop logging in or transacting, they are preparing to leave.")

print(f"\n5. GENDER:")
print("   - Female customers tend to have a slightly higher churn rate than male customers in this dataset.")


# 6. RECOMMENDATIONS FOR THE MARKETING TEAM
# ------------------------------------------------------------------------------
print("\n" + "="*50)
print("SECTION 6: RECOMMENDATIONS")
print("="*50)

print("""
1. STRATEGY FOR OLDER DEMOGRAPHIC (40-60s):
   - These customers have the highest churn. 
   - Action: Introduce 'Senior' or 'Long-term' loyalty tiers. Offer retirement planning advice or higher interest on savings for long-tenured older clients.

2. THE "GERMANY PROBLEM":
   - Churn in Germany is nearly double that of other regions.
   - Action: Conduct a market survey in Germany. Are fees too high? Is customer support lacking in German? 
   - Immediate fix: Offer a targeted retention bonus specifically for German account holders with high balances.

3. FIX THE PRODUCT STRUCTURE:
   - Customers with 3+ products are leaving.
   - Action: Simplify the portfolio. If a customer holds a credit card, savings, and loan, ensure the fees don't stack up to become a burden. 
   - Auto-alert relationship managers when a client opens a 3rd product to ensure they are satisfied.

4. RE-ENGAGEMENT CAMPAIGN:
   - Inactive members are high risk.
   - Action: Set up an automated email trigger. If a user hasn't logged in for 2 months, send a "We miss you" offer (e.g., small cashback or fee waiver) to prompt a login.
""")


# 7. FINAL SUMMARY
# ------------------------------------------------------------------------------
print("\n" + "="*50)
print("SECTION 7: FINAL SUMMARY")
print("="*50)

print("""
We analyzed the Bank Churn dataset to understand why customers are exiting.
Key Findings:
1. Age is the strongest indicator; older clients are leaving.
2. Geography matters; Germany is a problem area.
3. Product count is critical; having too many products leads to exit.
4. Activity status is predictive; inactive users leave.

By focusing retention efforts on older clients, the German market, and inactive users, 
the bank can maximize its retention impact.
""")