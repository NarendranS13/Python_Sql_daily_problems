with ranked_measurements as (
  SELECT
  measurement_id,
  measurement_value,
  measurement_time,
  row_number() over (partition by date_trunc('day', measurement_time)
  order by measurement_time)as measurement_num
  from 
  measurements




)

SELECT
date_trunc('day', measurement_time)as measurement_day,
sum(measurement_value) FILTER (WHERE measurement_num % 2 != 0) AS odd_sum,
sum(measurement_value) FILTER (WHERE measurement_num % 2 = 0) AS even_sum
from ranked_measurements
GROUP BY measurement_day
ORDER BY measurement_day;