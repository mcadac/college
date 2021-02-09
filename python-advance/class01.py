import pandas as pd
from sklearn import datasets

# Read a json file
json_file = pd.read_json('milo.json')
print(json_file)

# Creating 100 sampkes with 3 features
features, target, coefficients = datasets.make_regression(n_samples=100, n_features=3, n_informative=3, n_targets=1,
                                                          noise=0.0, coef=True, random_state=1)
print('feature matrix \n', features[:3])
print('target vector \n', target[:3])
