class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ''.join(filter(str.isalnum, s.lower()))
        p_end = len(s2) - 1
        p_start = 0

        return s2 == s2[::-1]

        while (p_start < p_end):
            if s2[p_start] != s2[p_end]:
                return False

            p_start+=1
            p_end -= 1
        return True
