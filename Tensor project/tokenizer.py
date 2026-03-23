class SimpleTokenizer:
    def __init__(self, text):
        self.vocab = set(text)
        self.sorted_vocab = sorted(self.vocab)
        #make stoi and itos
        self.stoi = {}
        for index, value in enumerate(self.sorted_vocab):
            self.stoi[value] = index
        self.itos = self.sorted_vocab

    #make encode, decode functions
    def encode(self, insert_text):
        return [self.stoi[character] for character in insert_text]

    def decode(self, insert_num):
        return "".join([self.itos[to_change_num] for to_change_num in insert_num])


if __name__ == "__main__":
    #print
    test_tokenizer = SimpleTokenizer("Hello world")
    print(test_tokenizer.sorted_vocab)
    print(test_tokenizer.encode("world"), test_tokenizer.decode([7, 5, 6, 4, 1]))
