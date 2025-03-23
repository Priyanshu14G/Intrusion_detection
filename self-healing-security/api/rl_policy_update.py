import numpy as np
import gym
from gym import spaces

class FirewallEnv(gym.Env):
    """Reinforcement Learning Environment for Dynamic Firewall Policy."""
    def __init__(self):
        super(FirewallEnv, self).__init__()
        self.action_space = spaces.Discrete(2)  # 0: No action, 1: Block IP
        self.observation_space = spaces.Box(low=0, high=1, shape=(1,), dtype=np.float32)

    def reset(self):
        self.state = np.array([0.5])  # Initial traffic state
        return self.state

    def step(self, action):
        reward = 0
        if action == 1:  # Block IP
            reward = self.evaluate_threat()
        self.state = np.random.random(1)
        done = False
        return self.state, reward, done, {}

    def evaluate_threat(self):
        """Simulate threat evaluation."""
        return np.random.choice([1, -1])  # Reward or penalty

# RL Training - Q-Learning
def train_rl_policy():
    env = FirewallEnv()
    q_table = np.zeros([env.observation_space.shape[0], env.action_space.n])
    learning_rate = 0.1
    discount_factor = 0.95
    episodes = 1000

    for _ in range(episodes):
        state = env.reset()
        for _ in range(100):
            action = np.argmax(q_table[state]) if np.random.rand() > 0.1 else env.action_space.sample()
            next_state, reward, _, _ = env.step(action)
            q_table[state, action] += learning_rate * (reward + discount_factor * np.max(q_table[next_state]) - q_table[state, action])
            state = next_state
    print("✅ RL Policy Training Complete!")
