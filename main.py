from tttenv import Env
from icecream import ic
import numpy as np

class Player:
    def __init__(self,_tttenv):
        self.env = _tttenv

    def step(self):
        envs, moves = self.env.get()
        scores = np.zeros(len(envs))
        for i,env in enumerate(envs):
            # print(env); #input()
            winner,score,boardfull = env.gameover()

            if boardfull:
                pass
            else:    
                if winner:
                    pass
                else:
                    # ic(winner)
                    score, _ = Player(env).step()
                
            scores[i] = score # push
            # print(i)
            
        # return
        if self.env.nextplayer == "x":
            return scores.max(), moves[scores.argmax()]
        elif self.env.nextplayer == "o":
            return scores.min(), moves[scores.argmin()]

    def play(self, x, y, player="x"):
        return self.env.put(x, y, player)

    def __str__(self):
        return self.env.__str__()


ttt = Env()
player  = Player(ttt)
print(player)

while True:
    ### USER PLAY ###
    try:
        x,y = input("x,y: ").split(',')
        x,y = int(x),int(y)
    except Exception as e:
        if isinstance(e, KeyboardInterrupt):
            # print("KeyboardInterrupt detected! Exiting gracefully.")
            exit(0)
        else:
            continue    
            
    if not player.play(x,y): continue
    print(player)
    
    winner,_,boardfull = player.env.gameover()
    if winner: 
        print(f"winner: {winner}")
        break

    elif boardfull:
        print(f"draw !!!")
        break

    ### COMPUTER PLAY ###
    score, move = player.step()
    # print(score,move)
    player.play(*move, 'o')
    print(player)
        
        
    winner,_,boardfull = player.env.gameover()
    if winner: 
        print(f"winner: {winner}")
        break

    elif boardfull:
        print(f"draw !!!")
        break
