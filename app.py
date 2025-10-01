import streamlit as st
import data
import analysis
import charts
import pandas as pd

st.set_page_config(page_title="Coupon Experiment Dashboard", layout="wide")

st.title("Coupon Experiment Results")

# Load data
ctrl_raw = data.flatten_customer(data.load_sales(flag=False))
exp_raw  = data.flatten_customer(data.load_sales(flag=True))

ctrl = analysis.add_order_amount(ctrl_raw)
exp  = analysis.add_order_amount(exp_raw)

ctrl_stats = analysis.coupon_summary(ctrl)
exp_stats  = analysis.coupon_summary(exp)

col1, col2 = st.columns(2)
col1.metric(f"Control Avg Sale from {len(ctrl_raw)} sales", f"${ctrl_stats['mean_with_coupon']:.2f}")
col2.metric(f"Experiment Avg Sale from {len(exp_raw)} sales", f"${exp_stats['mean_with_coupon']:.2f}")

st.write("**Control revenue:** ${:,.0f}".format(ctrl_stats["total_revenue"]))
st.write("**Experiment revenue:** ${:,.0f}".format(exp_stats["total_revenue"]))

# A/B test
test = analysis.ab_test(exp, ctrl)
st.subheader("Statistical Test")
st.text(test["summary"])
st.write(f"p-value: {test['pvalue']:.4g}")

# Add age_group column once
bins   = [0,18,25,35,50,65,120]
labels = ["<18","18–24","25–34","35–49","50–64","65+"]
for d in (ctrl_raw, exp_raw):
    d["age_group"] = pd.cut(d["age"], bins=bins, labels=labels)

# Heatmap
st.subheader("Heatmaps of Control & Experiment")
st.pyplot(charts.coupon_heatmap(ctrl_raw, "Control Group"))
st.pyplot(charts.coupon_heatmap(exp_raw, "Experiment Group"))

st.subheader("Comparison Table")
comp_table = charts.compare_coupon_tables(ctrl_raw, exp_raw)
st.dataframe(comp_table)


if __name__ == '__main__':
    print('Starting Coupon Experiment Dashboard')
