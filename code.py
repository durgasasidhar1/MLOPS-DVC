import pandas as pd
import os

data = {
    'Name':['sasidhar','ratan','durga'],
    'Age':[21,87,20],
    'City': ['Amalapuram','Mumbai','Vijayawada']
}

df = pd.DataFrame(data, columns=data.keys())

data_dir = 'MLOPS-DVC\data'

os.makedirs(data_dir, exist_ok=True)

file_paths = os.path.join(data_dir, 'sample_data.csv')

df.to_csv(file_paths)

print(f"CSV file is saved to {file_paths}")