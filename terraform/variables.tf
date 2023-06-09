locals {
  data_lake_bucket = "zoomcamp_project_bucket"
}

variable "project" {
  description = "Your GCP Project ID"
  default = "taxi-rides-ny-373121"
}

variable "region" {
  description = "Region for GCP resources. Choose as per your location: https://cloud.google.com/about/locations"
  default = "europe-southwest1"
  type = string
}

variable "storage_class" {
  description = "Storage class type for your bucket. Check official docs for more info."
  default = "STANDARD"
}

variable "BQ_DATASET" {
  description = "BigQuery Dataset that raw data (from GCS) will be written to"
  type = string
  default = "zoomcamp_project_bq"
}
