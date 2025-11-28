import numpy as np
import pandas as pd
from sklearn.feature_selection import VarianceThreshold
from sklearn.preprocessing import StandardScaler

file_path = 'descriptors_filtered_54.csv'
data = pd.read_csv(file_path, delimiter=';')

# Start operations from the column named "MW"
start_column = 'MW'
start_index = data.columns.get_loc(start_column)
data_subset = data.iloc[:, start_index:]

# Replace 'na' with NaN and convert to numeric
data_subset = data_subset.replace('na', np.nan)
data_subset = data_subset.apply(pd.to_numeric, errors='coerce')

data_subset = data_subset.dropna(axis=1)

# Remove low variance features
selector = VarianceThreshold(threshold=0.05)
data_var = selector.fit_transform(data_subset)
selected_features = data_subset.columns[selector.get_support(indices=True)]
data_var_df = pd.DataFrame(data_var, columns=selected_features)

# Remove highly correlated features
corr_matrix = data_var_df.corr().abs()
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))

to_drop = [column for column in upper.columns if any(upper[column] > 0.95)]
data_corr = data_var_df.drop(columns=to_drop)

# Update selected features
selected_features = pd.DataFrame(data_corr.columns)
mic = pd.DataFrame(data, columns=['No.','MIC_SAU','MIC_CAL'])

imidazole_selected = mic.join(data_corr.copy())
