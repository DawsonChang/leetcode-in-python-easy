class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        t1 = set(nums1)
        t2 = set(nums2)
        t = t1.intersection(t2)
        return list(t)
