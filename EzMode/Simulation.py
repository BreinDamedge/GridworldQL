from QAgent import QAgent
from Gridworld import Gridworld
from qol import print_progress_bar

if __name__ == "__main__":
    pass

    
    GRID_ROWS:int           = 10
    GRID_COLS:int           = 10
    NUM_HOLES:int           = 10
    EPISODES:int            = 10_000
    MAX_STEPS:int           = GRID_ROWS * GRID_COLS
    EXPLORATION_DECAY:float = 1/(EPISODES*MAX_STEPS)
    LEARNING_RATE:float     = 0.05
    DISCOUNT_FACTOR:float   = 0.99
    NUM_STATES:int          = GRID_ROWS * GRID_COLS
    NUM_ACTIONS:int         = 4

    steve = QAgent(NUM_STATES, NUM_ACTIONS)
    env = Gridworld(GRID_ROWS, GRID_COLS, NUM_HOLES)

    #print(steve._QTable)

    for _ in range(EPISODES):
        env.reset()
        state = env.state()
        for a in range(MAX_STEPS):
            action = steve.policy(state)
            new_state, reward, is_end = env.step(action)
            steve.update_table(state, action, new_state, reward, DISCOUNT_FACTOR, LEARNING_RATE)
            state = new_state
            steve.decay_exploration(EXPLORATION_DECAY)
            if is_end:
                break
        print_progress_bar(EPISODES, _)

    #print(steve._QTable)
    print(env._data)


    #THIS_CODE_DOESN'T_SCALE
    steve._testing = True
    from Gridworld import TDA
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
    #print(env._data)