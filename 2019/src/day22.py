input1="""Player 1:
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

input2="""Player 1:
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
number_of_players=2

lines = input2.split('\n')
separator_index=lines.index('')
print(separator_index)
player1=[int(c) for c in lines[:separator_index] if c.isdigit()]
player2=[int(c) for c in lines[separator_index+1:] if c.isdigit()]
g_list = [player1, player2]

print('input',g_list)

iterate=True
loser=-1

while iterate:
    player_index=0
    maxv=g_list[0][0]
    if g_list[1][0]>g_list[0][0]:
        player_index=1
        maxv=g_list[1][0]
    
    g_list[player_index].pop(0)
    g_list[player_index].append(maxv)

    g_list[player_index].append(g_list[(player_index+1)%number_of_players].pop(0))
    
    iterate=True
    for n in range(number_of_players):
        if len(g_list[n])==0:
            iterate=False
            loser=n
            break

winner=(loser+1)%number_of_players
m=len(g_list[winner])

ans=0
for i in range(m):
    ans+=(g_list[winner][i]*m)
    m-=1
print(ans)

