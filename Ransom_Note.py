class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if(len(ransomNote) > len(magazine)):            
            return False
               
        else:
            for l in ransomNote:
                if l in magazine:
                    
                    magazine = magazine.replace(l, '', 1)
                else:
                    return False
            return True
