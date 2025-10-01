import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def _coupon_segments(df: pd.DataFrame) -> pd.DataFrame:
    """Return coupon usage % by age_group & purchaseMethod."""
    seg = (
        df.groupby(["age_group","purchaseMethod"])
          .agg(
              n_sales=("couponUsed","count"),
              n_coupon=("couponUsed","sum")
          )
          .reset_index()
    )
    seg["pct_coupon"] = seg["n_coupon"] / seg["n_sales"] * 100
    return seg

def coupon_heatmap(df: pd.DataFrame, title: str):
    """Plot a heatmap of coupon usage for a dataset."""
    segments = _coupon_segments(df)
    pivot = segments.pivot(
        index="age_group",
        columns="purchaseMethod",
        values="pct_coupon"
    )
    fig, ax = plt.subplots(figsize=(8,5))
    sns.heatmap(pivot, annot=True, fmt=".1f", cmap="Oranges", ax=ax)
    ax.set_title(title)
    return fig

def compare_coupon_tables(ctrl: pd.DataFrame, exp: pd.DataFrame) -> pd.DataFrame:
    """Return side-by-side coupon % for control vs experiment."""
    c = _coupon_segments(ctrl).rename(columns={"pct_coupon": "pct_ctrl"})
    e = _coupon_segments(exp).rename(columns={"pct_coupon": "pct_exp"})

    merged = c.merge(e, on=["age_group", "purchaseMethod"], how="outer")

    # fill only numeric columns, leave categoricals alone
    num_cols = merged.select_dtypes(include="number").columns
    merged[num_cols] = merged[num_cols].fillna(0)

    merged["diff"] = merged["pct_exp"] - merged["pct_ctrl"]
    return merged.sort_values(["age_group", "purchaseMethod"])
