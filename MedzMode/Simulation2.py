from QAgent2 import QAgent
from Gridworld2 import Gridworld
from qol2 import print_progress_bar

if __name__ == "__main__":
    pass

    GRID_ROWS:int                  = 100
    GRID_COLS:int                  = 100
    NUM_HOLES:int                  = 300
    EPISODES:int                   = 40_000
    MAX_STEPS:int                  = GRID_ROWS * GRID_COLS
    INITIAL_EXPLORATION_RATE:float = 1.0
    EXPLORATION_DECAY:float        = 1/(EPISODES*MAX_STEPS)
    LEARNING_RATE:float            = 0.05
    DISCOUNT_FACTOR:float          = 0.99
    NUM_STATES:int                 = GRID_ROWS * GRID_COLS
    NUM_ACTIONS:int                = 4

    steve:QAgent  = QAgent(NUM_STATES, NUM_ACTIONS, INITIAL_EXPLORATION_RATE, EXPLORATION_DECAY, LEARNING_RATE, DISCOUNT_FACTOR)
    env:Gridworld = Gridworld(GRID_ROWS, GRID_COLS, NUM_HOLES)

    for _ in range(EPISODES):
        env.reset()
        steve.reset()
        steve.observe_state(env.state())
        for a in range(MAX_STEPS):
            new_state, reward, is_end = env.step(steve.take_action())
            steve.observe_state(new_state)
            steve.update_table(reward)
            steve.decay_exploration()
            if is_end:
                break
        print_progress_bar(EPISODES, _+1, end_newline_=True)
    

    

    #THIS_CODE_DOESN'T_SCALE
    print(env._data)

    steve.eval()
    from Gridworld2 import TDA
    actions = ["^", ".", "<", ">"]
    policy = TDA(GRID_ROWS, GRID_COLS)
    for r in range(GRID_ROWS):
        for c in range(GRID_COLS):
            state = r*GRID_COLS + c
            action = steve.policy(state)
            policy[r, c] = actions[action]
            if env._data[r,c].label != 'N':
                policy[r,c] = env._data[r,c].label
    print()
    print(policy)