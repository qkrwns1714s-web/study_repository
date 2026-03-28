#avatar ```
```
import torch
from tokenizer import SimpleTokenizer



text = "hello world! this is my first llm."
test_tokenizer = SimpleTokenizer(text)

  

#make tensor
data = torch.tensor(test_tokenizer.encode(text))

  

if __name__ == "__main__":
    print("all data : ", data)
    print("data length : ", data.shape)
    print("data type : ", data.dtype)
    
```
