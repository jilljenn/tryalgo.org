---
layout: en
title: Deep Reinforcement Learning
author: Jill-Jênn Vie
---

Stable Baselines rely on TF 1.x but Stable Baselines v3 rely on PyTorch.

- Breakout v4 and v5 are in the [Atari Learning Environment](https://github.com/mgbellemare/Arcade-Learning-Environment) (`ale-py`)
- There exists a [MinAtar environment](https://github.com/kenjyoung/MinAtar) that is 10x faster to train than the original Breakout (mini Atari). [I fixed it in a fork](https://github.com/jilljenn/MinAtar) so that Stable Baselines v3 can be used.
- [DQN](https://stable-baselines3.readthedocs.io/en/master/modules/dqn.html) of stable-baselines
- [Actor-Critic A2C](https://stable-baselines3.readthedocs.io/en/master/modules/a2c.html) of stable-baselines
- Actor-Critic is [very sensitive to hyper-parameter](https://araffin.github.io/post/sb3/)

## Benchmarks

- [Best models on Breakout-v5](https://wandb.ai/costa-huang/cleanRL/reports/Breakout-v5--VmlldzoxNDI1MTIx) using [CleanRL](https://github.com/vwxyzjn/cleanrl) thanks to this [Reddit post](https://www.reddit.com/r/reinforcementlearning/comments/smjhhx/which_algorithm_has_the_shortest_training_time_in/)
- [Extra features of DQN](https://ai.googleblog.com/2021/07/reducing-computational-cost-of-deep.html), notably Rainbow
- [Yet another benchmark](https://github.com/ShangtongZhang/DeepRL)

![](https://raw.githubusercontent.com/ShangtongZhang/DeepRL/master/images/Breakout.png)

Best model from CleanRL:

    ppo_atari_envpool.py --exp-name a2c --update-epochs 1 --num-minibatches 1 --norm-adv False --num-envs 64 --clip-vloss False --vf-coef 0.25 --anneal-lr False --num-steps 5 --track.

## Fun fact

- Running on my CPU was faster than Colab GPU (for the MinAtar environment), possibly because the data was not high dimensional and the network was not very deep
