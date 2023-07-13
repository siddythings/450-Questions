## Two Sum : Check if a pair with given sum exists in Array
```
Example 1:
Input Format: N = 5, arr[] = {2,6,5,8,11}, target = 14
Result: YES (for 1st variant)
       [1, 3] (for 2nd variant)
Explanation: arr[1] + arr[3] = 14. So, the answer is “YES” for the first variant and [1, 3] for 2nd variant.

Example 2:
Input Format: N = 5, arr[] = {2,6,5,8,11}, target = 15
Result: NO (for 1st variant)
	[-1, -1] (for 2nd variant)
Explanation: There exist no such two numbers whose sum is equal to the target.
```
### Solution
```
def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i,n in enumerate(nums):
            if n in dict:
                return dict[n],i
            else:
                dict[target-n]=i

```

## Best Time to Buy and Sell Stock
```
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

```
### Solution
```
def maxProfit(self, prices):
        profit = 0
        buy = prices[0]
        for sell in prices[1:]:
            if sell > buy:
                profit = max(profit, sell - buy)
            else:
                buy = sell
        
        return profit
```
## Contains Duplicate : Check if a value appears atleast twice
```
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1, 2, 3, 1]
Output: true.
Explanation: 1 appeared two times in the input array.

Example 2: 
Input: nums = [1, 2, 3, 4]
Output: false
Explanation: input array does not contain any duplicate number. 
```
### Solution

#### Approach 1: we can easily find any duplicate in the array just by using two nested loops. The first loop will pick integers one by one from the array and the second nested loop will check if there exists any duplicate or not. 
```
def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False
```

#### Approach 2: Sorting
```
def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return True
        return False
```

#### Approach 3: Hash Set
```
def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
```

## Kadane’s Algorithm : Maximum Subarray Sum in an Array
```
Problem Statement: Given an integer array arr, find the contiguous subarray (containing at least one number) which
has the largest sum and returns its sum and prints the subarray.
```

### Solution
```
def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        currentSum = 0
        
        for num in nums:
            currentSum += num
            
            if currentSum > maxSum:
                maxSum = currentSum
            
            if currentSum < 0:
                currentSum = 0
        
        return maxSum
```

## Maximum Product Subarray in an Array
```
Given an array that contains both negative and positive integers, find the maximum product subarray.
Input:
 Nums = [1,2,3,4,5,0]
Output:
 120
Explanation:
 In the given array, we can see 1×2×3×4×5 gives maximum product value.

Example 2:
Input:
 Nums = [1,2,-3,0,-4,-5]
Output:
 20
Explanation:
 In the given array, we can see (-4)×(-5) gives maximum product value.
```

#### Approch 1 (n2)
```
Find all possible subarrays of the given array. Find the product of each subarray. Return the maximum of all them.

int maxProductSubArray(nums):
    result = nums[0];
    for i in range(len(nums)):
        p = nums[i];
        for j in range(i+1, len(nums)):
           result = max(result,p);
           p *= nums[j];
        
        result = max(result,p)
    return result;
```
#### Approch 2 (On)
```
Idea is to find the maximum product from both sides,i.e, once in a forwarding direction and another in the backward direction.

def maxProductSubArray(nums):
    maxLeft = nums[0]
    maxRight = nums[0]

    prod = 1

    zeroPresent = False

    for i in nums:
        prod *= i
        if i == 0:
            zeroPresent = True
            prod = 1
            continue
        maxLeft = max(maxLeft, prod)

    prod = 1

    for j in range(len(nums) - 1, -1, -1):
        prod *= nums[j]
        if nums[j] == 0:
            zeroPresent = True
            prod = 1
            continue
        maxRight = max(maxRight, prod)

    if zeroPresent:
        return max(max(maxLeft, maxRight), 0)
    return max(maxLeft, maxRight)

```
