#avatar 
  
```
batch_size = 4;
block_size = 8;

  
  
def get_batch():
    random_start_point_list = torch.randint(len(data) - block_size, (batch_size, ))
    question = torch.stack([data[i : i+block_size] for i in random_start_point_list])
    answer = torch.stack([data[i+1 : i+block_size+1] for i in random_start_point_list])
    return question, answer

  

if __name__ == "__main__":
    question, answer = get_batch()
    print(question)
    print(answer)
    print(question.shape)
    print(question.dtype)
    
```
