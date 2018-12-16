from random import shuffle

def read_file():
    wordlist=[]
    for line in open("input.txt"):
        wordlist.append(line.split("\n")[0])
    
    return wordlist

wordlist = read_file()

jumbled_list = wordlist[:]

shuffle(jumbled_list)
print jumbled_list
