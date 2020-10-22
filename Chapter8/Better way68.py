#
# 아이템 68
#
class GameState:
    def __init__(self):
        self.level = 0
        self.lives = 4

state = GameState()
state.level += 1     # 플레이어가 레벨을 깼다
state.lives -= 1     # 플레이어가 재시도해야 한다

print(state.__dict__)

import pickle

state_path = 'game_state.bin'
with open(state_path, 'wb') as f:
    pickle.dump(state, f)

with open(state_path, 'rb') as f:
    state_after = pickle.load(f)

print(state_after.__dict__)

#
class GameState:
    def __init__(self):
        self.level = 0
        self.lives = 4
        self.points = 0 # 새로운 필드

state = GameState()
serialized = pickle.dumps(state)
state_after = pickle.loads(serialized)
print(state_after.__dict__)

with open(state_path, 'rb') as f:
    state_after = pickle.load(f)

print(state_after.__dict__)

assert isinstance(state_after, GameState)

#
class GameState:
    def __init__(self, level=0, lives=4, points=0):
        self.level = level
        self.lives = lives
        self.points = points

def pickle_game_state(game_state):
    kwargs = game_state.__dict__
    return unpickle_game_state, (kwargs,)

def unpickle_game_state(kwargs):
    return GameState(**kwargs)

import copyreg

copyreg.pickle(GameState, pickle_game_state)

state = GameState()
state.points += 1000
serialized = pickle.dumps(state)
state_after = pickle.loads(serialized)
print(state_after.__dict__)

class GameState:
    def __init__(self, level=0, lives=4, points=0, magic=5):
        self.level = level
        self.lives = lives
        self.points = points
        self.magic = magic   # 추가한 필드

print('이전:', state.__dict__)
state_after = pickle.loads(serialized)
print('이후:', state_after.__dict__)

#
class GameState:
    def __init__(self, level=0, points=0, magic=5):
        self.level = level
        self.points = points
        self.magic = magic

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#pickle.loads(serialized)

def pickle_game_state(game_state):
    kwargs = game_state.__dict__
    kwargs['version'] = 2
    return unpickle_game_state, (kwargs,)

def unpickle_game_state(kwargs):
    version = kwargs.pop('version', 1)
    if version == 1:
        del kwargs['lives']
    return GameState(**kwargs)

copyreg.pickle(GameState, pickle_game_state)
print('이전:', state.__dict__)
state_after = pickle.loads(serialized)
print('이후:', state_after.__dict__)

#
class BetterGameState:
    def __init__(self, level=0, points=0, magic=5):
        self.level = level
        self.points = points
        self.magic = magic

pickle.loads(serialized)

print(serialized)

copyreg.pickle(BetterGameState, pickle_game_state)

state = BetterGameState()
serialized = pickle.dumps(state)
print(serialized)

