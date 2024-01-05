import numpy as np
import random

class QAgent():
    def __init__(self, states_:int, actions_:int) -> None:
        self._num_states = states_
        self._QTable = np.zeros((states_, actions_))
        self._num_actions = actions_
        self._exp_rate = 1.0
        self._testing = False


    def policy(self, state_):
        if not self._testing and random.random() < self._exp_rate:
            return random.randint(0, self._num_actions-1)
        else:
            return np.argmax(self._QTable[state_, :])
        

    def update_table(self, prev_state_:int, action_, post_state_:int, reward_:float, discount_factor_:float, learning_rate_:float, ) -> None:
        """
        [1] Amber, “Zero to one: (DEEP) Q-learning, PART1, basic introduction and implementation,” 
        Medium, https://medium.com/@qempsil0914/zero-to-one-deep-q-learning-part1-basic-introduction-and-implementation-bb7602b55a2c 
        (accessed Jan. 3, 2024). 
        """
        
        # The formulation of updating Q(s, a)
        #self.Q[state, action] = self.Q [state, action] + learning_rate*(reward+discount*np.max(self.Q [new_state, :]) - self.Q [state, action]) [1]
        self._QTable[prev_state_, action_] += learning_rate_ * (reward_ + (discount_factor_ * np.max(self._QTable[post_state_, :])) - self._QTable[prev_state_, action_])
        
        
    def decay_exploration(self, exploration_decay_amount_:float) -> None:
        ARBITRARY_MINIMUM = 0.001
        if self._exp_rate > ARBITRARY_MINIMUM:
            self._exp_rate -= exploration_decay_amount_




if __name__ == "__main__":
    pass
    ta = QAgent(16, 4)
    for i in range(16):
        print(ta.policy(i))

