def count_deletions(S):
    letter_counts = {}
    
    # Count the occurrences of each letter using a dictionary
    
    for char in S:
        letter_counts[char] = letter_counts.get(char, 0) + 1
    
    deletions = sum(count % 2 != 0 for count in letter_counts.values())
    return deletions


print(count_deletions("acbcbba"))  
print(count_deletions("axxaxa"))  
print(count_deletions("aaaa"))

def reverse_words(S):
    # Split the input string into words,
    #  reverse each word, 
    # join them back into a string
    reversed_words = ' '.join(word[::-1] for word in S.split())
    return reversed_words

reversed_string = reverse_words("we test coders")
print(reversed_string) 
