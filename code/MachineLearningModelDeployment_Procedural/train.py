# ==== EXAMPLE OF PREPROC FUNCTIONS SCRIPT ========

import pandas as pd
import numpy as np

# to divide train and test set
from sklearn.model_selection import train_test_split

# feature scaling
from sklearn.preprocessing import StandardScaler

# to build the models
from sklearn.linear_model import LinearRegression, Lasso

# to evaluate the models
from sklearn.metrics import mean_squared_error

#=========== training pipeline ======
df = load(yaml_path_to_file)
x_train, x_test, y_train, y_test = divide_train_test(df, yaml_target_name)

# remove NA numerical
train[var1] = remove_numerical_na(x_train, var1, mean_val1_in_yaml)
train[var2] = remove_numerical_na(x_train, var2, mean_val2_in_yaml)

train[var3] = remove_categorical_na(x_train[var3])
train[var4] = remove_categorical_na(x_train[var4])

# Outliers
train[var5] = cap_outliers(x_train, var5, cap_value_in_yaml, bigger_than=False)
train[var6] = cap_outliers(x_train, var6, cap_value_in_yaml, bigger_than=False)

# Transformed skewed variables
train[var7] = transform_skewed_variables(x_train, var7)

#Remove Rare Labels
train[var8] = remove_rare_labels(x_train, var8, frequent_labels_in_yaml)

#Normalization
scaler = train_scaler(x_train, output_path_in_yaml)

#Train Model
lin_model = train_model(x_train, y_train, feature_list_in_yaml, scaler, output_path_in_yaml)