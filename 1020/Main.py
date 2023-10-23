from Animal import Animal
from Fruit import Fruit
from Member import Member

apple = Fruit
print("과일명 : %s"%apple.name)
print("색상 : %s"%apple.color)
apple.taste()
apple.vitamin()
print("-"*10)


cat = Animal
print(cat.name)
cat.sound()
print("-"*10)

mem1 = Member("지민",30)
mem2 = Member("뷔", 27)
mem1.showMember()
mem2.showMember()
print("-"*10)