import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Display name and Banner ID at the top
st.write("**Sneh Hitendrakumar Patel**")
st.write("**BannerID:** 001395012")

# Load the data
path = 'https://raw.githubusercontent.com/klamsal/Fall2024Exam/refs/heads/main/CleanedAutomobile.csv'
df = pd.read_csv(path)

# Streamlit Title
st.title('Automobile Data Analysis')

# Question 1: Data type of the "peak-rpm" column
st.subheader("1. What is the data type of the column 'peak-rpm'?")
st.write(f"The data type of 'peak-rpm' column is: {df['peak-rpm'].dtype}")

# Question 2: Correlation between selected columns
st.subheader("2. Correlation between 'bore', 'stroke', 'compression-ratio', and 'horsepower'")

selected_columns = df[['bore', 'stroke', 'compression-ratio', 'horsepower']]
correlation_selected = selected_columns.corr()
st.write(correlation_selected)

# Positive Linear Relationship - Engine size vs Price
st.subheader("3. Positive Linear Relationship - Engine size vs Price")
sns.regplot(x="engine-size", y="price", data=df)
plt.ylim(0,)
st.pyplot(plt)

# Inverse Linear Relationship - Highway mpg vs Price
st.subheader("4. Inverse Linear Relationship - Highway mpg vs Price")
sns.regplot(x="highway-mpg", y="price", data=df)
plt.ylim(0,)
st.pyplot(plt)

# Weak Linear Relationship - Peak rpm vs Price
st.subheader("5. Weak Linear Relationship - Peak rpm vs Price")
sns.regplot(x="peak-rpm", y="price", data=df)
plt.ylim(0,)
st.pyplot(plt)

# Question 3a: Correlation between 'stroke' and 'price'
st.subheader("6. Correlation between 'stroke' and 'price'")
st.write(df[["stroke", "price"]].corr())

# Question 3b: Regression plot of 'stroke' vs 'price'
st.subheader("7. Regression Plot of 'stroke' vs 'price'")
sns.regplot(x="stroke", y="price", data=df)
plt.ylim(0,)
plt.title("Regression Plot of Stroke vs Price")
st.pyplot(plt)

# Categorical Variables Visualization
st.subheader("8. Boxplot of Categorical Variables vs Price")

st.write("Boxplot of 'body-style' vs 'price'")
sns.boxplot(x="body-style", y="price", data=df)
st.pyplot(plt)

st.write("Boxplot of 'engine-location' vs 'price'")
sns.boxplot(x="engine-location", y="price", data=df)
st.pyplot(plt)

st.write("Boxplot of 'drive-wheels' vs 'price'")
sns.boxplot(x="drive-wheels", y="price", data=df)
st.pyplot(plt)

# Descriptive Statistical Analysis
st.subheader("9. Descriptive Statistical Analysis")
st.write(df.describe())
st.write(df.describe(include=['object']))

# Value Counts for 'drive-wheels' and 'engine-location'
st.subheader("10. Value Counts for 'drive-wheels' and 'engine-location'")
st.write("Value counts for 'drive-wheels':")
st.write(df['drive-wheels'].value_counts())

st.write("Value counts for 'engine-location':")
st.write(df['engine-location'].value_counts())

# Grouping data by 'body-style' to calculate average price
st.subheader("11. Average Price by Body Style")
avg_price_body_style = df[['body-style', 'price']].groupby(['body-style'], as_index=False).mean()
st.write(avg_price_body_style)

# Group by 'drive-wheels' and 'body-style'
st.subheader("12. Grouping by 'drive-wheels' and 'body-style'")
df_group_one = df[['drive-wheels', 'body-style', 'price']]
df_group_one = df_group_one.groupby(['drive-wheels', 'body-style'], as_index=False).mean()
st.write(df_group_one)

# Creating pivot table for 'drive-wheels' and 'body-style'
st.subheader("13. Pivot Table for 'drive-wheels' and 'body-style'")
grouped_test1 = df[['drive-wheels', 'body-style', 'price']]
grouped_test1 = grouped_test1.groupby(['drive-wheels', 'body-style'], as_index=False).mean()
grouped_pivot = grouped_test1.pivot(index='drive-wheels', columns='body-style').fillna(0)
st.write(grouped_pivot)

# Heatmap Visualization
st.subheader("14. Heatmap of Grouped Data")
plt.figure(figsize=(10, 6))
sns.heatmap(grouped_pivot, annot=True, cmap='RdBu')
st.pyplot(plt)
