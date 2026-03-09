# Day 4: Happy Number (Python)
https://leetcode.com/problems/happy-number

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

### Example 1:

Input: n = 19
Output: true
Explanation:

12 + 92 = 82

82 + 22 = 68

62 + 82 = 100

12 + 02 + 02 = 1

### Example 2:

Input: n = 2

Output: false
 

### Constraints:

1 <= n <= 2^31 - 1


# Day 4 Duplicate Job Listings (DataLemur)

Assume you're given a table containing job postings from various companies on the LinkedIn platform. Write a query to retrieve the count of companies that have posted duplicate job listings.

### Definition:

Duplicate job listings are defined as two job listings within the same company that share identical titles and descriptions.

job_listings Table:

| Column Name | Type     |
|-------------|----------|
| job_id      | integer  |
| company_id  | integer  |
| title       | string   |
| description | string   |

job_listings 

Example Input:

| job_id | company_id | title | description |
|--------|------------|-------|-------------|
| 248 | 827 | Business Analyst | Business analyst evaluates past and current business data with the primary goal of improving decision-making processes within organizations. |
| 149 | 845 | Business Analyst | Business analyst evaluates past and current business data with the primary goal of improving decision-making processes within organizations. |
| 945 | 345 | Data Analyst | Data analyst reviews data to identify key insights into a business's customers and ways the data can be used to solve problems. |
| 164 | 345 | Data Analyst | Data analyst reviews data to identify key insights into a business's customers and ways the data can be used to solve problems. |
| 172 | 244 | Data Engineer | Data engineer works in a variety of settings to build systems that collect, manage, and convert raw data into usable information for data scientists and business analysts to interpret. |

Example Output:

duplicate_companies
1

### Explanation:

There is one company ID 345 that posted duplicate job listings. The duplicate listings, IDs 945 and 164 have identical titles and descriptions.