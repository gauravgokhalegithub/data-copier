import os
import pandas as pd

def get_json_reader(BASE_DIR, TABLE_NAME, chunksize=1000):
    file_name = os.listdir(f'{BASE_DIR}/{TABLE_NAME}')[0]
    file_path = f'{BASE_DIR}/{TABLE_NAME}/{file_name}'
    json_reader = pd.read_json(file_path, lines=True, chunksize=chunksize)
    return json_reader

if __name__ == '__main__':
    base_dir = os.environ.get('BASE_DIR')
    table_name = os.environ.get('TABLE_NAME')
    json_reader = get_json_reader(base_dir, table_name)
    for idx, df in enumerate(json_reader):
        print(f'Number of record in chinks with index {idx} is {df.shape[0]}')