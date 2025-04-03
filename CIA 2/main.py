# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# import seaborn as sns

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
@st.cache_data
def load_data():
    try:
        # Use raw string for Windows path or relative path if file is in same directory
        data = pd.read_excel('big_kitten_dataset.xlsx')  # or use r'full_path_here'
        return data
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None

df = load_data()

if df is not None:
    st.title("Kitten Data Analysis")
    
    # 1. Breed with highest average energy level
    st.header("1. Breed Statistics")
    breed_energy = df.groupby('Breed')['Energy_Level'].mean()
    highest_energy_breed = breed_energy.idxmax()
    st.success(f"Breed with highest average energy level: {highest_energy_breed} ({breed_energy.max():.1f})")
    
    fig1, ax1 = plt.subplots()
    breed_energy.sort_values().plot(kind='barh', ax=ax1, color='skyblue')
    ax1.set_title('Average Energy Level by Breed')
    ax1.set_xlabel('Energy Level')
    st.pyplot(fig1)
    
    # 2. Most favorite toy
    st.header("2. Toy Preferences")
    toy_counts = df['Favorite_Toy'].value_counts()
    most_popular_toy = toy_counts.idxmax()
    st.success(f"Most favorite toy: {most_popular_toy} ({toy_counts.max()} kittens)")
    
    fig2, ax2 = plt.subplots()
    ax2.pie(toy_counts, labels=toy_counts.index, autopct='%1.1f%%')
    ax2.set_title('Favorite Toy Distribution')
    st.pyplot(fig2)
    
    # 3. Age with least and most weight
    st.header("3. Age vs Weight Analysis")
    age_weight = df.groupby('Age_Months')['Weight_kg'].mean()
    min_weight_age = age_weight.idxmin()
    max_weight_age = age_weight.idxmax()
    
    st.success(f"Age with least average weight: {min_weight_age} months ({age_weight.min():.1f} kg)")
    st.success(f"Age with most average weight: {max_weight_age} months ({age_weight.max():.1f} kg)")
    
    # Visualization
    fig3, ax3 = plt.subplots()
    age_weight.plot(kind='line', marker='o', ax=ax3)
    ax3.set_title('Average Weight by Age')
    ax3.set_xlabel('Age (months)')
    ax3.set_ylabel('Weight (kg)')
    ax3.grid(True)
    st.pyplot(fig3)
    
    # Show raw data
    if st.checkbox("Show raw data"):
        st.subheader("Raw Data")
        st.dataframe(df)
else:
    st.error("Failed to load data. Please check the file path.")


