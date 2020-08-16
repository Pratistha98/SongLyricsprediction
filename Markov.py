import random
import sys 
import os
import webbrowser
from webbrowser import open_new_tab
from newspaper import Article
import nltk


class Markov:
    def __init__(self, step=1):
        self._step = step

 # getter method
    def get_step(self):
      return self._step

# setter method
    def set_step(self,a):
        self._year = a 

    def markov_generator(self, start, rule, step):    
        keys = list(rule.keys())
        random_key = start
        final_string = random_key
        prob = {}
        if random_key in keys: 
             total = (len(rule[random_key]))
             #find the count of each 
             #print(rule[random_key])
             for value in rule[random_key]:
                 if value in prob:
                     prob[value] +=1
                 else: 
                    prob[value] = 1
            #got the probability
             for key, value in prob.items():
                prob[key] = round((value/total), 2)
             counter = 0 
             for key, value in prob.items():
                 if value > 0.05:
                     print("Text predicted: ", key)
                     counter +=1
                     #return True
                 else: 
                     continue
             if counter >= 1:
                 return True
             else : 
                 return False
        else:
            return False

    def create_bigram(self,s, step):
        words = s.split()
        d = {}
        #step = 2 # step is 2 because its a bigram
        for i in range(len(words)- step):
            c = words[i+step] # grab the word following a pair
            pair = ' '.join(words[i:i+step])
            # add that word to the dictionary
            if pair in d:
                d[pair].append(c)
            else:
                d[pair] = [c] 
        # for (key, value) in d.items():
        #     print(key, ": ", value)
        return d 

url_array = []
#Get the file name, length from the User 
text_file = "input.txt"
url1 = input("Enter the first URL: ")
url2 = input("Enter the second URL: ")
start = input("Enter a text to start: ")
print("\n")
#make a new file to write 

url_array.append(url1)
url_array.append(url2)
#url_array.append(url3)

file = open(text_file, "w+")
nltk.download('punkt')
for i in range(len(url_array)):

    article = Article(url_array[i], language="en")
    article.download()
    article.parse()
    article.nlp()
    #download and parse perform NLP 
    if(i == 0):
        file.write(article.text)
    else:
        file = open(text_file, "a")
        file.write(article.text)

file = open(text_file, "w+")
line = file.read().replace("\n", " ")
file.close()
# create objects
m1 = Markov()
step = m1.get_step()
rule = m1.create_bigram(line, step) 
filename = "output2.txt"
outFile = open(filename,'w')
# outFile.write(start + " ")
try:
    while True:
        outFile = open(filename,'a+')
        print("Start",  start)
        to_write = m1.markov_generator(start, rule, step)
        if (to_write):
            start_space =  start + " "
            outFile.write(start_space)
            print("\n")
            start = input("Enter among the predicted word or enter any word: ")
            print("\n")
            continue
          
        else: 
            second = input("Pick another word: ")
            print("\n")
            start = second
            continue
except KeyboardInterrupt:
    pass

outFile.close()



# https://www.azlyrics.com/lyrics/eminem/notafraid.html
# https://www.azlyrics.com/lyrics/eminem/therealslimshady.html
