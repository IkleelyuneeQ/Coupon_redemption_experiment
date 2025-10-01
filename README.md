# Customer Coupon Redemption A/B Test

This project investigates whether sending coupons (reminder emails / checkout offers) increases redemption and sales.
It uses MongoDB Atlas for data storage, pandas for feature engineering, and statistical testing with statsmodels & scipy.

Project Overview

Queried sales data from MongoDB (sample_supplies.sales collection).

Engineered customer features: age_group, purchaseMethod, storeLocation.

Designed an A/B test by synthesizing an experimental group (experimentFlag=True).

Performed chi-square association test to measure coupon redemption differences.

Analyzed Average Order Value (AOV) and coupon redemption lift.

Visualized results with heatmaps and statistical summaries.


ab_experiment/

│── app.py                  # Streamlit app to visualize coupon analysis

│── config.py               # MongoDB connection (loads from .env)

│── charts.py               # Helper functions for plots

│── analysis.py             # Statistical analysis functions

│── insight_report.md       # Project report (markdown)

│── ab-testing-couponbook.ipynb   # Jupyter notebook with experiment workflow


Setup Instructions

git clone https://github.com/your-username/ab_experiment.git
cd ab_experiment


MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/sample_supplies

install required packages

streamlit run app.py

Key Insights

Coupons increase customer engagement and sales.

Younger demographics (<25) show the highest coupon usage.

Phone/Online channels outperform in-store for coupon redemption.

Significant lift in AOV observed in experimental group.

