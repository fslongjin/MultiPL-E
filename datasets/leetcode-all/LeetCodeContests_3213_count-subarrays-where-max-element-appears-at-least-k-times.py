from typing import List

def countSubarrays(nums: List[int], k: int) -> int:
    """
    You are given an integer array nums and a positive integer k.
    Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.
    A subarray is a contiguous sequence of elements within an array.
    
    Example 1:
    
    Input: nums = [1,3,2,3,3], k = 2
    Output: 6
    Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
    
    Example 2:
    
    Input: nums = [1,4,2,1], k = 3
    Output: 0
    Explanation: No subarray contains the element 4 at least 3 times.
    
    
    Constraints:
    
    1 <= nums.length <= 105
    1 <= nums[i] <= 106
    1 <= k <= 105
    """
    ### Canonical solution below ###
    pass

### Unit tests below ###
def check(candidate):
    assert candidate([1, 3, 2, 3, 3], 2) == 6
    assert candidate([1, 4, 2, 1], 3) == 0
    assert candidate([61, 23, 38, 23, 56, 40, 82, 56, 82, 82, 82, 70, 8, 69, 8, 7, 19, 14, 58, 42, 82, 10, 82, 78, 15, 82], 2) == 224
    assert candidate([37, 20, 38, 66, 34, 38, 9, 41, 1, 14, 25, 63, 8, 12, 66, 66, 60, 12, 35, 27, 16, 38, 12, 66, 38, 36, 59, 54, 66, 54, 66, 48, 59, 66, 34, 11, 50, 66, 42, 51, 53, 66, 31, 24, 66, 44, 66, 1, 66, 66, 29, 54], 5) == 594
    assert candidate([28, 5, 58, 91, 24, 91, 53, 9, 48, 85, 16, 70, 91, 91, 47, 91, 61, 4, 54, 61, 49], 1) == 187
    assert candidate([43, 105, 105, 88, 19, 82, 95, 32, 80, 37, 49, 105, 25, 105, 46, 54, 45, 84, 105, 88, 26, 20, 49, 54, 31, 105, 8, 103, 37, 32, 105, 105, 97, 27, 105, 89, 105, 47, 25, 87, 29, 105, 105, 105, 24, 105, 105, 48, 19, 91, 96, 71], 7) == 454
    assert candidate([107, 101, 180, 137, 191, 148, 83, 15, 188, 22, 100, 124, 69, 94, 191, 181, 171, 64, 136, 96, 91, 191, 107, 191, 191, 191, 107, 191, 191, 11, 140, 33, 4, 110, 83, 5, 86, 33, 42, 186, 191, 6, 42, 61, 94, 129, 191, 119, 191, 134, 43, 182, 191, 187, 63, 116, 172, 118, 50, 141, 124, 191, 125, 145, 191, 34, 191, 191], 9) == 548
    assert candidate([41, 121, 92, 15, 24, 59, 45, 110, 97, 132, 75, 72, 31, 38, 103, 37, 132, 91, 132, 132, 105, 24], 3) == 61
    assert candidate([21, 11, 13, 15, 16, 21, 8, 9, 6, 21], 2) == 10
    assert candidate([31, 18, 36, 166, 166, 166, 135, 166, 166, 12, 102], 3) == 31
    assert candidate([2, 2, 2, 2, 1, 3, 3, 2, 2, 1, 1, 3, 1, 1, 2, 3, 2, 1, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 3, 1, 3, 3], 5) == 31
    assert candidate([3, 2, 4, 4, 3, 4, 3, 1, 1, 1, 1, 3, 2, 1, 2, 1, 3, 4, 4, 1, 2, 4, 1, 1, 2, 3, 3, 3, 4, 4, 4, 1, 3, 1, 4, 1, 4, 4, 4, 2, 2, 3, 4, 3, 3, 2, 2, 2, 1, 2, 4, 2, 2, 4, 4, 1, 3, 2, 3, 2, 4, 4, 4, 2, 3, 4, 2, 4, 1, 4, 1, 4, 1, 4, 4, 3, 4, 2, 4, 3, 3, 2, 3, 3, 2, 3, 4, 2, 1, 1, 1, 2, 3], 23) == 473
    assert candidate([1, 1, 1, 2, 3, 2, 1, 2, 3, 3, 3, 3, 2, 3, 2, 1, 1, 2, 2, 1, 3, 2, 3, 1, 2, 1, 3, 1, 1, 3, 1, 2, 1, 1, 1, 1, 1, 1, 3], 8) == 148
    assert candidate([54, 161, 161, 161, 161, 31, 74, 51, 87, 19, 161, 116, 108, 149, 6, 19, 155, 101, 161, 161, 154, 161, 78, 132, 62, 156, 112, 51, 161, 42, 92, 151, 142, 17, 110, 85], 4) == 279
    assert candidate([97, 102, 144, 55, 144, 128, 16, 93, 144, 9, 144, 15, 144, 144, 32, 68, 144, 60, 94, 56, 103, 5, 41, 27, 48, 144, 12, 86, 129, 144, 144, 99, 93, 96, 144, 73, 106, 76, 107, 144, 53, 21, 144, 144, 98, 32, 85, 97, 71, 127, 144, 9, 144, 144, 133, 125, 144, 135, 52, 144, 144, 46, 134, 23, 23, 144, 79], 1) == 2163
    assert candidate([17, 17, 15, 9, 14, 11, 15, 1, 6, 2, 1, 17, 3, 17, 11, 12, 9, 11, 2, 4, 15, 17, 3, 17, 8, 6, 7, 12, 3, 16, 2, 9, 14, 17, 17, 17, 3, 7, 8, 9, 8, 17, 17, 17, 4, 2, 12, 17, 7, 17, 17, 16, 17, 17, 8, 12, 11, 3, 10, 4, 10, 17, 14, 7, 5, 17, 12, 10, 17, 13, 5, 17, 8, 14, 9, 17, 17, 17, 7, 16, 10, 13, 17, 15, 1, 14, 6, 8, 11, 3], 15) == 1055
    assert candidate([17, 12, 16, 17, 7, 1, 12, 6, 17, 5, 17, 13, 16, 16, 17, 14, 17, 6, 17, 17, 17, 17, 16, 17, 14, 8, 14, 1, 12, 13, 17, 17, 14, 8, 14, 5, 16, 17, 17], 5) == 404
    assert candidate([98, 59, 98, 32, 45, 15, 98, 98, 98, 65, 98, 10, 98, 89, 87, 51, 42, 58, 76, 23, 85, 98, 98, 35, 18, 65, 39, 88, 56, 62, 10, 32, 8, 16, 32, 98, 6, 39, 14, 24, 98, 95, 68, 98, 77, 47, 98, 23, 69, 98, 49, 98, 7, 11, 92, 98, 27, 25, 85, 98, 45, 30, 50, 62, 46, 1, 79, 58, 69, 15, 59, 57, 85, 19, 98, 95, 98, 67, 52, 98, 59, 8, 98, 98, 98, 73, 86, 20, 98, 96, 21, 98, 79, 97, 52, 22, 98, 86], 12) == 1168
    assert candidate([6, 50, 118, 27, 133, 133, 3, 121, 133, 72, 117, 133, 91, 57, 107, 93, 66, 122, 133, 6, 133, 122, 81, 20, 133, 133, 121, 133, 46, 25, 133, 133, 133, 17, 8, 49, 133, 116, 40, 133, 67, 9, 133, 133, 133, 133, 109, 41, 127, 13, 39, 133, 133, 133, 122, 58, 8, 125, 33, 62], 12) == 538
    assert candidate([94, 34, 112, 106, 112, 13, 12, 112, 112, 21, 48, 71, 112, 104, 112, 29, 99, 58, 23, 11, 49, 112, 20, 86], 4) == 105
    assert candidate([21, 27, 9, 85, 1, 7, 28, 11, 44, 39, 85, 52, 51, 30, 67, 83, 75, 10, 57, 59, 53, 85, 75, 33, 35, 85, 76, 85, 65, 85, 85, 85, 35, 4, 60, 85, 85, 72, 57, 42, 34, 85, 53, 85, 85, 36, 85, 56, 13, 16, 69, 55, 81, 24, 85, 27, 54, 66, 10, 85, 30, 58, 71, 43, 85, 66, 42, 27, 85, 70], 13) == 508
    assert candidate([8, 14, 7, 1, 11, 10, 1, 13, 7, 14, 14, 6, 13], 2) == 32
    assert candidate([165, 135, 165, 46, 126, 165, 73, 165, 165, 155, 150, 165, 40, 38, 165, 145, 137, 106, 10], 7) == 5
    assert candidate([9, 3, 12, 6, 24, 23, 24], 2) == 5
    assert candidate([42, 85, 78, 92, 46, 63, 21, 14, 22, 37, 96, 50, 74], 1) == 33
    assert candidate([73, 54, 15, 4, 23, 70, 53, 65, 73, 73, 2, 72, 36, 71, 73, 69, 35, 18, 62, 73, 62, 73, 73, 50, 30, 73, 20, 71, 60, 9, 12, 57, 48, 73, 40, 20, 8, 73, 73, 73, 34, 59, 31, 49, 73, 5, 51, 36, 47, 38, 36, 58, 34, 42, 23, 28, 52, 73], 1) == 1537
    assert candidate([52, 88, 92, 92, 44, 4, 92, 37, 27, 59, 3, 3, 76, 51, 21, 89, 92, 31, 26, 10, 47, 69, 30, 68, 60, 92, 80, 19, 65, 38, 92, 4, 54, 88, 92, 75, 56, 71, 11, 92, 44, 43, 56, 92, 16, 66, 22, 70], 2) == 796
    assert candidate([29, 9, 43, 5, 8, 52, 24, 52, 52, 41, 33, 52, 27, 52, 8, 6, 35, 52, 27, 52, 7, 2, 9, 52, 52, 42, 52, 52], 7) == 76
    assert candidate([165, 165, 58, 153, 45, 124, 165, 143, 38, 165, 165, 165, 165, 73, 8, 138, 165, 139, 165, 165, 59, 40, 120, 165, 123, 92, 98, 136, 161], 1) == 394
    assert candidate([28, 64, 64, 63, 21, 64, 55, 64, 10, 30, 12, 5, 64, 56, 63, 64, 64, 31, 31, 64, 19, 54, 53, 64, 58, 44, 64, 28, 64, 64, 63, 10, 64, 64, 57, 29, 44, 32, 50, 55, 49, 21, 64, 64, 34, 26, 28, 64, 15, 31, 28, 64, 45, 64, 19, 54, 9, 41, 25, 33, 7, 60, 1, 7, 34, 14, 4, 64, 64, 64, 55, 49, 3, 41, 28, 42, 40, 52, 25, 46, 25, 15], 18) == 229
    assert candidate([97, 23, 53, 33, 141, 150, 128, 153, 71, 39, 153, 35, 125, 143], 2) == 32
    assert candidate([144, 144, 87, 144, 18, 53, 129, 61, 34, 123, 141, 68, 37, 23, 94, 28, 64, 58, 16, 36, 27, 112, 144, 80, 77, 144, 97, 142, 8, 101, 14, 74, 37, 115, 115, 144, 99, 37, 144, 48, 28, 110, 13, 78, 144, 144, 83, 7, 112, 144, 144, 144, 78, 61, 87, 144, 144, 61, 144, 44, 123, 74, 144, 142], 4) == 1083
    assert candidate([63, 129, 134, 61, 134, 134, 134, 43, 74, 4, 111], 2) == 38
    assert candidate([46, 105, 44, 36, 106, 35, 91, 8, 52, 106, 95, 86, 75, 7, 19, 30, 25, 27, 18, 72, 106, 106, 33, 106, 6, 63, 67, 45, 15, 106, 106, 6, 42, 106, 27, 14, 18, 106, 4, 106, 95, 64, 23, 93, 106, 37, 106, 106, 16, 81, 91, 79, 106, 97, 106, 66, 31, 59, 58], 1) == 1637
    assert candidate([78, 120, 110, 53, 53, 120, 116, 39, 64, 120, 120, 120, 120, 120, 97, 28, 92, 120, 101, 5, 46, 92], 1) == 224
    assert candidate([111, 111, 72, 111, 111, 56, 21, 95, 111, 101, 38, 77, 111, 111, 76, 58, 70, 72, 32, 72, 19, 111, 111, 63, 39, 111], 9) == 5
    assert candidate([33, 82, 82, 82, 71, 39, 17, 82, 38, 75, 82, 2, 82, 82, 9, 82, 57, 12, 78, 65, 29, 20, 82, 82, 50, 11, 39, 74, 65, 69, 81, 71, 25, 82, 46, 43, 49, 80], 6) == 219
    assert candidate([83, 72, 17, 147, 147, 57, 147, 22, 120, 107, 59, 133, 123, 91, 147, 147, 72, 147, 31, 147, 147, 147, 96, 147, 18, 25, 13, 8, 18, 59, 46, 91, 15, 147, 25, 30, 6, 147, 113, 27, 84, 95, 38, 147, 147, 147, 106, 53, 127, 132, 55, 147, 22, 147, 124, 102, 17, 69, 131, 147, 4, 95, 59, 38, 147, 147, 41, 99, 142, 147, 136, 142, 57, 26, 16, 3, 142], 8) == 1336
    assert candidate([52, 95, 173, 26, 173, 16, 4, 144, 173, 77, 22, 103, 162, 120, 77, 173, 173, 89, 173, 104, 62, 151, 173, 124, 173, 117, 113, 164, 3, 70, 15, 144, 161, 118, 139, 16, 157, 173, 154, 151, 37, 69, 60, 173, 173, 168, 148, 97, 173, 125, 161, 128, 85, 64, 70, 102, 100, 168, 56, 57, 157, 112, 119, 135, 42, 72, 135, 173, 173, 124, 143, 121, 75, 37, 162, 161, 102, 50, 173, 173, 107], 4) == 1940
    assert candidate([4, 18, 6, 22, 19, 15, 20, 12, 22, 22, 19, 6, 10, 7, 20, 4, 22, 21, 7, 17, 3, 16, 13, 17, 22, 14, 8, 2, 3, 22, 18, 18, 22, 22, 7, 22, 13, 10, 20, 4, 14, 17, 9, 19, 1, 12, 3, 11, 19, 15, 6, 4, 10], 6) == 347
    assert candidate([55, 103, 123, 68, 16, 72, 104, 63, 40, 15, 180, 162, 82, 180, 131, 46, 180, 2, 120, 107, 100, 97, 180, 180, 17, 134, 180, 124, 40, 125, 15, 132, 4, 112, 180, 180, 28, 66, 180, 122, 99, 46, 15, 180, 180, 111, 30, 169, 132, 180, 10, 180, 180, 180, 107, 74, 95, 28, 180, 66, 180, 128, 61, 180, 118, 180, 28, 103, 37, 180, 88, 152], 8) == 1181
    assert candidate([20, 6, 49, 60, 16, 54, 13, 2, 35, 6, 27, 62, 67, 56, 27, 6, 33, 51, 67, 42, 9, 59, 67, 14, 59, 7, 67, 34, 51, 5, 67, 48, 53, 20, 35, 67, 65, 34, 67, 67, 62, 7, 27, 18, 40, 10, 67, 67, 9, 8, 60, 12, 2, 67, 64, 67, 60, 28, 60, 26, 37, 2, 67, 33, 49, 23, 2, 36, 67, 6, 67, 7, 67, 44, 18], 8) == 1034
    assert candidate([191, 2, 46, 65, 191, 166, 191, 156, 157, 181, 167, 123, 26, 191, 191, 104, 33, 126, 51, 191, 191, 191, 6, 152, 74, 84, 126, 191, 191, 162, 188, 38, 30, 191, 191, 125, 30, 56, 12, 151, 45, 163, 91, 168, 15, 125, 60, 4, 108, 27, 67, 97, 125, 147, 167, 152, 191, 159, 142, 105], 7) == 647
    assert candidate([2, 4, 11, 30, 23, 1, 8, 18, 4, 6, 30, 30, 30, 10, 30, 17, 24, 13, 17, 30, 25, 30, 30, 12, 15, 29, 24, 28, 21, 30, 25, 11, 1, 30, 9, 30, 21, 3, 10, 6, 30, 5, 5, 24, 21, 30, 17, 29, 21, 30, 3, 30, 8, 18, 17], 7) == 584
    assert candidate([141, 106, 141, 141, 94, 98, 33, 141, 2, 115, 11, 141, 9, 131, 104, 2, 141, 75, 141, 141, 24, 141, 28, 68, 141, 134, 141, 110, 15, 21, 141, 65, 108, 141, 35, 95, 94, 141, 117, 25], 10) == 94
    assert candidate([139, 94, 77, 139, 139, 139, 139, 92, 61, 105, 25, 139, 93, 139, 113, 128, 139, 81, 70, 139, 25, 139, 37, 118, 15, 5, 139, 115, 133, 1], 3) == 292
    assert candidate([107, 160, 86, 160, 69, 160, 160, 73, 120, 129, 130, 104, 112, 136, 7, 100, 21, 160, 160, 94, 3, 96, 160, 65, 74, 87, 110, 160, 145, 116, 38, 72, 127, 152, 71, 24, 35, 79, 160, 120, 160, 80, 50, 160, 129, 50, 82, 160, 140, 160, 3, 17, 129, 18, 108, 34, 132, 69, 4, 160, 124, 108, 30, 125, 160, 102, 51, 138, 160, 120, 159, 160, 49, 68, 160, 19, 87, 160, 6, 160, 76, 160, 110], 16) == 124
    assert candidate([89, 9, 89, 82, 89, 11, 31, 45, 61, 56, 27, 15, 33, 6, 5, 89, 28, 73, 8, 48, 11, 89, 5, 89, 4, 65, 18, 20, 17, 38, 4, 36, 59, 34, 5, 81, 10, 6, 44, 19, 20, 86, 58, 60, 27, 89, 34, 29, 36, 88, 89, 10, 73], 7) == 14
    assert candidate([45, 40, 44, 51, 51, 33, 33, 38, 46, 38, 51, 40, 9, 29, 51, 40, 51, 36, 39, 36, 51, 24, 39, 51, 31, 50, 12, 50, 1, 51, 32, 51, 49, 12, 44, 19, 4, 26, 7, 51, 14, 4, 33, 36, 19, 18, 14, 20, 16, 11, 51, 51, 7, 18, 7, 10, 8, 8, 48, 51, 43, 41, 51], 10) == 199
    assert candidate([102, 4, 3, 22, 78, 96, 21, 126, 103, 52, 99, 94, 57, 126, 49, 20, 75, 126, 93, 1, 4, 126, 122, 123, 21, 111, 23, 110, 126, 81, 112, 92, 121, 30, 41, 126, 20, 10, 126, 54, 15, 27, 126, 126, 9, 126, 126, 1, 106, 34, 119, 108, 126, 126, 34, 57, 27, 126, 110, 126, 65, 125, 126, 59, 117, 126, 67, 114, 115, 38, 79, 123, 118, 126, 33, 52, 1, 119, 11, 105, 21, 51, 75, 126, 84], 9) == 1500
    assert candidate([71, 122, 36, 39, 48, 158, 83, 20, 131, 41, 126, 1, 33, 19, 138, 133, 80, 106, 92, 2, 68, 158, 158, 111, 158, 50, 158, 81, 158, 138, 108, 36, 149], 4) == 171
    assert candidate([39, 136, 153, 85, 134, 19, 34, 22, 5, 124, 116, 91, 122, 160, 112, 160, 22, 111, 160, 160, 113, 34, 40, 16, 160, 117, 61, 160, 31, 34, 145, 160], 6) == 72
    assert candidate([14, 14, 1, 8, 2, 11, 14, 14, 5, 1, 8, 1, 6, 3, 14, 14, 14, 2, 9, 10, 14, 2, 3, 14, 2, 5, 5, 11, 10, 11, 14, 5, 3, 10, 5, 3, 1, 3, 14, 5, 13, 9, 2, 9, 3, 5, 14, 14, 2, 3, 10, 4, 14, 14, 10, 14, 2, 10, 9, 2, 7, 9, 11, 14, 9, 5, 1, 5, 13, 6, 10, 1, 7, 4, 13, 13, 9, 10, 2, 10, 3, 8, 14, 3, 14, 13, 1, 14, 8, 12, 1, 6, 12, 14, 14], 14) == 438
    assert candidate([1, 7, 4, 10, 12, 10, 10, 1, 12, 1, 6, 6, 9, 7, 10, 6, 12, 10, 7, 9, 6, 10, 12, 8, 11, 9, 8, 3, 8, 3, 12, 12, 12, 3, 2, 2, 3, 1, 10, 2, 12, 12, 12, 9, 10, 1, 8, 10, 12, 4, 8, 8, 6, 2, 11, 7, 3, 3, 12, 12, 2, 7, 8, 11, 4, 3, 12, 5, 8, 12, 10, 2, 9, 6, 5, 10, 8], 7) == 1236
    assert candidate([1, 7, 11, 13, 10, 13, 8, 6, 4, 11, 13, 6, 1, 6, 8, 10, 5, 13, 4, 2, 3, 7, 12, 5, 1, 1, 11, 13, 8, 9, 1, 8], 2) == 262
    assert candidate([73, 24, 67, 11, 66, 73, 73, 40, 4, 47, 25, 26, 48, 40, 27, 69, 73, 28, 23, 9, 16, 8, 63, 65, 73, 57, 73, 21, 43, 73, 19], 1) == 408
    assert candidate([7, 47, 50, 16, 35, 24, 61, 44, 53, 49], 1) == 28
    assert candidate([14, 89, 43, 1, 12, 64, 23, 89, 55, 23, 56, 69, 62, 89, 89, 86, 89, 89, 89, 76, 84, 57, 18, 54, 29, 50, 67, 69, 65, 3, 22, 26, 8, 77, 51, 74, 74, 40, 89, 89, 18, 74, 89, 26, 16, 27, 1, 66, 72, 22, 78, 20, 15, 14, 63, 77, 73, 23, 65, 89, 79, 32, 18, 89, 59, 16, 24, 39, 87, 78, 29, 84, 89, 49, 80, 69, 89, 44, 89, 89, 58, 6, 55, 38, 89, 53, 89, 3, 81, 28, 65, 39, 30, 14, 16, 89, 22, 4, 23, 84], 7) == 2045
    assert candidate([16, 11, 12, 16, 5, 17, 11, 13, 12, 17, 16, 2, 3, 13, 1, 4, 10, 2, 17, 17, 8, 7, 4, 17, 11, 17, 8, 2, 15, 17, 4, 16, 9, 8, 17, 2, 17, 16, 17, 4, 6, 8, 12, 17, 16, 13, 4, 11, 9, 11, 16, 10, 17, 17, 10, 13, 17, 13, 1, 13, 3, 7, 4, 2, 15, 6, 11, 12, 17, 17, 7, 15, 9, 16, 7, 2, 17, 7, 17, 16, 5, 8], 8) == 1317
    assert candidate([52, 46, 47, 52, 52, 4, 2, 21, 2, 26, 47, 26, 52, 7, 12, 35, 52, 33, 47, 3, 31, 37, 36, 52, 38, 19, 12, 40, 52, 7, 40, 16, 51, 41, 52, 23, 20, 52, 18, 52, 21, 2, 52, 49, 5, 48, 23, 52, 52], 8) == 132
    assert candidate([99, 155, 73, 80, 32, 69, 113, 37, 126, 155, 95, 155, 155, 48, 155, 43, 37, 68, 131, 68, 150, 155, 153, 155, 45, 59, 155, 155, 155, 77, 155, 155, 100, 4, 127, 155, 107, 151, 101, 104, 155, 155, 71, 147, 153, 37, 155, 18, 155, 100, 155, 153, 155, 155, 138, 4, 114, 153, 111, 83, 74, 144, 18, 64, 94, 155, 50, 45, 51, 122, 146, 50, 43], 8) == 1346
    assert candidate([64, 156, 156, 119, 156, 35, 108, 82, 86, 18, 107, 156, 68, 83, 130, 86, 80, 8, 129, 95, 23, 7, 71, 131, 19, 156, 17, 21, 43, 156, 25, 156, 124, 51, 91, 156, 77, 88, 156, 156, 62, 105, 135, 142, 156, 156, 78, 156, 113, 156, 47, 156, 156, 22, 71, 49, 156, 57, 71, 156, 36, 84, 139, 156, 17, 49, 156, 121, 46, 7, 155, 156, 156, 156, 93, 150, 102, 81, 90, 52, 52, 91, 2, 63, 156, 49, 118, 77, 156, 156, 156, 79], 19) == 590
    assert candidate([24, 9, 28, 46, 14, 41], 1) == 12
    assert candidate([169, 19], 1) == 2
    assert candidate([95, 109, 79, 198, 195, 198, 198, 97, 34, 43, 165, 198, 198, 195, 98, 198, 198, 170, 39, 78, 21, 198, 140, 187, 29, 107, 198, 132, 198, 174, 109, 187, 173, 198, 58, 38, 62, 179, 198, 68, 114, 198, 10, 198, 81, 198, 40, 10, 71, 82, 196, 128, 50, 153, 146, 101, 195], 12) == 182
    assert candidate([9, 15, 39, 33, 43, 47, 15, 29, 14, 12, 48, 37, 9, 37, 15, 48, 48, 3, 1, 48, 37, 39, 43, 29, 43, 15, 35, 2, 33, 48, 28, 37, 48, 45, 9, 36, 3, 48, 29, 14, 48, 11, 24, 30, 38, 18, 24, 12, 47, 31, 22, 10, 29, 46, 14, 48, 15, 29, 43, 48, 37, 48, 46, 14, 32, 33, 15, 42, 9, 12, 48, 20, 35, 44, 48, 4], 10) == 274
    assert candidate([37, 12, 14, 46, 29, 98, 149, 149, 149, 67, 97, 56, 81, 71, 11, 149, 32, 149, 119, 149, 44, 149, 43, 149, 149, 32, 75, 54, 24, 148, 41], 2) == 379
    assert candidate([59, 101, 127, 118, 19, 55, 18, 127, 127, 26, 127, 103, 4, 127, 26, 43, 26, 125, 80, 127, 127, 112, 2, 107, 127, 127, 110, 122, 77, 127, 11, 86, 127, 127, 91, 27, 85, 86, 71, 36, 41, 127, 86, 37, 11], 6) == 418
    assert candidate([82, 82, 42, 51, 82, 64, 13, 16, 36, 49, 22, 52, 82, 10, 72, 9, 6, 42, 80, 74, 37, 80, 73, 10, 82, 31, 78, 22, 14, 11, 82, 60, 76, 67, 82, 2, 61, 52, 79, 72, 77, 12, 23, 33, 44, 11, 82, 4, 14, 65, 19, 66, 56, 11, 75, 82, 42, 82, 56, 77, 82, 81, 51, 48, 19, 70, 33, 51, 9, 78, 62, 31, 41, 46, 13, 82, 82, 77, 55, 24, 49, 82, 82, 8, 3, 44, 34], 9) == 427
    assert candidate([30, 83, 42, 83, 83, 60, 61, 60, 62, 83, 74, 32, 83, 83, 46, 82, 25, 81, 31, 83, 48, 15, 49, 43, 41, 83, 29, 36, 45, 53, 83, 74, 55, 63, 1, 19, 74, 2, 15, 83, 61, 82, 46, 48, 83, 83, 8, 45, 83, 80, 30, 33, 83, 83, 83, 22, 65, 79, 57, 15, 24, 25, 83, 83, 60, 60, 83, 44, 9, 29, 60, 69, 2, 83, 35, 7, 40, 74, 55, 83, 7, 21, 11, 59, 5, 80], 17) == 200
    assert candidate([11, 25, 22, 14, 14, 29, 6, 28, 12, 14, 2, 15, 29, 2, 6, 27, 22, 29, 26, 29, 11, 1, 7, 27, 24, 29, 7, 29, 6], 1) == 371
    assert candidate([173, 97, 53, 181, 161, 119, 152, 97, 69, 181, 123, 84, 83, 9, 169, 135, 86, 27, 119, 181, 64, 147, 7, 181, 154, 43, 83, 181, 14, 181, 45, 77, 181, 83, 181, 53, 181, 117, 181, 27, 181, 174, 181, 47], 6) == 302
    assert candidate([124, 52, 111, 24, 191, 117, 128, 153, 69, 190, 51, 1, 112, 52, 28, 191, 188, 191, 1, 124, 128, 111, 191, 94, 34, 167, 191, 191, 9, 191, 164, 60, 113, 69, 151, 130, 15, 86, 150, 191, 175, 36, 113, 23, 119, 68, 191, 87, 90, 159, 178, 50, 104, 191, 187, 48, 97, 100, 136, 155, 140, 132, 1, 180, 182, 191, 130, 110, 191, 191, 191, 191, 191, 177, 73, 118, 191, 27, 129, 124, 43, 140, 191, 132, 191, 41, 44, 191, 169, 49, 191, 191, 191, 191, 113, 4], 7) == 2434
    assert candidate([86, 89, 92, 23, 92, 72, 41, 92, 92, 92, 47, 30, 46, 76, 20, 80, 92, 60, 20, 9, 92, 92, 92, 36, 4, 38, 92, 74, 15, 20, 92, 2, 73, 58, 68, 2, 29, 13, 92, 91, 92, 44, 46, 8, 57, 10, 47, 92, 6, 90, 92, 92, 76, 92, 86, 26, 22, 67, 92, 92, 17, 92, 18, 23, 22, 40, 7], 9) == 738
    assert candidate([75, 65, 37, 83, 80, 17, 69, 83, 83, 76, 64, 58, 13, 83, 18, 66, 25, 55, 25, 60, 83, 83, 83, 50, 70, 39, 82, 83, 47, 39, 74, 83, 75, 83, 34, 8, 81, 46, 52, 72, 45, 65, 46, 2, 9, 4, 23, 47, 83, 83, 59, 32, 54, 43, 53, 56, 83], 9) == 256
    assert candidate([23, 70, 2, 70, 49, 65, 6, 69, 5, 26, 29, 70, 70, 15, 17, 22, 70, 63, 51, 25, 18, 68, 31, 3, 43, 60, 70, 6, 61, 23, 46, 21, 66, 67, 63, 3, 7, 70, 66, 47, 15, 65, 52, 70, 70, 38, 8, 18, 29, 33, 50, 9, 70, 9], 1) == 1305
    assert candidate([23, 12, 6, 3, 4, 7, 23, 23, 6, 23, 23, 9, 23, 2, 14, 11, 21, 23, 8, 9, 19, 10, 17, 23, 11, 3, 13, 23, 18, 3, 6, 7, 6, 19, 17, 14, 17, 7, 23, 21, 10, 22, 6, 23, 23, 3, 1, 20, 14, 7, 19, 20, 23, 19, 23, 15, 4, 23, 2, 6, 20, 23, 8, 6, 17, 14, 23, 6, 10, 23, 17, 6, 11, 8, 3, 6, 23, 16, 19, 16, 2, 19, 2, 23, 1, 16, 20, 4, 20, 12, 1], 11) == 942
    assert candidate([199, 146, 138, 199, 97, 169, 199, 198, 199, 199, 11, 62, 68, 122, 193, 199, 22, 41, 199, 181, 199, 157, 199, 44, 199, 199, 199, 142, 132, 112, 199, 199, 155, 199, 97, 101, 26, 52, 199, 45, 164, 112, 188, 97, 180, 103, 199, 3, 130, 64, 131, 199, 194, 135, 36, 199, 80, 67, 41, 67, 158, 183, 188, 12, 126], 13) == 420
    assert candidate([25, 32, 40, 47, 35, 9, 39, 58, 67, 42, 77, 57, 77, 77, 34, 28, 13, 77, 15, 33, 77, 10, 64, 67, 35, 21, 61, 60, 74, 57, 77, 71, 28, 77, 48, 67, 17, 48, 77, 77, 77, 60, 26, 30, 77, 49, 77, 3, 77, 33, 75, 77, 20, 77, 77], 9) == 325
    assert candidate([50, 108, 19, 118, 46, 45, 126, 118, 89, 126, 46, 63, 30, 126, 120, 10, 126, 126, 108, 95, 126, 94], 3) == 107
    assert candidate([28, 94, 94, 5, 1, 74, 33, 3, 88, 76, 78, 30], 1) == 32
    assert candidate([44, 4, 4, 31, 33, 51, 51, 40, 51, 2, 27, 48, 51, 6, 51, 27, 45, 1, 25, 2, 20, 43, 51, 12, 11, 44, 40, 28, 29, 51, 51, 45, 30, 24, 51, 51, 30, 51, 13, 18, 29, 51, 15, 11, 39], 11) == 52
    assert candidate([6, 30, 19, 32, 24, 8, 28, 2, 18, 32, 5, 31, 3, 31, 28, 30, 30, 22, 32, 22, 31, 1, 9, 2, 7, 32, 14, 24, 24, 6, 23, 6, 25, 32, 32, 22, 10, 11, 4, 2, 32, 18, 15, 1, 22, 20, 6, 26, 11, 13, 26, 22, 32, 30, 18], 4) == 570
    assert candidate([17, 41, 71, 95, 56, 88, 25, 95, 73, 95, 91, 95, 8, 43, 2, 52, 95, 88, 5, 49, 20, 48, 95, 84, 95, 44, 27, 95, 87, 32, 45, 95, 95, 95, 51, 56, 6, 5, 65, 21, 52, 56, 84, 95, 75, 33, 95, 62, 47, 95], 13) == 20
    assert candidate([5, 12, 6, 13, 11, 13, 9, 13, 10, 13, 13, 12, 7, 11, 2, 11, 4, 7, 6, 6, 13, 9, 1, 12, 13, 11, 7, 11, 11, 13, 2, 13, 7, 4, 9, 5, 13, 8, 4, 1, 2, 5, 13, 7, 7, 12, 2, 2, 8, 11, 12, 1, 8, 5, 3, 6, 4, 2, 9, 10, 6, 6, 13, 12, 13, 6, 13, 13, 13, 13, 13, 3, 4, 4, 10, 1, 2, 12, 12, 13, 13, 6, 13, 4, 13, 1, 12, 11, 9, 12, 2, 5], 3) == 3240
    assert candidate([13, 16, 2, 27, 10, 2, 44, 44, 44, 28, 44, 44, 23], 4) == 23
    assert candidate([69, 46, 80, 10, 80, 48, 76, 15, 67, 1, 80, 80, 34, 4, 14, 15, 2, 38, 62, 31, 17, 56, 58, 17, 38, 29, 67], 4) == 48
    assert candidate([39, 38, 136, 136, 97, 122, 54, 102, 112, 125, 135, 57, 136], 1) == 52
    assert candidate([39, 67, 17, 52, 89, 63, 52, 8, 14, 90, 76, 2, 90, 65, 90, 80, 90, 33, 61, 76, 90, 32, 43, 55, 62, 24, 29, 90, 35, 36, 90, 8, 40, 1, 72, 54, 64, 90, 58, 88, 77, 89, 35, 79, 90, 81, 90], 2) == 822
    assert candidate([16, 22, 10, 22, 4, 16, 16, 15, 3, 22, 22, 15, 7, 7, 21, 17, 16, 1, 10, 13, 16, 17, 2, 18, 2, 5, 11], 3) == 70
    assert candidate([120, 58, 118, 34, 32, 110, 94, 10, 119, 133, 70, 154, 151, 107, 124, 148, 154, 154, 24, 154, 6, 83, 20, 6, 3, 72, 154, 28, 148, 107, 154, 73, 126, 154, 41], 5) == 135
    assert candidate([15, 2, 1, 21, 20, 33, 16, 19], 1) == 18
    assert candidate([45, 25], 1) == 2
    assert candidate([179, 127, 54, 149, 90, 119, 179, 127, 115, 82, 159, 128, 6, 55, 33, 43, 2, 172, 105, 159, 83, 179, 30, 179, 175, 125, 179, 179, 105, 179, 74, 77, 179, 153, 145, 124, 70, 179, 129, 31, 62, 172, 179, 29, 130, 179, 82, 64, 98, 179, 91, 179, 89, 166, 60, 159, 54, 179, 179, 137, 54, 158, 64, 177, 56, 165, 97, 142, 90, 170, 179, 127, 111, 179, 145, 179, 8], 16) == 61
    assert candidate([25, 41, 11, 41, 26, 30, 41, 34, 31, 41, 40, 23, 14, 41, 10, 34, 8, 15, 41, 10, 14, 41, 37, 20, 37, 35, 37, 8, 21, 30, 11, 7, 33, 3, 25, 1, 3, 38, 27, 26, 27, 20, 29, 41, 30, 7, 23, 15, 41, 41, 41, 25, 18, 41, 19, 41, 34, 35, 33, 41, 4, 41, 15], 3) == 1227
    assert candidate([7, 6, 3, 9, 6, 3, 4, 4, 9, 7, 3, 3, 8, 9, 2, 4, 8, 8, 8, 6, 3, 2, 9, 9, 9, 4, 2, 6, 9, 3], 1) == 396
    assert candidate([158, 2, 138, 177, 96, 104, 175, 81, 46, 19, 85, 1, 174, 177, 115, 145, 32, 177, 174, 95, 96, 101, 177, 114, 115, 137, 77, 98, 15, 177, 125, 162, 177, 177, 111, 106, 112, 177, 174, 40, 177, 177, 176, 40, 177, 145, 177, 99, 177, 177, 163, 177, 143, 147, 177, 11, 142, 177, 44, 171, 52, 98, 177, 163, 140, 139, 61, 147, 71, 20, 177, 45, 172], 5) == 1642
    assert candidate([3, 1], 1) == 2
    assert candidate([99, 166, 166, 5, 166, 44, 83, 73, 40, 64, 166, 135, 166, 24, 166, 41, 70, 93, 166, 166, 166, 49, 157, 3, 135, 137, 1, 133, 18, 166, 15, 82, 4, 166, 13, 55, 95, 166, 166, 151, 102, 166, 166, 34, 32, 31, 48, 166, 166, 13, 166, 166, 94, 28, 166, 166, 119, 103, 157, 12, 103, 19, 126, 13, 117, 71, 85, 166, 166, 81, 132, 105, 128, 166, 166, 125, 73, 161, 166, 139, 6, 32, 5, 31, 137], 24) == 49
    assert candidate([121, 135, 135, 135, 57, 18, 7, 22, 135, 57, 96, 72, 23, 68, 32, 39, 135, 135, 135, 135, 51, 25, 100, 49, 72, 135, 99, 38, 126, 110, 52, 63, 48, 135, 135, 132, 111, 114, 135, 135, 24, 125, 135, 135, 120, 93, 55, 40, 135, 44, 135, 22, 135, 48, 35, 12, 116, 79, 80, 22, 135, 135, 111, 135], 20) == 7


def test_check():
    check(countSubarrays)


### Metadata below ###
# question_id = 3213
# question_title = Count Subarrays Where Max Element Appears at Least K Times
# question_title_slug = count-subarrays-where-max-element-appears-at-least-k-times
# question_difficulty = Medium
# question_category = Algorithms
# question_likes = 215
# question_dislikes = 10