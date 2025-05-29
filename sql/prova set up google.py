print (2+200)

from google.cloud import bigquery

client = bigquery.Client(project="sql-sandbox-435415")

# Esegui la query di test
QUERY = (
    'SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` '
    'WHERE state = "TX" '
    'LIMIT 100')

query_job = client.query(QUERY)

for row in query_job:
    print(row.name)



# da questo dataset 'bigquery-public-data.ml_datasets.iris' fai la lista delle species uniche

QUERY = (
    'SELECT DISTINCT species FROM `bigquery-public-data.ml_datasets.iris` '
    'LIMIT 100')

query_job = client.query(QUERY)

for row in query_job:
    print(row.species)


# for that db print the first 5 with biggest petal_length

QUERY = (
    'SELECT * FROM `bigquery-public-data.ml_datasets.iris` '
    'ORDER BY petal_length DESC '
    'LIMIT 5')

query_job = client.query(QUERY)

for row in query_job:
    print(row)



from google.cloud import bigquery
import pandas as pd

# Inizializza il client BigQuery
client = bigquery.Client()

# La tua query SQL
query = """
    SELECT name, gender, count
    FROM `bigquery-public-data.usa_names.usa_1910_2013`
    WHERE state = 'TX'
    ORDER BY count DESC
    LIMIT 10
"""

# Esegui la query e ottieni un DataFrame
df = client.query(query).to_dataframe()

# Mostra i risultati in formato tabellare
print(df)

from google.cloud import bigquery
import pandas as pd

# Inizializza il client con il progetto
client = bigquery.Client(project="sql-sandbox-435415")

# Query corretta (usa 'number' al posto di 'count')
query = """
    SELECT name, gender, number
    FROM `bigquery-public-data.usa_names.usa_1910_2013`
    WHERE state = 'TX'
    ORDER BY number DESC
    LIMIT 10
"""

# Esegui la query e ottieni un DataFrame
df = client.query(query).to_dataframe()

# Mostra il risultato in formato tabellare
print(df)





--------------
from google.cloud import bigquery
import pandas as pd

# Inizializza il client specificando il tuo progetto
client = bigquery.Client(project="sql-sandbox-435415")

# Query corretta (usa 'number' e non 'count')
query = """
    SELECT name, gender, number
    FROM `bigquery-public-data.usa_names.usa_1910_2013`
    WHERE state = 'TX'
    ORDER BY number DESC
    LIMIT 10
"""

# Esegui la query
df = client.query(query).to_dataframe()

# Visualizza in formato tabellare
print(df)
