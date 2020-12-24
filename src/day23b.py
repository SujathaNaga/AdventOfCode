input1='389125467'
input2='496138527'
lowest=1
highest=1000000

class Node:
    def __init__(self, val, next_node=None):
        self.val=val
        self.next=next_node

cups=list(input2)
cups=list(map(int,cups))

lookup_table={}
prev=None
# form linked list from the end node to beginning node
for i in range(len(cups)-1,-1,-1):
    new=Node(cups[i])
    new.next=prev
    lookup_table[cups[i]]=new # direct reference to the node that has the cup value
    prev=new


for i in range(highest,9,-1):
    new=Node(i)
    new.next=prev
    lookup_table[i]=new
    prev=new


lookup_table[cups[-1]].next=lookup_table[10]
current=lookup_table[cups[0]]
for _ in range(10000000):
    a=current.next
    b=a.next
    c=b.next
    current.next=c.next
    removed={current.val,a.val,b.val,c.val}
    destination=current.val
    while destination in removed:
        destination-=1
        if destination==0:
            destination=highest
    destination_reference=lookup_table[destination]
    destination_old_next=destination_reference.next
    destination_reference.next=a
    c.next=destination_old_next
    current=current.next

maincup=lookup_table[1]
a=maincup.next
b=a.next
print(a.val*b.val)



    


    
