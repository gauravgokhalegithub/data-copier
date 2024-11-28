import os
import sys
from read import get_json_reader
from write import load_db_table

def process_table(base_dir, conn, table_name):
    json_reader = get_json_reader(base_dir, table_name)
    for df in json_reader:
        load_db_table(df, table_name, conn, df.columns[0])



def main():
    base_dir = os.environ.get('BASE_DIR')
    table_names = sys.argv[1].split(',')
    config = dict(os.environ.items())
    conn = f'postgresql://{config["DB_USER"]}:{config["DB_PASS"]}@{config["DB_HOST"]}:{config["DB_PORT"]}/{config["DB_NAME"]}'
    for table_name in table_names:
        process_table(base_dir, conn, table_name)



if __name__ == '__main__':
    main()

# config = dict(os.environ.items())
# conn = f'postgresql://{config["DB_USER"]}:{config["DB_PASS"]}@{config["DB_HOST"]}:{config["DB_PORT"]}/{config["DB_NAME"]}'
# print(conn)