# 🟩 Day 2 — Valid Perfect Square (LeetCode #367)

## 🔗 Problem Link:
https://leetcode.com/problems/valid-perfect-square/

## 📘 Problem Description

Given a positive integer num, return true if num is a perfect square, otherwise return false.

A perfect square is an integer that is the square of another integer.
Example: 12 × 12 = 144

## ⚠️ Constraints

Do not use built-in functions like sqrt()

Solve in better than O(n) time complexity

## 💡 Technical Approach — Binary Search

The numbers from 1 to num form a naturally sorted range.
We can apply Binary Search to efficiently find whether a number exists whose square equals num.

Binary Search reduces the search space by half on every step.

## 🧠 Logic Steps

Base Case

If num < 2, return True
(Covers edge cases: 0 and 1)

Initialize Pointers

left = 2

right = num // 2
(Because for any number > 4, its square root will be less than num/2)

Binary Search Loop

While left <= right:

Calculate mid

Compute guess = mid * mid

If guess == num → return True

If guess > num → move right to mid - 1

If guess < num → move left to mid + 1

Final Result

If loop ends, num is not a perfect square → return False

## ⏱️ Complexity Analysis
Complexity	Value	Reason
Time	O(log n)	Binary search halves the range each step
Space	O(1)	Only pointer variables used
🧪 Example
Input	Output
16	True
14	False


## 🧩 Key Takeaway

This problem is a classic example of applying Binary Search on answer space instead of searching a data structure.


# 🟩 Day 3 — Unfinished Parts (Tesla SQL Interview Question)

## 🔗 Problem Link:
https://datalemur.com/questions/unfinished-parts

## 📘 Problem Description

Tesla is investigating production bottlenecks and needs help extracting relevant data.

The parts_assembly table contains all parts currently in production, each at different stages of the assembly process.

## 🎯 Goal

Write a SQL query to determine which parts have started the assembly process but are not yet finished.

## 🧾 Assumptions

An unfinished part is defined as one that does not have a finish_date

The parts_assembly table already contains all parts currently in production

## 💡 Technical Approach — Filtering for NULL Values

This problem tests a fundamental SQL concept: handling missing data.

In databases, unfinished tasks or open processes are commonly represented using NULL values in a completion column.

## 🧠 Logic Steps

Identify the Table

Source data is in the parts_assembly table

Filter Condition

We need rows where the part has started but not finished

This is identified by checking the finish_date column

Use IS NULL Operator

In SQL, we cannot use = NULL

We must use IS NULL to correctly filter missing values

Select Relevant Columns

The problem asks for:

part

assembly_step

This helps identify exactly where the bottleneck exists