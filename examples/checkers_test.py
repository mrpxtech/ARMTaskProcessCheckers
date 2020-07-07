import seoulai_gym as gym
from seoulai_gym.envs.checkers.agents import RandomAgentLight
from seoulai_gym.envs.checkers.agents import RandomAgentDark
import time


def main():
    env = gym.make("Checkers")

    a1 = RandomAgentLight()
    a2 = RandomAgentDark()

    obs = env.reset()
    current_agent = a1
    next_agent = a2
    
    # timer = 0
    # while timer < 2000:
    #     env.render()
    #     timer+=1

    while True:
        from_row, from_col, to_row, to_col = current_agent.act(obs)
        obs, rew, done, info = env.step(current_agent, from_row, from_col, to_row, to_col)
        current_agent.consume(obs, rew, done)
        env.render()
        time.sleep(.1) #time delay
        print(f"Rewards:{rew} by: {current_agent}")

        if done:
            print(f"Game over! {current_agent} agent wins.")
            obs = env.reset()

        # switch agents
        temporary_agent = current_agent
        current_agent = next_agent
        next_agent = temporary_agent


    env.close()


if __name__ == "__main__":
    main()