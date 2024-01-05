import numpy as np
import random




class TwoStack():
    def __init__(self) -> None:
        self._data:list[int] = [0,0]
    

    def push_back(self, val_:int) -> None:
        self._data[0] = self._data[1]
        self._data[1] = val_
    

    def push_front(self, val_:int) -> int:
        self._data[1] = self._data[0]
        self._data[0] = val_


    def front(self) -> int:
        return self._data[0]

    
    def back(self) -> int:
        return self._data[-1]




class QAgent():
    ACTION = int
    STATE  = int

    def __init__(self, states_:int, actions_:int, inital_exploration_rate_:float, exploration_decay_amount_:float, learning_rate_:float, discount_factor_:float,) -> None:
        self._num_states:int                 = states_
        self._QTable:np.ndarray              = np.zeros((states_, actions_))
        self._num_actions:int                = actions_
        self._exploration_rate:float         = inital_exploration_rate_
        self._exploration_decay_amount:float = exploration_decay_amount_
        self._testing:bool                   = False
        self._learning_rate:float            = learning_rate_
        self._discount_factor:float          = discount_factor_
        self._last_two_states:TwoStack       = TwoStack() 
        self._last_action:int                = 0
    

    def reset(self) -> None:
        self._last_two_states.push_back(0)
        self._last_two_states.push_back(0)


    def observe_state(self, state_:STATE) -> None:
        self._last_two_states.push_back(state_)

    
    def policy(self, state_:STATE) -> STATE:
        self.observe_state(state_)
        if not self._testing and random.random() < self._exploration_rate:
            return random.randint(0, self._num_actions-1)
        else:
            return np.argmax(self._QTable[state_, :])
    
    
    def take_action(self) -> int:
        self._last_action = self.policy(self._last_two_states.back())
        return self._last_action
        

    def train(self) -> None:
        self._testing = False

    
    def eval(self) -> None:
        self._testing = True


    def update_table(self, reward_:float) -> None:
        """
        [1] Amber, “Zero to one: (DEEP) Q-learning, PART1, basic introduction and implementation,” 
        Medium, https://medium.com/@qempsil0914/zero-to-one-deep-q-learning-part1-basic-introduction-and-implementation-bb7602b55a2c 
        (accessed Jan. 3, 2024). 
        """
        
        # The formulation of updating Q(s, a)
        #self.Q[state, action] = self.Q [state, action] + learning_rate*(reward+discount*np.max(self.Q [new_state, :]) - self.Q [state, action]) [1]
        maximum_next_state_q_value:float    = np.max(self._QTable[self._last_two_states.back(), :])
        discounted_next_state_q_value:float = self._discount_factor * maximum_next_state_q_value
        estimated_td_target:float           = discounted_next_state_q_value + reward_
        current_state_q_value:float         = self._QTable[self._last_two_states.front(), self._last_action]
        estimated_td_error:float            = estimated_td_target - current_state_q_value
        q_value_adjustment_amount:float     = self._learning_rate * estimated_td_error

        self._QTable[self._last_two_states.front(), self._last_action] += q_value_adjustment_amount
        
        
    def decay_exploration(self) -> None:
        ARBITRARY_MINIMUM = 0.001
        if self._exploration_rate > ARBITRARY_MINIMUM:
            self._exploration_rate -= self._exploration_decay_amount




if __name__ == "__main__":
    pass
    ta = QAgent(16, 4)
    for i in range(16):
        print(ta.policy(i))

