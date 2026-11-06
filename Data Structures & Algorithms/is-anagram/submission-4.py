class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return len(s)==len(t) and Counter(s)==Counter(t)
        
        # sfreq = Counter(s)
        # tfreq = Counter(t)

        # if len(sfreq)!=len(tfreq):
        #     return False

        # for ch, fq in tfreq.items():
        #     if ch not in sfreq or fq != sfreq[ch]:
        #         return False

        # return True
        