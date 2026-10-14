class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        smap={}
        for letter in s:
            if letter not in smap:
                smap[letter]=1
            else:
                smap[letter]=smap[letter]+1
        
        tmap={}
        for letter in t:
            if letter not in tmap:
                tmap[letter]=1
            else: 
                tmap[letter]+=1
        if smap!=tmap:
            return False
        return True
        