# Day 3: Two Sum Problem (Python)
https://leetcode.com/problems/two-sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

# Day 3: Laptop vs Mobile: Viewership
https://datalemur.com/questions/laptop-mobile-viewership

Assume you're given the table on user viewership categorised by device type where the three types are laptop, tablet, and phone.

Write a query that calculates the total viewership for laptops and mobile devices where mobile is defined as the sum of tablet and phone viewership. Output the total viewership for laptops as laptop_reviews and the total viewership for mobile devices as mobile_views.

Effective 15 April 2023, the solution has been updated with a more concise and easy-to-understand approach.

viewership Table

Column Name	Type
user_id	integer
device_type	string ('laptop', 'tablet', 'phone')
view_time	timestamp

viewership Example Input

| user_id | device_type | view_time |
|---|---|---|
| 123 | tablet | 01/02/2022 00:00:00 |
| 125 | laptop | 01/07/2022 00:00:00 |
| 128 | laptop | 02/09/2022 00:00:00 |
| 129 | phone | 02/09/2022 00:00:00 |
| 145 | tablet | 02/24/2022 00:00:00 |

Example Output

| laptop_views | mobile_views |
|---|---|
| 2 | 3 |

Explanation
Based on the example input, there are a total of 2 laptop views and 3 mobile views.