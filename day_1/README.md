# Day 1: Missing Number (LeetCode #268)

## Problem Link
[Missing Number - LeetCode](https://leetcode.com/problems/missing-number/)

## My Approach
Initially tried an $O(n^2)$ solution using list lookups. Optimized to $O(n)$ using the **Sum Formula** (Gauss) to find the difference between the expected and actual sum.

## Complexity
- **Time:** $O(n)$
- **Space:** $O(1)$

# Day 1: Snapchat Sending vs. Opening Snaps (SQL)

## Problem Link
[DataLemur - Sending vs. Opening Snaps](https://datalemur.com/questions/time-spent-snaps)

## Problem Description
Calculate the percentage of time spent **sending** and **opening** snaps as a share of the total time spent on these two activities for each age group. 

**Key Requirements:**
- Ignore activities that are not 'send' or 'open'.
- Round the percentages to 2 decimal places.
- Output: `age_bucket`, `send_perc`, `open_perc`.

## Technical Approach
The solution uses a **Common Table Expression (CTE)** and **Conditional Aggregation** to handle the data transformation efficiently.

1.  **Filtering & Totaling:** Inside the CTE, I calculate the `total_time_spent` per user, specifically filtering for only 'send' and 'open' types. This ensures the denominator for our percentage calculation is accurate.
2.  **Joining:** Joined the activity data with the `age_breakdown` table to categorize users by their age buckets.
3.  **Aggregation:** Used `SUM(CASE WHEN...)` logic to pivot the activity types into separate columns while simultaneously calculating their percentage of the total.
4.  **Precision:** Multiplied by `100.0` to force floating-point math, preventing integer division errors common in SQL.

## Complexity Analysis
- **Time Complexity:** $O(n)$ where $n$ is the number of rows in the activities table. We scan the data to aggregate and then join.