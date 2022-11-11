import gym

# making the environment:
env = gym.make("CartPole-v1")

for i in range(10):
    # initializing the environment:
    env.reset()
    done = False
    episode_reward = 0

    while not done:
        # choose a random action:
        new_observation, reward, done, info = env.step(env.action_space.sample())
        # render the environment:
        env.render(mode="human")
        # counting games:
        episode_reward += reward
        print("reward: ", reward)

    print("total reward of the game: ", episode_reward)
    print("---------------")
    if i == 9:
        break
    print("Episode: ", i+2)
