class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # n = len(strs)
        # common = ""
        # for i in range(n-1):
        #     status = True
        #     for j in range(n):
        #         if strs[j][i]!=strs[j][i+1]:
        #             status = False
        #     if status:
        #         common+=strs[]

        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]

                if not prefix:
                    return ""

        return prefix