#sort_text
text = "hello world"
vocab = set(text)
sorted_vocab = sorted(vocab)

#make stoi and itos
stoi = {}
for index, value in enumerate(sorted_vocab):
    stoi[value] = index
itos = sorted_vocab

#make encode, decode functions
def encode(insert_text):
    return [stoi[character] for character in insert_text]

def decode(insert_num):
    return "".join([itos[to_change_num] for to_change_num in insert_num])

#print
print(sorted_vocab)
print(encode("world"), decode([7, 5, 6, 4, 1]))
