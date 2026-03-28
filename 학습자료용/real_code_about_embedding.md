#avatar 

```
import torch
import torch.nn as nn
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

            import torch.nn.functional as F
            loss = F.cross_entropy(logits, targets)
        return logits, loss

  
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
```
