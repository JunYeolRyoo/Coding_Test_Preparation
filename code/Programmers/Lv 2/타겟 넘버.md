<img width="692" height="632" alt="image" src="https://github.com/user-attachments/assets/4c178b25-7beb-4f42-98d9-c860ddb2f9d1" />

``` python
def solution(numbers, target):
    answer = 0
    def helper(numbers,target,curSum,curInd):
        nonlocal answer
        if curInd == len(numbers):
            if curSum == target:
                answer += 1
            return None
        
        for i in [numbers[curInd],numbers[curInd]*-1]:
            helper(numbers,target,curSum+i,curInd+1)
    helper(numbers,target,0,0)
    return answer
```
***Time Complexity: O(2^N) (N<=20)<br>***
***Space Complexity: O(N)***
