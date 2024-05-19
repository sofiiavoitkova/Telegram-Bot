import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('table.xlsx')
df = df.fillna(0)
def numFormat(value, _):
    return f'{value:,}'

# 1st chart
plt.figure(figsize=(11, 6))

sns.lineplot(data=df, x='Year', y='EU mh', label='Number of Mental Health cases', linewidth=3.0, marker='o',
             color='purple')
sns.lineplot(data=df, x='Year', y='EU covid', label='Number of Covid-19 cases', linewidth=3.0, marker='o',
             color='deeppink')

plt.xlabel('Year', fontsize=13)
plt.ylabel('Amount of people', fontsize=13)
plt.title('Trend of Mental Health in EU before and during Covid-19', fontsize=14)

plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(numFormat))

plt.savefig('plot_EU.jpg', dpi=300)
plt.show()
plt.clf()

# 2nd figure
plt.figure(figsize=(11, 6))

sns.lineplot(data=df, x='Year', y='US mh', label='Number of Mental Health cases', linewidth=3.0, marker='o',
             color='green')
sns.lineplot(data=df, x='Year', y='US covid', label='Number of Covid-19 cases', linewidth=3.0, marker='o',
             color='darkgoldenrod')

plt.xlabel('Year', fontsize=13)
plt.ylabel('Amount of people', fontsize=13)
plt.title('Trend of Mental Health in US before and during Covid-19', fontsize=14)

plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(numFormat))

plt.savefig('plot_US.jpg', dpi=300)
plt.show()