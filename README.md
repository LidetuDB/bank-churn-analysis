# Bank Customer Churn Analysis

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Library](https://img.shields.io/badge/Library-Pandas%20|%20Seaborn-orange)
![Status](https://img.shields.io/badge/Status-Completed-green)

## Overview

This project analyzes a bank customer dataset containing 10,000 records to understand why customers leave and identify patterns that can help reduce churn rates. Customer retention is critical in banking since acquiring new customers costs significantly more than keeping existing ones.

## Dataset

The analysis uses `Bank_Churn.csv` with these key features:

| Feature | Description |
|---------|-------------|
| **CreditScore** | Customer credit rating |
| **Geography** | Location (France, Spain, Germany) |
| **Age** | Customer age |
| **Tenure** | Years with the bank |
| **Balance** | Account balance |
| **NumOfProducts** | Number of products held (1-4) |
| **IsActiveMember** | Activity status (1 = Active, 0 = Inactive) |
| **Exited** | Target variable (1 = Churned, 0 = Retained) |

## Data Preparation

The dataset was cleaned by:
- Removing non-predictive columns (RowNumber, CustomerId, Surname)
- Encoding categorical variables (Gender, Geography) for analysis

```python
# Drop unnecessary columns
cols_to_drop = ['RowNumber', 'CustomerId', 'Surname']
df_clean = df.drop(cols_to_drop, axis=1)

# Encode geography
df_encoded = pd.get_dummies(df_clean, columns=['Geography'], drop_first=True)
```

## Key Findings

### 1. Age is the Strongest Predictor

Customers aged 40-60 show significantly higher churn rates. The average age of churned customers is 44.8 years compared to 37.4 for retained customers.

```python
sns.kdeplot(data=df[df['Exited'] == 0]['Age'], label='Retained', fill=True)
sns.kdeplot(data=df[df['Exited'] == 1]['Age'], label='Churned', fill=True)
```
![Age Distribution](https://raw.githubusercontent.com/LidetuDB/bank-churn-analysis/main/images/age_distribution-1.png)


### 2. Geographic Disparity

German customers churn at twice the rate of those in France and Spain:
- France & Spain: ~16% churn rate
- Germany: ~32% churn rate

 ![Geography Churn](https://raw.githubusercontent.com/LidetuDB/bank-churn-analysis/main/images/geography_churn.png) 

This suggests operational or competitive issues specific to the German market.

### 3. Product Complexity Problem

More products doesn't mean better retention:
- 2 Products: Lowest churn (optimal)
- 3 Products: 82% churn rate
- 4 Products: 100% churn rate

 ![Product Churn](https://raw.githubusercontent.com/LidetuDB/bank-churn-analysis/main/images/product_churn.png) 

Customers holding 3+ products are highly likely to leave, indicating these bundles may be too complex or expensive.

Recommendations
Based on these findings, the following actions are recommended:
1. Target the 40-60 Demographic

Launch a "Senior Loyalty" program with exclusive benefits
Offer retirement planning advisory services
Provide higher yield savings accounts to retain this mature demographic

2. German Market Audit

Conduct targeted surveys specifically for German account holders
Investigate local competitor offerings and pricing
Consider region-specific retention bonuses or incentives
Review service quality and operational issues in German branches

3. Restructure Product Bundles

The 3-product and 4-product accounts show critical churn rates
Review and simplify the fee structure for multi-product accounts
Reduce complexity for customers holding multiple products
Consider consolidating or redesigning these bundles to improve user experience

4. Re-engage Inactive Users

Inactive members (IsActiveMember=0) represent high-risk customers
Implement automated email campaigns with personalized messaging
Offer small financial incentives to encourage login or transaction activity
Create targeted "We miss you" campaigns with clear value propositions
