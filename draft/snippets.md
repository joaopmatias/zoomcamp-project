
```
docker-compose run --rm --build python --file_name=green_tripdata_2019-01.csv --if_exists=replace --table_name=green_taxi_data 
```

```
terraform version
```

```
gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS
```

```
find $PWD -maxdepth 1 
```

```
terraform init
terraform plan
terraform apply
```

```
export TF_LOG=TRACE
```

```
terraform plan -out /home/joaopmatias/data-engineering-zoomcamp/plan2.tf.txt
```

```
terraform destroy
```

```
pgcli -U root -W  -d ny_taxi -h localhost -p 5432
```

```
prefect orion start
prefect agent start
```

```
git add submodule https://github.com/discdiver/prefect-zoomcamp
```


```
prefect deployment etl_gcs_to_bq.py:etl_gcs_to_bq -n FirstDeploy
prefect deployment build etl_gcs_to_bq.py:etl_gcs_to_bq -n FirstDeploy
prefect deployment build etl_gcs_to_bq.py:etl_gcs_to_bq
prefect agent start --work-queue "default"
```

```
prefect deployment etl_gcs_to_bq-deployment.yaml 
prefect deployment apply  etl_gcs_to_bq-deployment.yaml 
perfect deployment build etl_web_to_gcs.py -n ParquetToGCS
prefect deployment build etl_web_to_gcs.py -n ParquetToGCS
```

```
prefect deployment build etl_web_to_gcs.py:etl_web_to_gcs
prefect deployment build etl_web_to_gcs.py:etl_web_to_gcs -n wem_to_gcs
prefect deployment build etl_web_to_gcs.py:etl_web_to_gcs -n web_to_gcs
prefect deployment build etl_gcs_to_bq.py:etl_gcs_to_bq -n gcs_to_bq
prefect deployment apply etl_gcs_to_bq-deployment.yaml 
prefect deployment apply etl_web_to_gcs-deployment.yaml 
prefect deployment run web_to_gcs
prefect deployment run web_to_gcs/web_to_gcs
prefect deployment run web_to_gcs/web_to_gcs --help
prefect deployment run web_to_gcs/web_to_gcs -p color=green -p month=1 -p year=2020
prefect deployment run web_to_gcs/web_to_gcs -p color=yellow -p month=2 -p year=2019
prefect deployment run web_to_gcs/web_to_gcs -p color=yellow -p month=3 -p year=2019
```

```
curl -s "https://get.sdkman.io" | bash 
source "/home/joaopmatias/.sdkman/bin/sdkman-init.sh" 
sdk
sdk list java
sdk install java 11.0.18-tem
sdk list spark
sdk install spark
sdk install hadoop
sdk install scala
```

```
dbt init
```

```
dbt debug
dbt build 
dbt run
```

```
GCP_PROJECT_ID: '<your_gcp_project_id>'
GCP_GCS_BUCKET: '<your_bucket_id>'
```

```
GOOGLE_APPLICATION_CREDENTIALS: /.google/credentials/google_credentials.json
AIRFLOW_CONN_GOOGLE_CLOUD_DEFAULT: 'google-cloud-platform://?extra__google_cloud_platform__key_path=/.google/credentials/google_credentials.json'
```

```
prefect orion start
prefect agent start  --work-queue "default"
prefect work-queue set-concurrency-limit default 3
```

```
prefect deployment run web_to_gcs/web_to_gcs -p color=fhv -p month=$i -p year=2019
```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```
