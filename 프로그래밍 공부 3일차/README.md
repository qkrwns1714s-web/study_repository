# 오늘 배운 내용

## Embedding

make tenser on coordinate

## Logits

possibility which word can Correct

## Linear

get question and out logits.

## Channel

dimention number which contain feature

## Bigram

Bi(two) + Gram(word)

Predict the next word using only the word preceding.

## class

` def __init__(self, ex_num):` : reset function
` class ex_class(ex_inheritence_class): ` : inheritence another class
` super() ` : indicate parents class

## torch.nn : Neural Network
` nn.model ` : inherence in class
` super().__init__()` : setting for Pytorch
` nn.embedding(vocab_size, dimention)` : make 32 dataset to record
` nn.linear(dimention, vocab_size)` : setting Weight and bias, prepare to calculate the Logits
` ex_logits.view(B*T, C) ` : make \[B]\[T]\[C] to \[BT]\[C] 

### torch.nn.functional
` F.cross_entropy(logits, targets) ` : using [[Softmax]] and [[Negative Log-Likelihood]] for all logits 

## Softmax

make logit to percent

make ${z_i}$ to ${e^{z_i}}$ , so it emphasize big logit, and all results are > 0

$$p_i = \frac{e^{z_i}}{\sum_{j} e^{z_j}}$$

## markdown
language which is Easy to use, using text or documents.

using in GitHub, Notion, Discord, Jupyter Notebook..

many markdown platform also provide LaTeX Language.

## LaTeX

complecated language which is using in mathmatics.

## Negative Log-Likelihood

NLL

get Loss more if target is close to zero
$$L = -log(P_{target})$$

## Loss

diffenciation between question and answer.