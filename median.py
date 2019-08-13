class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        l1,l2 = len(nums1),len(nums2)

        if l1>l2:
            nums2,nums1,l1,l2 = nums1,nums2,l2,l1

        i_min,i_max = 0,l1
        half_len = (l1+l2+1) // 2

        while i_min<=i_max:
            i = (i_min+i_max) // 2
            j = half_len - i
            if (i > 0  and nums1[i-1] > nums2[j]):
                i_max = i - 1
            elif (i < l1 and nums2[j-1] > nums1[i]):
                i_min = i + 1
            else:
                if i==0:
                    left_max = nums2[j-1]
                elif j==0:
                    left_max = nums1[i-1]
                else:
                    left_max = max(nums1[i-1],nums2[j-1])
                
                if (l1+l2)%2==1:
                    return left_max

                if i==l1:
                    right_min = nums2[j]
                elif j==l2:
                    right_min = nums1[i]
                else:
                    right_min = min(nums1[i],nums2[j])
                
                return (left_max+right_min)/2 

nums1 = [1,2]
nums2 = [3]
s = Solution()
print( s.findMedianSortedArrays(nums1,nums2) )           
    
