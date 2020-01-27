import requests

right =  [0,1,0,0,0]
right_run = [0,1,0,1,0]
right_jump = [0,1,0,0,1]
right_jump_run = [0,1,0,1,1]
left = [1,0,0,0,0]
left_run = [1,0,0,1,0]
left_jump = [1,0,0,0,1]
left_jump_run = [1,0,0,1,1]
all_actions = [right, right_run, right_jump, right_jump_run, left, left_run, left_jump, left_jump_run]

class Client:

    def __init__(self):
        self.tensor_action_map =  {0: right, 1:right_run, 2:right_jump, 3:right_jump_run, 4:left, 5:left_run, 6:left_jump, 7:left_jump_run}
        self.API_ENDPOINT = "http://localhost:8080"
        self.init_endpoint = self.API_ENDPOINT + "/init"
        self.action_endpoint = self.API_ENDPOINT + "/action"
        self.init_data = {    
                        "visual": True,
                        "scale": 2.0,
                        "marioState": 0,
                        "fps": 30,
                        "timer": 200
                        }
    
    def init_env(self):
        r = requests.post(url = self.init_endpoint, json = self.init_data)
        frame = r.json()["frame"]
        alive = r.json()["alive"]
        return (frame, alive)

    def step(self, action):
        r = requests.post(url = self.action_endpoint, json = self.tensor_to_action(action))
        frame = r.json()["state"]["frame"]
        reward = r.json()["reward"]["reward"]
        alive = r.json()["state"]["alive"]
        return (frame, reward, alive)

    def tensor_to_action(self, action):
        list_action = action.tolist()
        return self.tensor_action_map[list_action[0][0]]
