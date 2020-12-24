input1='389125467'
input2='496138527'

cups=list(input2)
cups=list(map(int,cups))
highest,lowest=len(cups),1

current=cups[0]
for _ in range(100):
    pickedupcups=[]
    for i in range(3):
        pickedupcups.append(cups.pop((cups.index(current)+1)%len(cups)))
    
    destination=current-1
    if destination<lowest:
            destination=highest
    
    while destination in pickedupcups :
        destination-=1
        if destination<lowest:
            destination=highest
    pos=cups.index(destination)
    cups[pos+1:pos+1]=pickedupcups # insert after destination
    currentcupindex=cups.index(current)
    current=cups[(currentcupindex+1)%len(cups)]
    
pos=cups.index(1)
if pos==len(cups)-1:
    cups2=cups[:pos]
elif pos==0:
    cups2=cups[(pos+1):]
else:
    cups2=cups[pos+1:]+cups[:pos]
print('a)',''.join(list(map(str,cups2))))
