import random
import time
players = [0,0]
padding = [16 , 11]

move = 0
got6 = False
places = []
i=0
for y in range(10):
    if ((i/10)%2)==0:
        for x in range(10):
            places.append([x ,9-y ])
            i+=1
    else:
        for x in range(10):
            places.append([9-x ,9-y ])
            i+=1




        
    
    
while (players[0]<100 and players[1]<100):
    if move%2==0:
        order = input("Enter d for Roll : ")
        
        while order!="d":
            order = input("Enter d for Roll : ")
        dise = random.randint(1, 6)
        if dise==6:
            got6=True
        if (players[0]+dise)<=100  :
            if players[0]==0:
                if dise==6:
                    players[0]=1
                else:
                    pass
            else:
                players[0]+=dise
        else:
            players[0]=players[0]
    else:
        dise = random.randint(1, 6)
        if dise==6:
          got6=True
        if (players[1]+dise)<=100:
            if players[1]==0:
                if dise==6:
                    players[1]=1
                else:
                    pass
            else:
                players[1]+=dise
        else:
          players[1]=players[1]
    print(f"players {(move%2)+1} place is {players[move%2]}")
    
    if players[move%2]==7:
      players[move%2]=45
      time.sleep(0.5)
      print(f"players {(move%2)+1} place is {players[move%2]}")
    elif players[move%2]==33:
      players[move%2]=10
      time.sleep(0.5)
      print(f"players {(move%2)+1} place is {players[move%2]}")
    elif players[move%2]==34:
      players[move%2]=66
      time.sleep(0.5)
      print(f"players {(move%2)+1} place is {players[move%2]}")
    elif players[move%2]==37:
      players[move%2]=5
      time.sleep(0.5)
      print(f"players {(move%2)+1} place is {players[move%2]}")
    elif players[move%2]==40:
      players[move%2]=77
      time.sleep(0.5)
      print(f"players {(move%2)+1} place is {players[move%2]}")
    elif players[move%2]==48:
      players[move%2]=91
      time.sleep(0.5)
      print(f"players {(move%2)+1} place is {players[move%2]}")
    elif players[move%2]==57:
      players[move%2]=19
      time.sleep(0.5)
      print(f"players {(move%2)+1} place is {players[move%2]}")
    elif players[move%2]==62:
      players[move%2]=81
    elif players[move%2]==70:
      players[move%2]=31
      time.sleep(0.5)
      print(f"players {(move%2)+1} place is {players[move%2]}")
    elif players[move%2]==74:
      players[move%2]=96
      time.sleep(0.5)
      print(f"players {(move%2)+1} place is {players[move%2]}")
    elif players[move%2]==92:
      players[move%2]=55
      time.sleep(0.5)
      print(f"players {(move%2)+1} place is {players[move%2]}")
    elif players[move%2]==97:
      players[move%2]=56
      time.sleep(0.5)
      print(f"players {(move%2)+1} place is {players[move%2]}")
    else:
        pass
    
    
    if got6:
      got6=False
    else:
      move+=1
    
    
