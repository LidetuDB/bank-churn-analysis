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
![Age Distribution](https://raw.githubusercontent.com/LidetuDB/bank-churn-analysis/main/images/age_distribution.png)


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

## Recommendations

**Focus on the 40-60 Age Group**
- Develop targeted retention programs
- Offer specialized financial products for this demographic

**Address Germany Market Issues**
- Conduct customer satisfaction surveys in Germany
- Review competitive landscape and adjust offerings

**Simplify Multi-Product Accounts**
- Audit the 3 and 4 product bundles
- Reduce complexity and fees for these accounts

**Reactivate Inactive Members**
- Create engagement campaigns for inactive customers
- Offer incentives to encourage account activity

## Setup

Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/bank-churn-analysis.git
```

Install dependencies:
```bash
pip install pandas numpy matplotlib seaborn
```

Run the analysis:
```bash
python churn_analysis.py
```

## Project Structure

```
bank-churn-analysis/
│
├── Bank_Churn.csv
├── churn_analysis.py
├── images/
│   ├── age_distribution.png
│   ├── geography_churn.png
│   └── product_churn.png
└── README.md
```

## Author

Lidetu Tesfaye
