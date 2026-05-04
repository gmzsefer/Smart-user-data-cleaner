import random

scores = []

while len(scores) < 20:
    score = random.randint(0, 6)
    
    if score == 0:
        break
    
    if score == 6:
        continue
    
    scores.append(score)

print(scores)


