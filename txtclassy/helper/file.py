import pandas as pd

df = pd.read_csv('.data/data_test_csv/train.csv', delimiter=', ')
train_sets = df.to_dict('records')
print(dicts)