# 2114. Maximum Number of Words Found in Sentences
https://leetcode.com/problems/maximum-number-of-words-found-in-sentences

A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

You are given an array of strings sentences, where each sentences[i] represents a single sentence.

Return the maximum number of words that appear in a single sentence.

 

Example 1:

Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
Output: 6
Explanation: 
- The first sentence, "alice and bob love leetcode", has 5 words in total.
- The second sentence, "i think so too", has 4 words in total.
- The third sentence, "this is great thanks very much", has 6 words in total.
Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.
Example 2:

Input: sentences = ["please wait", "continue to fight", "continue to win"]
Output: 3
Explanation: It is possible that multiple sentences contain the same number of words. 
In this example, the second and third sentences (underlined) have the same number of words.
 

**Constraints:**

- 1 <= sentences.length <= 100
- 1 <= sentences[i].length <= 100
- sentences[i] consists only of lowercase English letters and ' ' only.
- sentences[i] does not have leading or trailing spaces.
- All the words in sentences[i] are separated by a single space.


# Odd and Even Measurements (DataLemur)

Assume you're given a table with measurement values obtained from a Google sensor over multiple days with measurements taken multiple times within each day.

Write a query to calculate the sum of odd-numbered and even-numbered measurements separately for a particular day and display the results in two different columns. Refer to the Example Output below for the desired format.

Definition:

Within a day, measurements taken at 1st, 3rd, and 5th times are considered odd-numbered measurements, and measurements taken at 2nd, 4th, and 6th times are considered even-numbered measurements.
Effective April 15th, 2023, the question and solution for this question have been revised.

measurements Table:

| Column Name      | Type     |
|------------------|----------|
| measurement_id   | integer  |
| measurement_value| decimal  |
| measurement_time | datetime |

measurements Example Input:

| measurement_id | measurement_value | measurement_time       |
|----------------|-------------------|------------------------|
| 131233         | 1109.51           | 07/10/2022 09:00:00    |
| 135211         | 1662.74           | 07/10/2022 11:00:00    |
| 523542         | 1246.24           | 07/10/2022 13:15:00    |
| 143562         | 1124.50           | 07/11/2022 15:00:00    |
| 346462         | 1234.14           | 07/11/2022 16:45:00    |

Example Output:

| measurement_day       | odd_sum | even_sum |
|-----------------------|---------|----------|
| 07/10/2022 00:00:00   | 2355.75 | 1662.74  |
| 07/11/2022 00:00:00   | 1124.50 | 1234.14  |


Explanation
Based on the results,

On 07/10/2022, the sum of the odd-numbered measurements is 2355.75, while the sum of the even-numbered measurements is 1662.74.
On 07/11/2022, there are only two measurements available. The sum of the odd-numbered measurements is 1124.50, and the sum of the even-numbered measurements is 1234.14.