def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Determines if ransomNote can be constructed using letters from magazine.
    Each letter in magazine can only be used once.

    Parameters:
        ransomNote (str): The target string to construct.
        magazine (str): The source string with available characters.

    Returns:
        bool: True if ransomNote can be constructed, False otherwise.
    """

    # Build a hash table/dictionary of letter counts from magazine
    letter_counts ={}                   # empty dict: letter -> count
    for char in magazine:               # loop through each character
        if char in letter_counts:       # check if a new letter:
            letter_counts[char] += 1    # yes (seen before): add 1 to its count
        else:
            letter_counts[char] = 1     # no (new letter): add it with a count of 1

    # Check each letter of the note against the magazine's count:
    for char in ransomNote:                               # loop through each note character
        if char not in letter_counts or letter_counts[char] == 0:   # missing or used up:
            return False                                  # can't build the note, stop now
        letter_counts[char] -= 1                          # use one copy of this letter