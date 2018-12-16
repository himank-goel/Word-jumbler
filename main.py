from random import shuffle


def read_file():
    wordlist = []
    for line in open("input.txt"):
        wordlist.append(line.split("\n")[0])

    return wordlist


wordlist = read_file()

jumbled_list = wordlist[:]
shuffle(jumbled_list)

output_dict = {}

for word in jumbled_list:
    definition = raw_input(word + " ")
    type(definition)
    output_dict[word] = definition
    # print output_dict

f = open("output.txt", "w+")

for word in wordlist:
    f.write("%s - %s\n" % (word, output_dict[word]))
    # print output_dict[word]

# print jumbled_list
