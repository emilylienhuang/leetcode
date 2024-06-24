class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        ans = ""
        min_len = min(len(x) for x in strs)
        record = True

        for i in range(min_len):
            target = strs[0][i]

            for word in strs:
                if word[i] != target:
                    record = False
                    break
            
            if record:
                ans += target
            else:
                break
        return ans

        



