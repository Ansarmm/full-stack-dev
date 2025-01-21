wins = int(input("Enter quantity of wins: ")) 
loses = int(input("Enter quantity of loses: "))
score = wins * 25 + loses * 5 #25 points for each win, 5 point for each lose
def calculate_team_performance(wins, loses, score):
    return score * 1.2 if wins > loses else score #If wins more than loses score multiplied by 1.2
score = calculate_team_performance(wins, loses, score)
print(score)

player1_results = []
number_games = int(input("Enter number of games: "))
for i in range(1, number_games + 1): #Enter scores of each game
    result = int(input(f"Enter scores of game N{i}: "))
    if result > 30: #if one of results > 30, add 10 scores
        result = result + 10
    else:
        result
    player1_results.append(result) #add scores of game into list
def player_performance(player1_results, number_games):
    return sum(player1_results) / number_games #sum of scores divided by number of games 
average_points = player_performance(player1_results, number_games)
print(average_points)

overall = 0 #overall report of team
def final_report(overall, average_points, score):
    if (average_points > 30 and score > 100):
        return overall + 2
    elif (score > 100 or average_points > 30):
        return overall + 1
    else:
         return overall
overall = final_report(overall, average_points, score)
if overall == 2:
    print("Awesome team")
elif overall == 1:
    print("Great work, but there is still work to be done")
else: 
    print ("You have a lot work to be done")