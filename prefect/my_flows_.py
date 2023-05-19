import subprocess
from pathlib import Path

from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
from prefect_gcp.credentials import GcpCredentials
from random import randint


@flow(log_prints=True)
def make_gcp_blocks(
    service_account_file="/mnt/.gc/taxi-rides-ny-373121-83cac15e98a3.json",
    bucket="zoomcamp_project_bucket",
):
    gcp_credentials = make_gcp_credentials(service_account_file)
    _ = make_bucket(bucket, gcp_credentials)


@task(log_prints=True)
def make_gcp_credentials(service_account_file):
    block_name = "zoom-gcp-creds"
    block = GcpCredentials(
        service_account_file=service_account_file,
    )
    block.save(name=block_name)
    return block


@task(log_prints=True)
def make_bucket(bucket, gcp_credentials):
    block_name = "zoom-gcs"
    block = GcsBucket(
        bucket=bucket,
        gcp_credentials=gcp_credentials,
        bucket_folder=".",
    )
    block.save(block_name)
    return block


@flow(log_prints=True)
def kaggle_to_gcs(name: str, path: str = "."):
    """Upload files to GCS."""
    subprocess.run([
        "kaggle",
        "datasets",
        "download",
        "--unzip",
        "--path", path,
        name,
    ])

    gcs_block = GcsBucket.load("zoom-gcs")
    for p in Path(path).glob("*.csv"):
        q = p.relative_to(".").as_posix()
        gcs_block.upload_from_path(from_path=q, to_path=q)
    return 
