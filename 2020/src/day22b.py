import copy # for deepcopy

input1 = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
"""

input2 = """Player 1:
3
42
4
25
14
36
32
18
33
10
35
50
16
31
34
46
9
6
41
7
15
45
30
27
49

Player 2:
8
11
47
21
17
39
29
43
23
28
13
22
5
20
44
38
26
37
2
24
48
12
19
1
40
"""
number_of_players = 2
g_stack = []

def find_game_loser(list1):
    global number_of_players
   
    game_loser = -1
    for n in range(number_of_players):
        if len(list1[n]) == 0:
            game_loser = n
            break
            
    return game_loser

def update_winner_and_game_loser_of_round(winnerplayer,bothlist):
    bothlist[winnerplayer].append(bothlist[winnerplayer].pop(0))
    bothlist[winnerplayer].append(bothlist[(winnerplayer+1)%number_of_players].pop(0))
    return bothlist

def update_game(winner,g_list): 
    global g_stack
    global number_of_players
    
    # update prev game list with the sub game winner
    newlist = update_winner_and_game_loser_of_round(winner,copy.deepcopy(g_list[-1]))
    g_list.append(copy.deepcopy(newlist))
    
    game_loser = find_game_loser(g_list[-1])
    iterate = True
    if game_loser != -1:
        if len(g_stack) > 0:
            # found game game_loser. get previously pushed g_list from stack and operate on it
            g_list = g_stack.pop(-1)
            game_winner = (game_loser+1)%number_of_players

	    # update prev game list with the sub game winner
            newlist = update_winner_and_game_loser_of_round(game_winner,copy.deepcopy(g_list[-1]))
            g_list.append(copy.deepcopy(newlist))
        else:
            iterate = False # final winner
        
    return g_list,iterate,game_loser

# main 
lines = input2.split('\n')
separator_index=lines.index('')
print(separator_index)
player1=[int(c) for c in lines[:separator_index] if c.isdigit()]
player2=[int(c) for c in lines[separator_index+1:] if c.isdigit()]
g_list = [[player1,player2] ]
print('input',g_list)
iterate = True
game_loser = -1

# avoiding recursion because python cannot handle more than 999 recursions
while iterate:
    winner = -1
    # if any list matches with previous round list, player1 is automatic winner
    for prevround in g_list[:-1]:
        if prevround[0] == g_list[-1][0] and prevround[1] == g_list[-1][1]:
            winner = 0
            # if this is a sub game, update the prev game
            if len(g_stack) > 0:
                g_list = g_stack.pop(-1)
                # update prev game list with the sub game winner
                g_list,iterate,game_loser = update_game(winner,g_list)
            else:
                # if this is not a sub game find if the game ends
                game_loser = find_game_loser(g_list[-1])
                iterate = True
                if game_loser != -1:
                    iterate = False # game ends
        
    if winner == -1:        
        # winner was not found from prev round comparison
        # if the list total is greater than or equal to the value for both players
        # then go into sub game
        if len(g_list[-1][0])-1 >= g_list[-1][0][0] and len(g_list[-1][1])-1 >= g_list[-1][1][0]:
            g_stack.append(copy.deepcopy(g_list))
            g_list = [copy.deepcopy(g_list[-1])]

            # start with the existing cards the size of the value of the top card
            g_list[-1][0] = copy.deepcopy(g_list[-1][0][:g_list[-1][0].pop(0)])
            g_list[-1][1] = copy.deepcopy(g_list[-1][1][:g_list[-1][1].pop(0)])
        else:
            # otherwise do a simple combat rule where the higher value card wins the round
            winner = 0 if g_list[-1][0][0]  >  g_list[-1][1][0] else 1
            g_list,iterate,game_loser = update_game(winner,g_list)

# when the whole game ends, calculate answer
winner = (game_loser+1)%number_of_players
m = len(g_list[-1][winner])
print('winner',winner, g_list[-1][winner])
ans = 0
for i in range(m):
    ans += (g_list[-1][winner][i]*m)
   
    m -= 1
print('b) ',ans)
    
