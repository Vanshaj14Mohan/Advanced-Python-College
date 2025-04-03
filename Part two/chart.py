import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📕 Data Visualization Web App")

data = pd.read_excel("E:\Advanced Python\Part two\Cardata.xlsx")

st.subheader("5 rows of the dataset")
st.write(data.head(5))

st.subheader("📓 Data Summary")
st.write(data.describe())

# columns = data.columns.tolist()
# st.write(columns)

# x_axis = st.selectbox("Select the X-axis column", columns, index=None)
# y_axis = st.selectbox("Select the Y-axis column", columns, index=None)

# chart = st.radio("Choose Chart Type", ["Line Chart", "Bar Chart", "Scatter plot", "Histogram", "Box Plot"], index=None)

# fig, ax = plt.subplots(figsize=(9,6))

# if chart == "Line Chart":
#     ax.plot(data[x_axis], data[y_axis], marker='o', linestyle="-")
#     ax.set_title(f"Line Chart")

# elif chart == "Bar Chart":
#     ax.bar(data[x_axis], data[y_axis], color="skyblue")
#     ax.set_title(f"Bar Chart")

# elif chart == "Scatter Plot":
#     ax.scatter(data[x_axis], data[y_axis], color="red")
#     ax.set_title(f"Scatter Plot")

# elif chart == "Histogram":
#     ax.hist(data[x_axis], bins=10, color="green", edgecolor="black")
#     ax.set_title("Histogram")
#     ax.set_xlabel(x_axis)
#     ax.set_ylabel("Frequency")

# elif chart == "Box Plot":
#     ax.boxplot(data[y_axis])
#     ax.set_title("Box Plot")
#     ax.set_ylabel(y_axis)

# ax.set_xlabel(x_axis)
# ax.set_ylabel(y_axis)

# st.pyplot(fig)