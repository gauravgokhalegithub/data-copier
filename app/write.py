def load_db_table(df, table_name, conn, key):
    min = df[key].min()
    max = df[key].max()
    df.to_sql(table_name, conn, if_exists='append', index=False)
    print(f'Loaded data for {table_name} with in the range of {min} and {max}')



if __name__ == '__main__':
    import os
    import pandas as pd
    data = [
        {'user_id': 1, 'user_first_name': 'Scott', 'user_last_name': 'Tiger'},
        {'user_id': 2, 'user_first_name': 'Donald', 'user_last_name': 'Duck'}
    ]
    df = pd.DataFrame(data)
    configs = dict(os.environ.items())
    conn = f'postgresql://{configs["DB_USER"]}:{configs["DB_PASS"]}@{configs["DB_HOST"]}:{configs["DB_PORT"]}/{configs["DB_NAME"]}'
    load_db_table(df, 'users',conn, 'user_id')