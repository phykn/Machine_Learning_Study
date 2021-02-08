### Q-Learning
#####  | Q-Learning algorithm [1]

![](https://latex.codecogs.com/gif.latex?Q%28s_%7Bt%7D%2C%20a_%7Bt%7D%29%20%5Cleftarrow%20%281-%5Calpha%29%20%5Ccdot%20%5Cunderbrace%7BQ%28s_%7Bt%7D%2C%20a_%7Bt%7D%29%7D_%7B%5Cmathrm%7Bold%5C%3Bvalue%7D%7D&plus;%5Cunderbrace%7B%5Calpha%7D_%7B%5Cmathrm%7Blearning%5C%3Brate%7D%7D%20%5Ccdot%20%5Cleft%28%20%5Coverbrace%7B%20%5Cunderbrace%7Br_%7Bt%7D%7D_%7B%5Cmathrm%7Breward%7D%7D%20&plus;%20%5Cunderbrace%7B%5Cgamma%7D_%7B%5Cmathrm%7Bdiscount%5C%3Bfactor%7D%7D%20%5Ccdot%20%5Cunderbrace%7B%5Cunderset%7Ba_%7Bt&plus;1%7D%7D%7B%5Crm%7Bmax%7D%7D%20Q%28s_%7Bt&plus;1%7D%2C%20a_%7Bt&plus;1%7D%29%7D_%7B%5Cmathrm%7Bestimate%5C%3Bof%5C%3Boptimal%5C%3Bfuture%5C%3Bvalue%7D%7D%20%7D%5E%7B%5Cmathrm%7Blearned%5C%3Bvalue%7D%7D%20%5Cright%20%29)

| Term                                                         | Description                                                  |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| ![](https://latex.codecogs.com/gif.latex?s_{t})              | 시간 ![](https://latex.codecogs.com/gif.latex?t) 에서 상태 (state) |
| ![](https://latex.codecogs.com/gif.latex?a_{t})              | 시간 ![](https://latex.codecogs.com/gif.latex?t) 에서 행동 (action) |
| ![](https://latex.codecogs.com/gif.latex?Q(s_{t},%20a_{t}))  | 주어진 상태 ![](https://latex.codecogs.com/gif.latex?s_{t}) 에서 행동 ![](https://latex.codecogs.com/gif.latex?a_{t}) 의 기대 Return (Reward) |
| ![](https://latex.codecogs.com/gif.latex?\alpha)             | 학습률 ![](https://latex.codecogs.com/gif.latex?%280%20%3C%20%5Calpha%20%5Cleqq%201%29) |
| ![](https://latex.codecogs.com/gif.latex?r_{t})              | ![](https://latex.codecogs.com/gif.latex?a_{t}) 에 의한 보상 |
| ![](https://latex.codecogs.com/gif.latex?\gamma)             | 보상의 감소율 ![](https://latex.codecogs.com/gif.latex?%280%20%5Cleqq%20%5Cgamma%20%5Cleqq%201%29) |
| ![](https://latex.codecogs.com/gif.latex?\underset{a_{t+1}}{\rm{max}}Q(s_{t+1},a_{t+1})) | ![](https://latex.codecogs.com/gif.latex?Q) 가 최대가 되는 ![](https://latex.codecogs.com/gif.latex?a_{t+1}) 을 선택 (Greedy action) |



#####  | ![](https://latex.codecogs.com/gif.latex?\epsilon-greedy )
새로운 행동을 찾기 위한 무작위 선택 ![](https://latex.codecogs.com/gif.latex?%280%20%5Cleqq%20%5Cepsilon%20%5Cleqq%201%29)



##### | Markov Decision Process
> Property (Policy)
![](https://latex.codecogs.com/gif.latex?P%28a_%7Bt&plus;1%7D%7Cs_%7Bt%7D%2C%20a_%7Bt%7D%2C%20s_%7Bt&plus;1%7D%29%3DP%28a_%7Bt&plus;1%7D%7Cs_%7Bt&plus;1%7D%29)

> Property (Transition probability)
![](https://latex.codecogs.com/gif.latex?P%28s_%7Bt&plus;2%7D%7Cs_%7Bt%7D%2C%20a_%7Bt%7D%2C%20s_%7Bt&plus;1%7D%2C%20a_%7Bt&plus;1%7D%29%3DP%28s_%7Bt&plus;2%7D%7Cs_%7Bt&plus;1%7D%2C%20a_%7Bt&plus;1%7D%29)



##### | Return: Sum of rewards

![](https://latex.codecogs.com/gif.latex?%5Cbegin%7Baligned%7D%20G_%7Bt%7D%20%26%20%5Ctriangleq%20R_%7Bt%7D%20&plus;%20%5Cgamma%20R_%7Bt&plus;1%7D%20&plus;%20%5Cgamma%5E%7B2%7D%20R_%7Bt&plus;2%7D%20%5C%5C%20%26%20%3D%20%5Csum_%7Bn%3D0%7D%5E%7B%5Cinfty%7D%20%5Cgamma%5E%7Bn%7D%20R_%7Bt&plus;n%7D%20%5Cend%7Baligned%7D)

### Reference
[1] https://ko.wikipedia.org/wiki/Q_%EB%9F%AC%EB%8B%9D
[2]  https://www.youtube.com/channel/UCcbPAIfCa4q0x7x8yFXmBag
