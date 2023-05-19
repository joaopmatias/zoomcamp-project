 {#
    This macro returns the description of the DISTANCE 
#}

{% macro get_distance_type_description(DISTANCE) -%}

    case when cast( {{ DISTANCE }} as int ) between 0 and 1000 then 'less than 1000'
    when cast( {{ DISTANCE  }} as int ) between 1001 and 2000 then 'greater than 1000'
    else 'greater than 2000'
    end

{%- endmacro %}