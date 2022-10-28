# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = []
        i = -1
        for number1 in nums:
            i = i + 1
            j = -1
            for number2 in nums:
                j = j + 1
                if number1 + number2 == target and i != j:
                    if number1 > number2:
                        result.append(j)
                        result.append(i)
                        return result
                    else:
                        result.append(i)
                        result.append(j)
                        return result

solution_Object = Solution()
nums = [3,6,7,8,9,12]
target = 17
nums = [3,3]
target = 6
nums = [3,2,4]
target = 6
index_list = solution_Object.twoSum(nums,target)
print("inside twoSum def ")
print("target - ", target)
print("nums - ", nums)
print("The result is", index_list)