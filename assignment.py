# Assuming you have fitted a linear regression model named 'model'
coefficients = model.coef_
feature_names = df.columns[:-1]  # Exclude the target variable 'cnt'
# Create a DataFrame to pair features with their coefficients
coef_df = pd.DataFrame({'Feature': feature_names, 'Coefficient': coefficients})

# Sort the DataFrame by absolute coefficient values in descending order
