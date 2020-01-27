import DQNAgent
import torch

BATCH_SIZE = 128
GAMMA = 0.999
EPS_START = 0.9
EPS_END = 0.05
EPS_DECAY = 200
TARGET_UPDATE = 10
screen_width = 256
screen_height = 240
num_episodes = 50

agent = DQNAgent.DQNAgent(BATCH_SIZE, GAMMA, EPS_START, EPS_END, EPS_DECAY, TARGET_UPDATE, num_episodes, screen_height, screen_width)
agent.train()

tens = torch.randn((1,1,240,256))
#print(tens)

replace = torch.ones(240, 256)

tens[0][0] = replace

#print(tens[0][0])
#print(tens)
