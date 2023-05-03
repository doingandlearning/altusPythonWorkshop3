from string import punctuation
from collections import Counter 
from operator import itemgetter 

def top_x_words(text, limit):
  # Clean - removing punctation, lowering case
  cleaned_text = text.translate(str.maketrans("", "", punctuation)).lower()
  # Split it into a list
  split_text = cleaned_text.split()
  # Count the things in the list
  word_frequencies = Counter(split_text)
  # return the array of tuples
  return sorted(word_frequencies.items(), key=itemgetter(1), reverse=True)[:limit]


text = "!@#!@#!@#!@#!@{}[]\%$#%Functional programming is a programming paradigm that treats computation as the evaluation of mathematical functions and avoids changing state and mutable data. It is a declarative programming paradigm, which means programming is done with expressions or declarations instead of statements."
top_x = 5

print(top_x_words(text, top_x))

def top_x_words(text,text_x):
    counts = dict()
    words = text.strip().split(' ')

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return sorted(counts.items())
print(top_x_words(text, top_x))

