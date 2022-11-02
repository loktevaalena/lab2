n = int(input())
team1 = []
team2 = []
for i in range(n):
 name, age = input().split()
 if(int(age)<20) and (int(age)>40):
  team1.append(name)
 else:
  team2.append(name)
print(team1)
print(team2)
