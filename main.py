from tttenv import Env

class Player:
    def __init__(self,_tttenv):
        self.env = _tttenv

    def step(self):
        envs = self.env.get()
        scores = np.zeros(len(envs))
        for i,env in enumerate(envs):
            winner,score = env.gameover()
            if winner:
                scores[i] = score
            else 
                
    


ttt = Env()
