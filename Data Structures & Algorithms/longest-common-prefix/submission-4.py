class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        n = len(strs)
        i = 0

        while i<len(strs[0]):
            status = True
            pre = strs[0][i]
            for j in range(n):
                if j>=len(strs) or i>=len(strs[j]):
                    status = False
                    break
                if strs[j][i]!=pre:
                    status = False
                    break

            if not status:
                break
            
            i+=1
            
            prefix+=pre

        return prefix
