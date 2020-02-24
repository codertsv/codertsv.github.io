# Anything Goes: Loops
*Examples from our 'anything goes' loop session on 24th of Feb 2020*

## Python 
Wytamma presented an algorithm that uses a for loop to calculate the hamming distance of two sequences.

```python
def hamming_distance(s1, s2):
    """
    Return the Hamming distance between equal-length sequences
    https://en.wikipedia.org/wiki/Hamming_distance#Algorithm_example
    """
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(el1 != el2 for el1, el2 in zip(s1, s2)) 
```

The comprehension on the final line can be written as a multiline loop as follows:

```python
l = []
for el1, el2 in zip(s1, s2):
    l.append(el1 != el2)
sum(l)
```
Here’s a [link](https://gist.github.com/Wytamma/18b76543857b328d4fa25ca377252728) to a gist with more information. 
