from flask import Flask, request
import numpy as np
import matplotlib.pyplot as plt
import random
import json
import DQN

app = Flask(__name__)
app.debug = True

right =  [0,1,0,0,0]
right_run = [0,1,0,1,0]
right_jump = [0,1,0,0,1]
right_jump_run = [0,1,0,1,1]
left = [1,0,0,0,0]
left_run = [1,0,0,1,0]
left_jump = [1,0,0,0,1]
left_jump_run = [1,0,0,1,1]
all_actions = [right, right_run, right_jump, right_jump_run, left, left_run, left_jump, left_jump_run]

height = 256
width = 240
n_actions = len(all_actions)
n_episodes = 50

#model = Training(height, width, n_actions, n_episodes)


@app.route("/", methods=["POST"])
def action():
    frame = request.get_json()
    
    matrix = np.array(frame["frame"])
    reward = frame["reward"]
    print(matrix.shape, reward)
    
    #save_image(matrix)
    #model.train(matrix, reward, )
    response = json.dumps(random_action())
    #print(response)
    return json.dumps(left)


def save_image(matrix):
    plt.imshow(matrix, cmap="gray")
    plt.show()
    plt.savefig("mario.png")


def random_action():
    return random.choice(all_actions)

if __name__ == "__main__":
    app.run(debug=True)


