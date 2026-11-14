class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        for i in range(len(strs[0])):
            char = strs[0][i]
            print(char)
            for s in strs:
                print(i,len(s))
                if i>=len(s) or s[i]!=char:
                    print("inside",i,len(s))
                    print('returning', strs[0][:i])
                    return strs[0][:i]

        return strs[0]