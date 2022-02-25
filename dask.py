"""
Example from: https://examples.dask.org/dataframes/02-groupby.html
01.12.2021
"""


import dask

df = dask.datasets.timeseries()

# small dataset fits into memory, so can persist
df = df.persist()

df.groupby('name').x.mean().compute()

df.groupby('name').agg({'x': ['mean', 'std'], 'y': ['mean', 'count']}).compute().head()
