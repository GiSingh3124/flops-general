import gym
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.distributions import Categorical

# Impostazioni base
learning_rate = 0.001
gamma = 0.99
state_dim = 10      # Dimensione dello stato (sostituiscilo con la tua)
action_dim = 20     # 2 location x 10 modelli (sostituiscilo con il tuo spazio azione)

# Dummy environment (da sostituire con il tuo simulatore)
class DummyOffloadingEnv(gym.Env):
    def __init__(self):
        super(DummyOffloadingEnv, self).__init__()
        self.observation_space = gym.spaces.Box(low=0, high=1, shape=(state_dim,), dtype=np.float32)
        self.action_space = gym.spaces.Discrete(action_dim)

    def reset(self):
        self.state = np.random.rand(state_dim).astype(np.float32)
        return self.state

    def step(self, action):
        next_state = np.random.rand(state_dim).astype(np.float32)
        reward = -np.random.rand()  # simulazione negativa per minimizzazione
        done = np.random.rand() < 0.05
        return next_state, reward, done, {}

# Actor network
class Actor(nn.Module):
    def __init__(self):
        super(Actor, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(state_dim, 128),
            nn.ReLU(),
            nn.Linear(128, action_dim),
            nn.Softmax(dim=-1)
        )

    def forward(self, x):
        return self.fc(x)

# Critic network
class Critic(nn.Module):
    def __init__(self):
        super(Critic, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(state_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 1)
        )

    def forward(self, x):
        return self.fc(x)

# Inizializzazione
env = DummyOffloadingEnv()
actor = Actor()
critic = Critic()
actor_optim = optim.Adam(actor.parameters(), lr=learning_rate)
critic_optim = optim.Adam(critic.parameters(), lr=learning_rate)

# Training loop
num_episodes = 1000

for episode in range(num_episodes):
    state = env.reset()
    done = False
    total_reward = 0
    step_count = 0

    while not done:
        state_tensor = torch.FloatTensor(state)
        probs = actor(state_tensor)
        dist = Categorical(probs)
        action = dist.sample()

        next_state, reward, done, _ = env.step(action.item())
        total_reward += reward
        step_count += 1

        next_state_tensor = torch.FloatTensor(next_state)
        reward_tensor = torch.tensor([reward], dtype=torch.float32)

        # Compute advantage
        value = critic(state_tensor)
        next_value = critic(next_state_tensor).detach()
        advantage = reward_tensor + gamma * next_value * (1 - int(done)) - value

        # Actor loss
        actor_loss = -dist.log_prob(action) * advantage.detach()

        # Critic loss
        critic_loss = advantage.pow(2)

        # Aggiornamento rete attore
        actor_optim.zero_grad()
        actor_loss.backward()
        actor_optim.step()

        # Aggiornamento rete critico
        critic_optim.zero_grad()
        critic_loss.backward()
        critic_optim.step()

        state = next_state

    print(f"Episode {episode + 1:3d} | Total Reward: {total_reward:.3f} | Steps: {step_count}")
