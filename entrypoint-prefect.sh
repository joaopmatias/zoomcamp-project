#!/bin/bash

prefect server start > server.log &

prefect agent start --work-queue "default" > agent.log &

#prefect deployments build my_flows.py:make_gcp_blocks -n make_gcp_blocks && \
#  prefect deployments apply make_gcp_blocks-deployment.yaml && \
#  prefect deployments build my_flows.py:kaggle_to_gcs -n kaggle_to_gcs && \
#  prefect deployments apply kaggle_to_gcs-deployment.yaml && \
#  prefect work-queue set-concurrency-limit default 3

exec tail -f server.log agent.log
