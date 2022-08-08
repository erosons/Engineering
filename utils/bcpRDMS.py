# pip install bcp

# Import data:

import bcp

conn = bcp.Connection(host='HOST', driver='mssql',
                      username='USER', password='PASSWORD')
my_bcp = bcp.BCP(conn)
file = bcp.DataFile(file_path='path/to/file.csv', delimiter=',')
my_bcp.load(input_file=file, table='table_name')


# Export data:


conn = bcp.Connection(host='HOST', driver='mssql',
                      username='USER', password='PASSWORD')
my_bcp = bcp.BCP(conn)
file = bcp.DataFile(file_path='path/to/file.csv', delimiter=',')
my_bcp.dump(query='select * from sys.tables', output_file=file)
