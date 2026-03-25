# 오늘 배운 내용

# PyTorch

make faster in Matrix calculator in GPU

` python -m pip install torch ` : install torch by terminal

` torch.tensor(encoded) ` : make encoded list to tensor
` ex_tensor.tolist() ` : make tensor to list
` ex_tensor.shape ` : tensor dimention
` ex_tensor.dtype` : Data type of tensor
` torch.stack([t1, t2, t3, t4]) ` : batching torch [4, ..]
` torch.randint(max_range, (extract_num,)) ` : make random int list in max_range, [1, extact_num]
` torch.multinomial(percents, ex_number) : ` make a roulette, and choice ex_number. 
` torch.cat((list_1, list_2), dimention) : ` concatenate list_1 and list_2, and dim = 0, it will be Height, dim = 1, it add width.
` torch.zeros((B, T), dtype = torch.long) ` : make (B, T) tensor filled with zero.(Pytorch using only torch.long or torch.int64)

## torch.nn : Neural Network
` nn.model ` : inherence in class
` super().__init__()` : setting for Pytorch
` nn.embedding(vocab_size, dimention)` : make 32 dataset to record
` nn.linear(dimention, vocab_size)` : setting Weight and bias, prepare to calculate the Logits
` ex_logits.view(B*T, C) ` : make \[B]\[T]\[C] to \[BT]\[C] 
` self(encoded_num)` : doing Hook, \_\_call\_\_, and run forward. 

### torch.nn.functional
` F.cross_entropy(logits, targets) ` : using [[Softmax]] and [[Negative Log-Likelihood]] for all logits 
` F.softmax(logits, dimention)` : softmax in all logits, if dimention is -1, it mean last dimention in logits.

# Method

Ability which datatype have.
`datatype.method()`



