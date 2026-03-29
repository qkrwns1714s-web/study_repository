#word #math
make difference in all Weight.
So if $g_t$ is big, Learning rate is smaller.


ROOT + Mean + Squere.

Calculrate $g_t{^2}$ [[EMA]]
$$s_t = \beta_2 \cdot s_{t-1} + (1 - \beta_2) \cdot g_t^2$$
if $\beta$ = 0.9, it can be multyply ten.



$$W_{t+1} = W_t - \frac{\alpha}{\sqrt{s_t} + \epsilon} \cdot g_t$$
