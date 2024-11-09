


import pandas as pd
from sqlalchemy import create_engine
pd.__version__




engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')


df_iter = pd.read_csv('yellow_tripdata_2021-01.csv', iterator=True, chunksize=100000)

from time import time
while True: 
    t_start = time()

    df = next(df_iter)

    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    
    df.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')

    t_end = time()

    print('inserted another chunk, took %.3f second' % (t_end - t_start))



df_zones = pd.read_csv('taxi+_zone_lookup.csv')
df_zones.head()
df_zones.to_sql(name='zones', con=engine, if_exists='replace')

