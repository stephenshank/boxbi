import sqlite3
import argparse


parser = argparse.ArgumentParser(description="Export data from database.")
parser.add_argument('--fields', dest='fields', help='Relevant fields to grab. Choices: all, splice.', default='all')
parser.add_argument('--after', dest='after', help='Select after a given date (format YYYY-MM-DD).', default=None)
parser.add_argument('--db', dest='db', help='Location of the database file.', default=None)

args = parser.parse_args()

if args.fields=='all':
    columns_string = '*'
elif args.fields=='splice':
    columns_string = 'datetime,MachineSpeed,DBSplice,CEFMSplice,CEFLSplice,BFMSplice,BFLSplice'

if args.after:
    datetime_string = args.after + ' 11:00:00'
    where_string = ' where datetime >= "' + datetime_string + '"'
else:
    where_string = ''

if args.db:
    db_filename = args.db
else:
    db_filename = '/Users/stephenshank/Documents/BoxBI/backup.sqlite3'

connection = sqlite3.connect(db_filename)
cursor = connection.cursor()
query_string = 'select %s from api_corrdata%s;'
query_params = (columns_string, where_string)
query = query_string % query_params
data = cursor.execute(query)
columns_string = ','.join(zip(*cursor.description)[0])
print columns_string
for row in data:
    print ','.join([str(i) for i in row])

