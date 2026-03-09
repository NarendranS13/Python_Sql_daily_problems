select count(distinct company_id)as duplicate_companies from 
(
SELECT 
*,
row_number() over (partition by company_id,title,description order by job_id)as row_rnk
FROM job_listings as jd
)as x
where row_rnk > 1