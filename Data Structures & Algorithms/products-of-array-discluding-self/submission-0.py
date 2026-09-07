class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix =[1] * len(nums)
        postfix = [1] * len(nums)

        current = 1
        for i, num in enumerate(nums):
            prefix[i] = current
            current *= num

        current = 1
        for i, num in reversed(list(enumerate(nums))):
            postfix[i] = current
            current *= num

        return [pre * post for pre, post  in zip(prefix, postfix)]
  