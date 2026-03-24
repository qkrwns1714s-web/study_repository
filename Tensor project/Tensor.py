import torch

class SimpleDataLoader:
    def __init__(self, data_tensor, batch_size, block_size):
        self.data = data_tensor
        self.batch_size = batch_size
        self.block_size = block_size

    def get_batch(self):
        random_start_point_list = torch.randint(len(self.data) - self.block_size, (self.batch_size, ))
        question = torch.stack([self.data[i : i+self.block_size] for i in random_start_point_list])
        answer = torch.stack([self.data[i+1 : i+self.block_size+1] for i in random_start_point_list])
        return question, answer

if __name__ == "__main__":
    #make tensor
    from tokenizer import SimpleTokenizer
    text = "hello world! this is my first llm."
    test_tokenizer = SimpleTokenizer(text)
    data = torch.tensor(test_tokenizer.encode(text))

    loader = SimpleDataLoader(data, batch_size = 4, block_size = 8)

    question, answer = loader.get_batch()
    print(question)
    print(answer)
    print(question.shape)
    print(question.dtype)