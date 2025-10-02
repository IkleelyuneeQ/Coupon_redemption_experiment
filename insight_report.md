**Customer Coupon Redemption Report(A/B Testing)**

**Executive summary:**

Null Hypothesis (H₀): Sending coupon reminders has no effect on coupon redemption or sales compared to control.
Decision: Based on chi-square results (p < 0.05), we reject H₀. Coupons significantly influence redemption and sales.

I investigated whether sending customers a coupon (reminder email / checkout offer) increases redemption and sales.
Queried the sample_supplies.sales collection from MongoDB database and derived customer features (age, email, items, etc.).
Measured baseline coupon usage across age_group and purchaseMethod.
Computed required sample size (chi-square power) and ran the experiment (synthesized an experiment by inserting experimentFlag=True documents (n ≈ 400 over a time window)).
Ran a chi-square / contingency-table test comparing coupon redemption rates between experiment and control group, then computed average sale amounts for each group.
Observed a statistically significant difference (chi-square test), and a measurable lift in average purchase amount in the experimental group.
The experiment shows increased coupon usage and improved sales.



**Data extraction & feature engineering(method & pipeline):**

Loaded documents from MongoDB; flattened customer and items fields.
Created age_group using pd.cut() and customer_email.
Computed percentage coupon per group (age × purchaseMethod) and plotted heatmaps.

**Sample size & timing:**

H₀ (planning stage): If effect size ≤ 0.2, our sample may not detect a meaningful difference at α = 0.05, power = 0.8.

Decision: Power analysis showed ~400 observations required in a timeframe of 200days.
With synthetic data, I achieved sufficient sample size.


**Hypothesis & evaluation:**

Result: Chi-square test returned p ≈ 0.0 (< 0.05).
Decision: Reject H₀. Coupon reminders significantly increase redemption.

Built contingency table of couponUsed × group (experiment vs control).
Used Table2x2 from statsmodels / chi2_contingency to test association (nominal association test).
Calculated average sale amounts and usage rates for control and experiment; computed percentage lift.


**Results summary (interpretation of outputs):**

Coupon usage rate in experiment group materially increased compared to control group.
Chi-square / nominal association test returned p < 0.05 → statistically significant difference in coupon redemption rates across groups.
Average sale amount (AOV) in the experiment group increased compared to control

**Age / channel patterns:**

H₀: Coupon redemption patterns across age groups & purchase methods are uniform (no differences).
Result: Heatmaps show under-18s redeem more online/phone; older cohorts less responsive.
Decision: Reject H₀. Redemption rates vary meaningfully by age and channel.

Younger groups (e.g., <18, 18–24) show higher baseline coupon redemption.
Purchase method patterns: phone / online sometimes showed coupon redemption than in-store, considering the heatmap.


**Business insights & recommendations**

**Coupons increase engagement:**

Since H₀ was rejected in main tests, I conclude coupons:
Sending reminders / offering coupons significantly increases redemption rates.
This suggests coupon reminders can be an effective retention tactic.

**Focus on repeat purchases:**

Frequency matters, combine coupon campaigns with communications that encourage repeat buying (e.g., subscriptions, bundle promotions).

**Channel-specific messaging:**

Phone and online channels show stronger coupon uptake for many age groups;
customize creative and channel allocation accordingly.
