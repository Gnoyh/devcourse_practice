from airflow import DAG
from airflow.models import Variable
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.decorators import task

from datetime import datetime
from datetime import timedelta

import requests
import logging
import json

def get_Redshift_connection(autocommit=True):
    hook = PostgresHook(postgres_conn_id='redshift_dev_db')
    conn = hook.get_conn()
    conn.autocommit = autocommit
    return conn.cursor()


@task
def extract(url):
    logging.info(datetime.utcnow())
    f = requests.get(url)
    return f.text


@task
def transform(text):
    lines = json.loads(text)
    records = []
    for l in lines:
        country = l['name']['official']
        population = l['population']
        area = l['area']

        records.append([country, population, area])
    return records


@task
def load(schema, table, records):
    logging.info("load started")    
    cur = get_Redshift_connection()   

    # BEGIN과 END를 사용해서 SQL 결과를 트랜잭션으로 만들어주는 것이 좋음
    try:
        cur.execute("BEGIN;")
        cur.execute(f"DELETE FROM {schema}.rest_countries;") 
        # DELETE FROM을 먼저 수행 -> FULL REFRESH을 하는 형태
        for r in records:
            country = r[0]
            population = r[1]
            area = r[2]
            print(name, "-", gender, "-", area)
            sql = f"INSERT INTO {schema}.rest_countries VALUES ('{country}', '{population}', '{area}')"
            cur.execute(sql)
        cur.execute("COMMIT;")   # cur.execute("END;") 
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        cur.execute("ROLLBACK;")   
    logging.info("load done")


with DAG(
    dag_id='rest_countries',
    start_date=datetime(2024, 5, 16),  # 날짜가 미래인 경우 실행이 안됨
    schedule='30 6 * * 6',  # 적당히 조절
    max_active_runs=1,
    catchup=False,
    default_args={
        'retries': 1,
        'retry_delay': timedelta(minutes=3),
        # 'on_failure_callback': slack.on_failure_callback,
    }
) as dag:

    url = Variable.get("countries_url")
    schema = 'fourksenhs'   ## 자신의 스키마로 변경
    table = 'rest_countries'

    lines = transform(extract(url))
    load(schema, table, lines)
