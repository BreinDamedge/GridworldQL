

import random

""" 
Author: Jacob Ableidinger
Full Class Name: Two Dimentional Array
Date Documented: 12/31/2023
Description: 
    - 2d array
"""
class TDA():
    def __init__(self, rows_, columns_) -> None:
        self._rows = rows_
        self._cols = columns_
        self._data = [0]*(self._rows*self._cols)
    

    def __getitem__(self, rc: tuple):
        r, c = rc
        return self._data[r*self._cols + c]
    

    def __setitem__(self, rc: tuple, val:int):
        r, c = rc
        self._data[r*self._cols + c] = val


    def __repr__(self) -> str:
        width = max([len(str(i)) for i in self._data])
        ret = ""
        for r in range(self._rows):
            ret += "[ "
            for c in range(self._cols):
                ret += f"{str(self._data[r*self._cols + c]):>{width}}, "
            ret += "]"
            if r < self._rows - 1:
                ret += "\n"
        return ret
    




class Tile():
    def __init__(self, label_:str, value_:float, is_end_:bool) -> None:
        self.label = label_
        self.value = value_
        self.end = is_end_
    

    def info(self):
        """
        label, value, is_end
        """
        return self.label, self.value, self.end
    

    def __repr__(self) -> str:
        return str(self.label)


    def step_data(self):
        """
        value, is_end
        """
        return self.value, self.end

NEUTRAL_TILE_VALUE = 0
HOLE_TILE_VALUE = -5
GOAL_TILE_VALUE = 3
NEUTRAL = Tile('N', NEUTRAL_TILE_VALUE, False)
HOLE    = Tile('H', HOLE_TILE_VALUE, True)
GOAL    = Tile('G', GOAL_TILE_VALUE, True)




class Gridworld():
    def __init__(self, r_:int, c_:int, num_holes_:int=3) -> None:
        self._rows:int = r_
        self._cols:int = c_
        self._data:TDA = TDA(r_, c_)

        # fill data with neutral
        for r in range(self._rows):
            for c in range(self._cols):
                self._data[r,c] = NEUTRAL

        # make holes
        for _ in range(num_holes_):
            r = random.randint(0, self._rows-1)
            c = random.randint(0, self._cols-1)
            self._data[r, c] = HOLE

        # create goal
        self._data[self._rows-1, self._cols-1] = GOAL

        # set agent position to start
        self._agent_pos:list[int] = [0, 0]

        # Actions
        def up(self:"Gridworld"):
            if self._agent_pos[0] > 0:
                self._agent_pos[0] -= 1
        def down(self:"Gridworld"):
            if self._agent_pos[0] < self._rows-1:
                self._agent_pos[0] += 1
        def left(self:"Gridworld"):
            if self._agent_pos[1] > 0:
                self._agent_pos[1] -= 1
        def right(self:"Gridworld"):
            if self._agent_pos[1] < self._rows-1:
                self._agent_pos[1] += 1
        self._ACTIONS = [up, down, left, right]
    

    def __repr__(self) -> str:
        width = max([len(str(t))+1 for t in self._data._data]) # daaaaa... find a way to make the 2d array iterable. just python iterables in general
        ret = ""
        for r in range(self._rows):
            ret += "[ "
            for c in range(self._cols):
                if r == self._agent_pos[0] and c == self._agent_pos[1]:
                    ret += f"{(self._data[r, c].label + "."):>{width}}, "
                else:
                    ret += f"{self._data[r, c].label:>{width}}, "
            ret += "]"
            if r < self._rows - 1:
                ret += "\n"
        return ret
        
    
    def state(self) -> int:
        return self._cols*self._agent_pos[0] + self._agent_pos[1]


    """
    Author: Jacob Ableidinger
    Full Function Name: (full-name goes here if applicable)
    Date Documented: 01/04/2024
    Description: 
        - 
    Parameters:
        - 
    Returns:
        - new_state:int
        - reward:float
        - end_state:bool
    """
    def step(self, action_) -> tuple:
        """Step the environment
        Returns:
            state:int, reward:float, end_state:bool
        """

        # take action
        self._ACTIONS[action_](self) 
        # calculate state
        state = self.state()
        reward, end = self._data[*self._agent_pos].step_data()
        # return state and info
        return state, reward, end


    def reset(self) -> None:
        while self._data[*self._agent_pos].end:
            self._agent_pos[0] = random.randint(0, self._rows-1)
            self._agent_pos[1] = random.randint(0, self._cols-1)
        



if __name__ == "__main__":
    gw = Gridworld(4,4)
    print(gw)
    gw.step(0)
    print(gw)
    
