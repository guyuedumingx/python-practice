###All The Same


Request:
```
In this mission you should check if all elements in the given list are equal.  
Input: List.  
Output: Bool.  
```

Example:
```
all_the_same([1, 1, 1]) == True
all_the_same([1, 2, 1]) == False
all_the_same(['a', 'a', 'a']) == True
all_the_same([]) == True
```

Best solution:  
```python
def all_the_same(elements):
   return elements[1:] == elements[:-1]
```

Explanation:
```
elements = [X1,X2,X3,X4,X5]
elements[:-1] # [X1,X2,X3,X4]
elements[1:] #  [X2,X3,X4,X5]
compares a pair and then moves further: compares X1 with X2 and if they are equal, 
it will then compare X2 and X3 and so on.

This solution works because of transitivity. If X1 == X2 and X2 == X3, then X1 == X3.
In reality, you're always comparing X1 (which is equal to X2, X3, X4) to the next element.
```

Other solution:
```
def all_the_same(elements: List[Any]) -> bool:
    return len(set(elements)) <= 1
```
