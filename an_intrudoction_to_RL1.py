import gym
import time

# creating the environment:
env = gym.make("CartPole-v1")

# initializing the environment:
env.reset()


# playing the game randomly for 10 times:
for i in range(250):
    # choose and play a random action
    env.step(env.action_space.sample())
    # showing the action
    env.render(mode="human")
    #time.sleep(1)

# closing the environment:
env.close()