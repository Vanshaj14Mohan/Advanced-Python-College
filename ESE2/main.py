import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache
def load_data():
    data = pd.read_csv('E:\Advanced Python\ESE2\Car Sales.xlsx - car_data - Car Sales.xlsx - car_data.csv')
    return data

data = load_data()

# Sidebar for user input
st.sidebar.header('Filters and Graph Selection')

# Graph selection
graph_type = st.sidebar.selectbox(
    'Select Graph Type',
    ["Bar Chart", "Pie Chart", "Line Chart", "Box Plot", "Scatter Plot"]
)

# Filter by gender (optional)
selected_gender = st.sidebar.selectbox(
    'Select Gender',
    ['All'] + list(data['Gender'].unique())
)

# Filter by dealer region (optional)
selected_region = st.sidebar.selectbox(
    'Select Dealer Region',
    ['All'] + list(data['Dealer_Region'].unique())
)

# Apply filters
if selected_gender != 'All':
    data = data[data['Gender'] == selected_gender]

if selected_region != 'All':
    data = data[data['Dealer_Region'] == selected_region]

st.write('### Car Sales Data')
st.write(data)

st.write(f'### {graph_type}')

#1-> Bar Chart
if graph_type == 'Bar Chart':
    company_sales = data['Company'].value_counts()
    st.bar_chart(company_sales)

#2-> Pie Chart
elif graph_type == 'Pie Chart':
    gender_sales = data['Gender'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(gender_sales, labels=gender_sales.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.
    st.pyplot(fig)

#3-> Line Chart
elif graph_type == 'Line Chart':
    data['Date'] = pd.to_datetime(data['Date'])  
    sales_over_time = data.groupby('Date').size()  
    st.line_chart(sales_over_time)

#4-> Box Plot
elif graph_type == 'Box Plot':
    fig, ax = plt.subplots(figsize=(10, 6))
    data.boxplot(column='Price ($)', by='Company', ax=ax)
    plt.title('Distribution of Car Prices by Company')
    plt.suptitle('')  # Remove default title
    plt.xlabel('Company')
    plt.ylabel('Price')
    plt.xticks(rotation=90)
    st.pyplot(fig)

#5-> Scatter Plot
elif graph_type == 'Scatter Plot':
    fig, ax = plt.subplots(figsize=(12, 6))
    
    #Creating Scatter Plot
    for company in data['Company'].unique():
        company_data = data[data['Company'] == company]
        ax.scatter(company_data['Company'], company_data['Price ($)'], label=company, alpha=0.6)
    
    plt.title('Car Prices by Company')
    plt.xlabel('Company')
    plt.ylabel('Price ($)')
    plt.xticks(rotation=90)
    
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    
    plt.tight_layout()
    st.pyplot(fig)



