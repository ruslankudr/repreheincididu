import numpy as np

class QLearning:
    def __init__(self, states, actions, learning_rate=0.1, discount_factor=0.9):
        self.states = states
        self.actions = actions
        self.q_table = np.random.rand(len(states), len(actions))
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor

    def choose_action(self, state):
        q_values = self.q_table[state]
        return np.argmax(q_values)

    def update(self, state, action, reward, next_state):
        q_value = self.q_table[state, action]
        next_q_value = np.max(self.q_table[next_state])
        self.q_table[state, action] = q_value + self.learning_rate * (reward + self.discount_factor * next_q_value - q_value)

    def get_q_value(self, state, action):
        return self.q_table[state, action]
