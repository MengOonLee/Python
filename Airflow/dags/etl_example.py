from airflow.models import DAG
from datetime import datetime

etl_dag = DAG(
    dag_id='etl_example', 
    default_args={
        "owner": "meng",
        "email": "darklemon2000@gmail.com",
        "start_date": datetime(2020, 1, 20),
        "retries": 2
    }
)