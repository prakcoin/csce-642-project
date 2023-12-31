import numpy as np
import gymnasium as gym
from stable_baselines3 import A2C



class A2CBaseline():
    def __init__(self, env, training_steps, testing_steps, lr, gamma):
        self.env = env
        self.training_steps = training_steps
        self.testing_steps = testing_steps
        self.model = A2C("MlpPolicy", env, learning_rate=lr, gamma=gamma, use_rms_prop=False)

    def train_model(self):
        self.model.learn(total_timesteps=self.training_steps, progress_bar=True)
        self.model.save("saved models/a2c_baseline20k")
    
    def model_predict(self, model):
        total_reward = 0
        total_steps = 0
        state, _ = self.env.reset()
        for step in range(1, self.testing_steps + 1):
            total_steps = step
            action, _ = model.predict(state)
            next_state, reward, done, _, _ = self.env.step(action)

            total_reward += reward

            if done:
                break

            state = next_state

        return total_reward, total_steps