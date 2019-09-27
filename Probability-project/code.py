# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)
fico_credit_score = df['fico']
#fico_credit_store
fico = df[df['fico'] > 700]
p_a = len(fico)/len(fico_credit_score)
p_a

p = df['purpose']
purpose = df[df['purpose'] == 'debt_consolidation']
p_b = len(purpose)/len(p)

p_b

df1 = df[df['purpose'] == 'dbt_consolidation']

p_a_b = p_b/p_a
p_a_b

result = (p_a_b == p_a)
print(result)
# code ends here


# --------------
# code starts here
a = df['paid.back.loan']
#df['paid.back.loan']
loan_paid_back = df[df['paid.back.loan'] == 'Yes']
prob_lp = len(loan_paid_back)/len(a)

b = df['credit.policy']
credit_policy = df[df['credit.policy'] == 'Yes']
prob_cs = len(credit_policy)/len(b)

new_df = df[df['paid.back.loan'] == 'Yes']

prob_pd_cs = new_df[new_df['credit.policy'] == 'Yes'].shape[0]/new_df.shape[0]


bayes = prob_pd_cs*prob_lp/prob_cs
print(bayes)
# code ends here


# --------------
# code starts here
df['purpose'].value_counts().plot.bar()
plt.show()

df1 = df[df['paid.back.loan'] == 'No']

ax = df1['purpose']#.plot(kind='bar',figsize=(15, 10), legend=True, fontsize=12)
df1['purpose'].value_counts().plot(kind='bar',figsize=(15, 10), legend=True, fontsize=12)
plt.show()

# code ends here


# --------------
# code starts here
inst_median = df['installment'].median()
inst_median

inst_mean = df['installment'].mean()

df['installment'].plot.hist(bins=20)
df['log.annual.inc'].plot.hist(bins=20)
# code ends here


