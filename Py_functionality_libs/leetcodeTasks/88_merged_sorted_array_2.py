# 88. Merge Sorted Array
# version 2026-July-07 input: [1,2,3,0,0,0], 3, [2,5,6], 3 in progress
# decision 2 not accepted
nums1t = [1, 2, 3, 0, 0, 0]
mt = 3
nums2t = [2, 5, 6]
nt = 3


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # nums1 = list(nums1[:m:]).extend(nums2[:n:])
        # list(nums1).pop(1)
        # print(nums1)
        # nums1.extend(nums2[:n:])
        new_list = sorted(nums2[::-1])
        print(new_list)
        for x in range(m, m + n):
            print(x)
            nums1[x] = new_list[x - n]

        return sorted(nums1)


def main():
    c = Solution()
    print(f" result : {c.merge(nums1t, mt, nums2t, nt)}")
    assert c.merge(nums1t, mt, nums2t, nt) == [1, 2, 2, 3, 5, 6]


if __name__ == "__main__":
    main()
