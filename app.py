import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Simple EDA Generator') # give warning, run python3 -m streamlit run app.py

uploaded_file = st.file_uploader("Upload a file for EDA")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("File uploaded successfully!")

    with st.expander("Dataset Information"):
        checkbox1 = st.checkbox("Show Data Frame")

        if checkbox1:
            st.write(df)
        
        checkbox2 = st.checkbox("Show Data Statistics")
        if checkbox2:
            num_rows = df.shape[0]
            num_cols = df.shape[1]

            # Count categorical, numerical, and boolean variables
            categorical_vars = df.select_dtypes(include='object').columns.tolist()
            numerical_vars = df.select_dtypes(include=['int', 'float']).columns.tolist()
            bool_vars = df.select_dtypes(include='bool').columns.tolist()

            # Display dataset relevant statistics
            st.write(str(num_rows), " rows and ", str(num_cols), " columns")
            st.write(str(len(categorical_vars)), " categorical variables")
            st.write(str(len(numerical_vars)), " numerical variables")
            st.write(str(len(bool_vars)), " boolean variables")

    with st.expander("Select a Numerical Variable to Perform EDA"):
        # select column
        selected_column = st.selectbox("Select a column", df.columns)

        if df[selected_column].dtype in ['int', 'float']:
            # Display five-number summary
            summary_stats = df[selected_column].describe().loc[['min', '25%', '50%', '75%', 'max']]
            st.write("Five-Number Summary:")
            st.write(summary_stats)

            # Create distribution plot
            fig, ax = plt.subplots(figsize=(10, 4))
            sns.distplot(a=df[selected_column], hist=True, kde=False, rug=False)
            ax.set_title(f"Distribution of {selected_column}")
            ax.set_xlabel(selected_column)
            ax.set_ylabel("Frequency")
            st.pyplot(fig)
        if df[selected_column].dtype == 'object':
            # Calculate proportions
            proportions = df[selected_column].value_counts(normalize=True)

            # Display proportions in a table
            st.write("Category Proportions:")
            st.dataframe(proportions)

            # Create customized barplot
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.countplot(data=df, x=selected_column, ax=ax, palette='pastel')
            ax.set_title(f"Barplot of {selected_column}")
            ax.set_xlabel(selected_column)
            ax.set_ylabel("Count")
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
            st.pyplot(fig)
        else:
            st.write("Warning: Selected Column Not Valid")
