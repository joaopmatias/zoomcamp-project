
# zoomcamp-project

Commands

```

docker-compose build

docker-compose up

export PREFECT_API_URL=http://127.0.0.1:4200/api

prefect work-queue set-concurrency-limit default 3

prefect deployment build my_flows.py:make_gcp_blocks -n make_gcp_blocks --path /apps

prefect deployment apply make_gcp_blocks-deployment.yaml 

prefect deployment run make-gcp-blocks/make_gcp_blocks

prefect deployment build my_flows.py:kaggle_to_gcs -n kaggle_to_gcs --path /apps

prefect deployment apply kaggle_to_gcs-deployment.yaml 

prefect deployment run kaggle-to-gcs/kaggle_to_gcs -p name=jl8771/2022-us-airlines-domestic-departure-data -p path=flights2022

$SPARK_HOME/bin/spark-submit --master spark://127.0.0.1:7077 --jars gcs-connector-hadoop3-2.2.12-shaded.jar,spark-3.3-bigquery-0.30.0.jar  spark/job.py

dbt init

dbt build

dbt run

```

profiles.yml

```
dbt_taxi:
  outputs:
    dev:
      dataset: zoomcamp_project_bq
      job_execution_timeout_seconds: 300
      job_retries: 1
      keyfile: /home/joaopmatias/.gc/taxi-rides-ny-373121-83cac15e98a3.json
      location: europe-southwest1
      method: service-account
      priority: interactive
      project: taxi-rides-ny-373121
      threads: 2
      type: bigquery
  target: dev
```
