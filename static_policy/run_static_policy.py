#
# School of Continuing Studies, University of Toronto
# 3547 TERM PROJECT
# Intelligent Systems and Reinforcement Learning
# Robot obstacle avoidance with reinforcement learning
#
# Alexandre Dietrich
# Ankur Tyagi
# Haitham Alamri
# Rodolfo Vasconcelos
#

'''
Run the robot in episodes and show the performance in a graph
'''

import math
import random
import sys
sys.path.insert(0,'..')
import constants
import obavd3
import matplotlib.pyplot as plt
from matplotlib import gridspec
import episodes

# run one episode. Stops when reaches an end state or the max number the steps is reached
def play_episode(robot_pos, goal_pos, full_obstacle_list):
    robot_co = 1

    start_pos = robot_pos.copy()
    print (f"start_pos={start_pos}")
    print (f"robot_pos={robot_pos}")
    print (f"goal_pos={goal_pos}")
    print (f"full_obstacle_list={full_obstacle_list}")

    #create robot
    r1 = obavd3.Robot(robot_pos.copy(), robot_co, constants.N_SENSOR, goal_pos)

    print("000000000000000000000000000000000000000000")
    print("000000000000000000000000000000000000000000")
    print("Playing episode for Reinforcement Learning Robot")
    print("000000000000000000000000000000000000000000")
    print("000000000000000000000000000000000000000000")

    step_number1 = 1
    hit_obstcle1, reach_goal1 = False, False
    # Experiment 1
    while (hit_obstcle1 == False and reach_goal1 == False):
        print("")

        print (f"start_pos={start_pos}")
        print (f"robot_pos={robot_pos}")
        print (f"goal_pos={goal_pos}")
        print (f"full_obstacle_list={full_obstacle_list}")

        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("")
        print(f"step_number={step_number1}")
        hit_obstcle1, reach_goal1 = r1.update(full_obstacle_list, goal_pos) 
        step_number1 += 1
        if step_number1 > 200:
            hit_obstcle1 = True
            reach_goal1 = False
            print(f"Too many steps, it will probably take too long to end")
            break
    print(f"Completed in {step_number1} steps")
    
    print (f"start_pos={start_pos}")
    print (f"robot_pos={robot_pos}")
    print (f"goal_pos={goal_pos}")
    print (f"full_obstacle_list={full_obstacle_list}")
    return step_number1, hit_obstcle1, reach_goal1

episodes_data = {    
    "episode" : [],
    "steps1" : [],
    "success1" : [],
}

# execute all the episodes
for i in range(constants.N_EPISODES):
    episode_setup = episodes.EPISODES[i]
    step_number1, hit_obstcle1, reach_goal1 = play_episode(episode_setup["robot_pos"], episode_setup["goal_pos"], episode_setup["full_obstacle_list"])
    episodes_data["episode"].append(i)
    episodes_data["steps1"].append(step_number1)
    episodes_data["success1"].append(reach_goal1)

print("Final result")
print("------------")
print("Episode: ", episodes_data["episode"])
print("Steps1: ", episodes_data["steps1"])
print("Success1: ", episodes_data["success1"])

# prepare to show the statistics
passed_episodes = {
    "x" : [],
    "y" : [],
    "rl" : 0,
}
failed_episodes = {
    "x" : [],
    "y" : []
}

# will print success points
for episode_index in range(constants.N_EPISODES):
    if episodes_data["success1"][episode_index]:
        passed_episodes["x"].append(episode_index)
        passed_episodes["y"].append(episodes_data["steps1"][episode_index])
        passed_episodes["rl"] += 1

# will print failed points
for episode_index in range(constants.N_EPISODES):
    if episodes_data["success1"][episode_index] == False:
        failed_episodes["x"].append(episode_index)
        failed_episodes["y"].append(episodes_data["steps1"][episode_index])

fig, axes = plt.subplots(2)
fig.suptitle('Obstacle Avoidance')
episode_steps_plot = axes[0]
episode_steps_plot.set_title("Episode Steps") 

episode_steps_plot.plot(episodes_data["steps1"], "Blue", label = "Static Policy")
episode_steps_plot.scatter(passed_episodes["x"], passed_episodes["y"], label= "Reached the Goal", color= "green",  
            marker= "*", s=30) 
episode_steps_plot.scatter(failed_episodes["x"], failed_episodes["y"], label= "Hit an Obstacle", color= "red",  
            marker= "s", s=30) 

episode_steps_plot.set(xlabel='Episodes', ylabel='Steps')
episode_steps_plot.legend()

print("Accuracy:")
rl_accuracy = passed_episodes["rl"]/constants.N_EPISODES*100
print(f"Static Policy: {rl_accuracy}%")

accuracy_plot = axes[1]
accuracy_plot.set_title("Accuracy") 
accuracy_plot.set(xlabel='Algorithms', ylabel='Percentage')
accuracy_plot.bar(["Static Policy"], [rl_accuracy], width=0.4)

# show the chart
plt.tight_layout()
plt.show()


