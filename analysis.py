import pandas as pd
from decimal import Decimal
from statsmodels.stats.contingency_tables import Table2x2

def order_total(items):
    return sum(float(it["price"].to_decimal()) * it["quantity"] for it in items)

def add_order_amount(df):
    df = df.copy()
    df["sale_amount"] = df["items"].apply(order_total)
    return df

def coupon_summary(df):
    with_coupon = df[df["couponUsed"]]
    without     = df[~df["couponUsed"]]
    return {
        "mean_with_coupon":    with_coupon["sale_amount"].mean(),
        "mean_without_coupon": without["sale_amount"].mean(),
        "usage_rate_pct":      with_coupon.shape[0] / len(df) * 100,
        "total_revenue":       df["sale_amount"].sum()
    }

def ab_test(exp_df, ctrl_df):
    exp = pd.DataFrame({"coupon": exp_df["couponUsed"], "group": "experiment"})
    ctrl= pd.DataFrame({"coupon": ctrl_df["couponUsed"],"group": "control"})
    crosstab = pd.crosstab(pd.concat([exp, ctrl], ignore_index=True)["coupon"],
                           pd.concat([exp, ctrl], ignore_index=True)["group"])
    table = Table2x2(crosstab.values)
    result = table.test_nominal_association()
    return {
        "chi-square-static": result.statistic,
        "pvalue": result.pvalue,
        "summary": table.summary().as_text()
    }
