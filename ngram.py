import random

def generate_text(input_string,n=2,length=10):
    #split input string into a list of words
    words=input_string.split()

#create a dictionary to store n-grams and their frequency counts 
   
    ngrams={}
    for i in range(len(words) - n):
        gram=' '.join(words[i:i+n])
        if gram not in ngrams:
            ngrams[gram]=[]
            ngrams[gram].append(words[i+n])

#generate text by starting with a rando n-gram and choosing the next word based on the frequency count
            
    current_gram=random.choice(list(ngrams.keys()))
    result=current_gram
    for i in range(length):
        if current_gram not in ngrams:
            break
        next_word=random.choice(ngrams[current_gram])
        result+=' '+next_word
        current_gram=' '.join(result.split())[-n:]
        
    return result
input_string= input("enter the input string: ")
generated_text= generate_text(input_string)
print(generated_text)
