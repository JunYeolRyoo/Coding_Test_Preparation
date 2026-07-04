<img width="857" height="717" alt="Screenshot 2026-07-04 185401" src="https://github.com/user-attachments/assets/c8446170-b4aa-4a34-9d14-01871e162af9" />
<br>

``` python
def solution(numbers):
    answer = [-1]*len(numbers)
    stk = [0]
    for i in range(1,len(numbers)):
        if numbers[i] <= numbers[stk[-1]]: stk.append(i)
        else:
            while stk and numbers[stk[-1]] < numbers[i]:
                answer[stk[-1]] = numbers[i]
                stk.pop()
            stk.append(i)
    
    return answer
```

***Time Complexity: O(N)***<br>
***Space Complexity: O(N)***
