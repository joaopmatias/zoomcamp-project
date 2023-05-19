{{ config(materialized='view') }}

select ORIGIN, DEST, DEP_TIME, CRS_DEP_TIME, 
{{ get_distance_type_description('DISTANCE') }} as DIST_DESCRIPTION
from {{ source('staging','CompleteData') }}
