class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = []
        for i in range (len(nums1)):
            for j in range (len(nums2)):
                if (nums1[i]==nums2[j]):
                    a.append(nums1[i])
                    del nums2[j]
                    break
        return a                       
        
