class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)

            current = n
            square_sum = 0
            while current > 0:
                digit = current % 10
                square_sum += digit * digit
                current = current // 10
            
            n = square_sum
        else:
            return True
        
sol = Solution()
print(sol.isHappy(19))