class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        r=26*[0]
        m=26*[0]
        
        for i in range(len(s)):
            r[ord(s[i])-ord('a')]+=1
            
        for i in range(len(t)):       
            m[ord(t[i])-ord('a')]+=1
            
        for i in range(0,26):
            if r[i]!=m[i]:
                return False
        return True
