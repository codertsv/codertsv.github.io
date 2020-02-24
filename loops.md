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

## Bash 
Chloë presented a loop where she uses [trimmomatic](http://www.usadellab.org/cms/?page=trimmomatic) to trim her read adapters from her multiple fasta files.

```bash
for i in *_R1.fastq.gz #any file that ends with 
do
filename=`echo $i|cut -c 1-3` #for output use a substring to just cut first 3 characters
echo $filename
  trimmomatic SE -phred33 -threads 10 \ 
  $i \
  ${filename}_trimmed.fastq.gz \
  ILLUMINACLIP:TruSeq3-SE:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36 #settings from example TruSeq, should adapt for your specific run
done

echo "Trimming reads like a baller" #because
```

Bash uses 'do' and 'done' like R uses parentheses {} and python uses white space :)
If you want to try a bash loop there's a tutorial [here](https://linuxize.com/post/bash-for-loop/).
