import csv
import random

def game():
            
    players = ["Josh", "Luke", "Kate", "Mark", "Mary"]
    results = []

    for i in range(0,10):
        for player in players:
            result1 = random.randint(0, 100+1)
            results.append([player, result1])

    print(results)    

    with open('results.csv', 'w', newline="") as file:
    
        writer = csv.writer(file) 
        writer.writerow(["Player name", "Score"])
        writer.writerows(results)

game()
    
def high_scores():

    high_scores = {}

    with open('results.csv', mode='r') as file:
        
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            player = row[0]
            scores1 = int(row[1])
            
            if player not in high_scores:
                high_scores[player] = scores1

            if scores1 > high_scores[player]:
                high_scores[player] = scores1
            
            new_high_score = dict(sorted(high_scores.items(), key=lambda item: item[1],reverse=True))
    print(new_high_score)
    with open('high_scores.csv', mode='w', newline="") as file:

        #writer = csv.DictWriter(file)
        writer = csv.writer(file)
    
        writer.writerow(["Player name", "Score"])
        writer.writerows(new_high_score.items())

high_scores()