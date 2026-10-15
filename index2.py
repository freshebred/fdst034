sum = 0
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
for d in days:
    num = input(f"How many hours did you study on {d}? ")
    sum = sum + int(num)
print(f"You have studied {sum} hours this week, congrats!")