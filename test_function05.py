import pandas as pd

# Sample data
data = {
    'Department': ['HR', 'IT', 'Finance', 'HR', 'IT'],
    'Gender': ['Female', 'Male', 'Female', 'Female', 'Male'],
    'Ethnicity': ['Asian', 'Caucasian', 'Hispanic', 'African American', 'Asian'],
    'Annual Salary': [75000, 65000, 80000, 72000, 50000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Filter the DataFrame
filtered_df = df[(df['Gender'] == 'Female') & (df['Annual Salary'] > 50000)]

# Select specific columns
result = filtered_df[['Department', 'Gender', 'Ethnicity', 'Annual Salary']]

# Display the result
print(result)