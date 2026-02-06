SELECT 
count(DISTINCT CASE WHEN device_type = 'laptop' then user_id END)as laptop_views,
count(DISTINCT CASE WHEN device_type in ('phone','tablet') then user_id END)as mobile_views
from viewership;