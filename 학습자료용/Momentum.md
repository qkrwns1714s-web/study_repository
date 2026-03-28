#word #math 
$$v_t = \gamma \cdot v_{t-1} + g_t$$
$$W_{t+1} = W_t - \alpha \cdot v_t$$

optimizer model which change velocity take $\gamma$ into account.
so if $\gamma$ is 0.9, Learning_rate can multyply ten.