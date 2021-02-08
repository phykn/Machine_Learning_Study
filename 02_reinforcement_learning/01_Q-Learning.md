### Q-Learning
#####  | Q-Learning algorithm [1]

$$
Q(s_{t}, a_{t}) \leftarrow (1-\alpha) \cdot \underbrace{Q(s_{t}, a_{t})}_{\mathrm{old\;value}}+\underbrace{\alpha}_{\mathrm{learning\;rate}} \cdot \left( \overbrace{ \underbrace{r_{t}}_{\mathrm{reward}} + \underbrace{\gamma}_{\mathrm{discount\;factor}} \cdot \underbrace{\underset{a_{t+1}}{\rm{max}} Q(s_{t+1}, a_{t+1})}_{\mathrm{estimate\;of\;optimal\;future\;value}} }^{\mathrm{learned\;value}} \right )
$$

![](https://latex.codecogs.com/gif.latex?s_{t})
| Term                                             | Description                                                  |
| :----------------------------------------------- | :----------------------------------------------------------- |
| <img src="https://render.githubusercontent.com/render/math?math=s_{t}"> | 시간 <img src="https://render.githubusercontent.com/render/math?math=t"> 에서 상태 (state) |
| <img src="https://render.githubusercontent.com/render/math?math=a_{t}"> | 시간 <img src="https://render.githubusercontent.com/render/math?math=t"> 에서 행동 (action) |
| <img src="https://render.githubusercontent.com/render/math?math=Q(s_{t}, a_{t})"> | 주어진 상태 <img src="https://render.githubusercontent.com/render/math?math=s_{t}"> 에서 행동 <img src="https://render.githubusercontent.com/render/math?math=a_{t}"> 의 기대 Return (Reward) |
| <img src="https://render.githubusercontent.com/render/math?math=\alpha"> | 학습률 <img src="https://render.githubusercontent.com/render/math?math=(0 < \alpha \leqq 1)"> |
| <img src="https://render.githubusercontent.com/render/math?math=r_{t}"> | <img src="https://render.githubusercontent.com/render/math?math=a_{t}"> 에 의한 보상 |
| <img src="https://render.githubusercontent.com/render/math?math=\gamma"> | 보상의 감소율 <img src="https://render.githubusercontent.com/render/math?math=(0 \leqq \gamma \leqq 1)"> |
| <img src="https://render.githubusercontent.com/render/math?math=\underset{a_{t+1}}{\rm{max}}Q(s_{t+1},a_{t+1})"> | <img src="https://render.githubusercontent.com/render/math?math=Q"> 가 최대가 되는 <img src="https://render.githubusercontent.com/render/math?math=a_{t + 1}"> 을 선택 (Greedy action) |



#####  | $\epsilon-$greedy 
새로운 행동을 찾기 위한 무작위 선택 $(0 \leqq \epsilon \leqq 1)$
https://latex.codecogs.com/gif.latex?%280%20%5Cleqq%20%5Cepsilon%20%5Cleqq%201%29


##### | Markov Decision Process
> Property (Policy)
$$
P(a_{t+1}|s_{t}, a_{t}, s_{t+1})=P(a_{t+1}|s_{t+1})
$$
> Property (Transition probability)
$$
P(s_{t+2}|s_{t}, a_{t}, s_{t+1}, a_{t+1})=P(s_{t+2}|s_{t+1}, a_{t+1})
$$



##### | Return: Sum of rewards

$$
\begin{aligned}
G_{t} & \triangleq R_{t} + \gamma R_{t+1} + \gamma^{2} R_{t+2} \\
& = \sum_{n=0}^{\infty} \gamma^{n} R_{t+n}
\end{aligned}
$$

### Reference
[1] https://ko.wikipedia.org/wiki/Q_%EB%9F%AC%EB%8B%9D
[2]  https://www.youtube.com/channel/UCcbPAIfCa4q0x7x8yFXmBag
