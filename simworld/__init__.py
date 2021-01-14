from gym.envs.registration import register

register(
    id='gridworld-jump-v0',
    entry_point='simworld.envs:GridJump',
)