# Lab: Hash Tables – Ransom Note Construction  
**Completed Sept 30, 3036**

<br>

## Overview
A Python function that determines whether a ransom note can be built using the letters from a magazine, where each letter in the magazine can only be used once.

## How It Works

The function `can_construct(ransomNote, magazine)` in `ransom_note.py` uses a **hash table (dictionary)** to solve the problem in three steps:

1. **Count the magazine letters.** It loops through the magazine and builds a dictionary of letter counts, e.g. `"aab"` → `{'a': 2, 'b': 1}`.
2. **Check the note against the counts.** It loops through the ransom note one letter at a time. If a letter is missing from the dictionary or its count has reached 0, it returns `False` immediately. Otherwise, it decrements that letter's count by 1.
3. **Return the result.** If every letter in the note is found, it returns `True`.

Using a dictionary makes each lookup fast, so the function runs in O(n + m) time, where n and m are the lengths of the note and magazine.

### Examples

```python
can_construct("treasure", "the rare stones were hidden under a tree")            # True
can_construct("coffee", "a cup of hot tea")                                      # False (only has one f)
can_construct("moonlight", "the old lighthouse glowed under the moon at night")  # True
```

## Project Files

- `ransom_note.py` – the `can_construct` function
- `test_ransom_note.py` – test cases that check the function's output
- `.gitignore` – excludes `__pycache__` and `.pyc` files

## Setup

Requires Python 3.

1. Clone the repository:
```
   git clone https://github.com/hanjennings1/hash-table-ransom-note-lab.git
```
2. Move into the project folder:
```
   cd hash-table-ransom-note-lab
```

## Running the Tests

```
python test_ransom_note.py
```

If all tests pass, the final line of output will be `🎉 All tests passed!`