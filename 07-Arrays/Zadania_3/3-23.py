text = "An apple a day keeps the doctor away"

def number(text):
    words = text.split()
    
    return len(words)


def ordered(text):
    words = text.split()
    sorted_words = []
    
    while words:
        longest = words[0]
        for x in words:
            if len(x) > len(longest):
                longest = x
        sorted_words.append(longest)
        words.remove(longest)
    
    return sorted_words


def alphabetically(text):
    words = text.split()
    sorted_words = []

    while words:
        smallest = words[0]

        for x in words:
            if x.lower() < smallest.lower():
                smallest = x
        sorted_words.append(smallest)
        words.remove(smallest)
        
    return sorted_words



print(f"Text: {text}")
print(f"Number of words: {number(text)}")
print(f"Words from the longest: {', '.join(ordered(text))}")
print(f"Words ordered alphabetically: {', '.join(alphabetically(text))}")