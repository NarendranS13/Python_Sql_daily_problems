class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        no_of_blanks = []

        for i in range(len(sentences)):
            counter = 0
            words = sentences[i].lower().strip()
            for word in words:
                if not word.isalnum():
                    counter += 1

                no_of_blanks.append(counter)

        no_of_blanks.sort(reverse = True)
        output = no_of_blanks[0] + 1
        return output
    
sol = Solution()
print(sol.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))