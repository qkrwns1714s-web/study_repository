import torch
import torch.nn as nn
import torch.nn.functional as F
from Tensor import SimpleDataLoader
from tokenizer import SimpleTokenizer

class BigramlanguageModel(nn.Module):
    def __init__(self, vocab_size, dimention):
        super().__init__()
        self.token_embedding_table = nn.Embedding(vocab_size, dimention)
        self.lm_head = nn.Linear(dimention, vocab_size)

    def forward(self, index, targets = None):
        question = self.token_embedding_table(index)
        logits = self.lm_head(question)
        
        if targets is None:
            loss = None
        else:
            B, T, C = logits.shape
            logits = logits.view(B*T, C)
            targets = targets.view(B*T)
            
            loss = F.cross_entropy(logits, targets)
        return logits, loss

    def generate(self, encoded_num, max_new_tokens):
        for _ in range(max_new_tokens):
            logits, loss = self(encoded_num)
            logits = logits[:, -1, :] 
            probs = F.softmax(logits, dim=-1)
            num_next = torch.multinomial(probs, num_samples=1)
            encoded_num = torch.cat((encoded_num, num_next), dim=1)
        return encoded_num

if __name__ == "__main__":
    # make_data
    text = "hello world! this is my first llm. AI is fun"
    tokenizer = SimpleTokenizer(text)
    data = torch.tensor(tokenizer.encode(text))

    # batching
    loader = SimpleDataLoader(data, batch_size = 4, block_size = 8)
    question, answer = loader.get_batch()

    vocab_size = len(tokenizer.vocab)
    dimention = 32

    #make model
    model = BigramlanguageModel(vocab_size, dimention)
    context = torch.zeros((1, 1), dtype=torch.long)
    generated_indices = model.generate(context, max_new_tokens=100)
    result_list = generated_indices[0].tolist()
    print(tokenizer.decode(result_list))
