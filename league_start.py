import pandas as pd
import random
import re
import csv
import time
import seaborn as sns
import matplotlib.pyplot as plt


class Players:
    
    def __init__(self, name, position, rating, year, team = None):
        """Initializes a Player with specific attributes

        Args:
            name (String): Name of the player
            position (String): Position that the player plays
            year (int): How many years into college the players are (0 - High School,
            1 - Freshman, 2 - Sophmore etc.)
            rating (int): Overall rating of each player
            team (String): Team the player is on. Default value of 0
        """
        self.name = name
        self.position = position
        self.rating = rating
        self.year = year
        self.team = team
        
    def assign_position(self, position):
        self.position = position
    def assign_rating(self, rating):
        self.rating = rating
    def next_year(self):
        self.year += 1
    def assign_team(self, team):
        self.team = team    

def start():
    """This is the start of the league, where the user inputs their name,
    team, and drafts their players if they want to. If not, it will be 
    randomized for you.

    Args:
        lst_of_players (list): A list of all current 
        Player objects
    """
    name = input("Hello! Get ready to start your season. What is your name? ")
    
    if re.search(r"Aric", name):
        print("Hey Aric! Hope you enjoy our program! :)")
    
    #if not(name == match(^[a-zA-Z]\s*[a-zA-Z]?)):
        #print("Alert: The name you entered contains numbers and/or punctuation.")
    userName = re.compile("^[a-zA-Z]*\s?[a-zA-Z]*?")
    userName
    if not(userName.match(name)):
        print("Alert: The name you entered contains numbers and/or punctuation.")
        
    real_team = False
    all_teams = ["Arizona", "UCONN", "Duke", "Gonzaga", "Kansas","Kentucky", 
                 "Louisville", "Maryland", "Michigan", "Michigan State", 
                 "North Carolina", "Ohio State", "Texas", "UCLA", 
                 "Villanova", "Xavier"]
    while real_team == False:
        print("The college basketball teams available are:\n", all_teams)
        team = input(f"Welcome {name}. Choose your team! ")
        if team in all_teams:
            print(f"You have chosen {team}. Get ready your season is starting.")
            real_team = True
        else:
            print("Please enter a team in the list.")
    show_team(team)
    return team
    

def score(team,opponent):
    """Creates and calculates ech player points during the game

    Args:
        team (str): Users chosen team to play as
        opponent (str): Scheduled team going against users chosen team

    Returns:
        True if the team won or false if they lost
    """
    df = pd.read_csv("og_players_final.csv")
    df['Points Scored'] = df['Rating']*(random.randrange(1,5)/10)
    df['Points Scored'] -= df['Points Scored']%1
    #summing up the points scored to get points the team scored
    player_score = df.groupby("Team")['Points Scored'].sum()
    my_score = player_score[team]
    opp_score = player_score[opponent]
    if my_score >= opp_score:
        return True
    else:
        return False

def graduation(team):
    """Determines how many players are graduating from your team this season
    Args:
        team (str): Users chosen team to play as

    Returns:
        num_of_grads(int): Number of graduating players on your team
    
    """
    with open("og_players_final.csv", mode='r') as og_players:
        players_team = {}
        players_year = {}
        num_of_grads = 0
        reader = csv.reader(og_players)
        for rows in reader:
            #players_team[rows[0]] = rows[4]
            #players_year[rows[0]] = rows[3]
            if rows[4] == team:
                if rows[3] == "5":
                    num_of_grads += 1       
    print("Team " + str(team) + " has " + str(num_of_grads) + " graduating players this year.")
    return
def season(team):
    """Scheduled season for the chosen team to play against

    Args:
        team (str): Users chosen team to play as
    Returns:
        A statement saying whether they won or lost 
    """
    wins = 0
    losses = 0
    if team == "Arizona":
        pass
    else:
        win = score(team, "Arizona")
        if win == True:
            print(f"You won! {team} beat Arizona.")
            wins += 1
        else:
            losses += 1
            print(f"You lost :( Arizona beat {team}.")
        time.sleep(2)
    if team == "UCONN":
        pass
    else:
        win = score(team, "UCONN")
        if win == True:
            print(f"You won! {team} beat UCONN.")
            wins += 1
        else:
            losses += 1
            print(f"You lost :( UCONN beat {team}.")
        time.sleep(2)
    if team == "Duke":
        pass
    else:
        win = score(team, "Duke")
        if win == True:
            print(f"You won! {team} beat Duke.")
            wins += 1
        else:
            losses += 1
            print(f"You lost :( Duke beat {team}.")
        time.sleep(2)
    if team == "Gonzaga":
        pass
    else:
        win = score(team, "Gonzaga")
        if win == True:
            print(f"You won! {team} beat Gonzaga.")
            wins += 1
        else:
            losses += 1
            print(f"You lost :( Gonzaga beat {team}.")
        time.sleep(2)
    if team == "Kansas":
        pass
    else:
        win = score(team, "Kansas")
        if win == True:
            print(f"You won! {team} beat Kansas.")
            wins += 1
        else:
            losses += 1
            print(f"You lost :( Kansas beat {team}.")
        time.sleep(2)
    if team == "Kentucky":
        pass
    else:
        win = score(team, "Kentucky")
        if win == True:
            print(f"You won! {team} beat Kentucky.")
            wins += 1
        else:
            losses += 1
            print(f"You lost :( Kentucky beat {team}.")
        time.sleep(2)
    if team == "Louisville":
        pass
    else:
        win = score(team, "Louisville")
        if win == True:
            print(f"You won! {team} beat Louisville.")
            wins += 1
        else:
            losses += 1
            print(f"You lost :( Louisville beat {team}.")
        time.sleep(2)
    if team == "Maryland":
        pass
    else:
        win = score(team, "Maryland")
        if win == True:
            print(f"You won! {team} beat Maryland.")
            wins += 1
        else:
            losses += 1
            print(f"You lost :( Maryland beat {team}.")
        time.sleep(2)
    if team == "Michigan":
        pass
    else:
        win = score(team, "Michigan")
        if win == True:
            print(f"You won! {team} beat Michigan.")
            wins += 1
        else:
            losses += 1
            print(f"You lost :( Michigan beat {team}.")
        time.sleep(2)
    if team == "Michigan State":
        pass
    else:
        win = score(team, "Michigan State")
        if win == True:
            print(f"You won! {team} beat Michigan State.")
            wins += 1
        else:
            losses += 1
            print(f"You lost :( Michigan State beat {team}.")
        time.sleep(2)
    if team == "North Carolina":
        pass
    else:
        win = score(team, "North Carolina")
        if win == True:
            print(f"You won! {team} beat North Carolina.")
            wins += 1
        else:
            losses += 1
            print(f"You lost :( North Carolina beat {team}.")
        time.sleep(2)
    if team == "Ohio State":
        pass
    else:
        win = score(team, "Ohio State")
        if win == True:
            print(f"You won! {team} beat Ohio State.")
            wins += 1
        else:
            losses += 1
            print(f"You lost :( Ohio State beat {team}.")
        time.sleep(2)
    if team == "Texas":
        pass
    else:
        win = score(team, "Texas")
        if win == True:
            print(f"You won! {team} beat Texas.")
            wins += 1
        else:
            losses += 1
            print(f"You lost :( Texas beat {team}.")
        time.sleep(2)
    if team == "UCLA":
        pass
    else:
        win = score(team, "UCLA")
        if win == True:
            print(f"You won! {team} beat UCLA.")
            wins += 1
        else:
            losses += 1
            print(f"You lost :( UCLA beat {team}.")
        time.sleep(2)
    if team == "Villanova":
        pass
    else:
        win = score(team, "Villanova")
        if win == True:
            print(f"You won! {team} beat Villanova.")
            wins += 1
        else:
            losses += 1
            print(f"You lost :( Villanova beat {team}.")
        time.sleep(2)
    if team == "Xavier":
        pass
    else:
        win = score(team, "Xavier")
        if win == True:
            print(f"You won! {team} beat Xavier.")
            wins += 1
        else:
            losses += 1
            print(f"You lost :( Xavier beat {team}.")
        time.sleep(2)       
    print(wins,losses)

def season_quiet(team):
    """Keeps a record of the wins and loses

    Args:
        team (str): Users chosen team to play as
    """
    #team = start()
    wins = 0
    losses = 0
    if team == "Arizona":
        pass
    else:
        win = score(team, "Arizona")
        if win == True:
            wins += 1
        else:
            losses += 1
    if team == "UCONN":
        pass
    else:
        win = score(team, "UCONN")
        if win == True:
            wins += 1
        else:
            losses += 1
    if team == "Duke":
        pass
    else:
        win = score(team, "Duke")
        if win == True:
            wins += 1
        else:
            losses += 1
    if team == "Gonzaga":
        pass
    else:
        win = score(team, "Gonzaga")
        if win == True:
            wins += 1
        else:
            losses += 1
    if team == "Kansas":
        pass
    else:
        win = score(team, "Kansas")
        if win == True:
            wins += 1
        else:
            losses += 1
    if team == "Kentucky":
        pass
    else:
        win = score(team, "Kentucky")
        if win == True:
            wins += 1
        else:
            losses += 1
    if team == "Louisville":
        pass
    else:
        win = score(team, "Louisville")
        if win == True:
            wins += 1
        else:
            losses += 1
    if team == "Maryland":
        pass
    else:
        win = score(team, "Maryland")
        if win == True:
            wins += 1
        else:
            losses += 1
    if team == "Michigan":
        pass
    else:
        win = score(team, "Michigan")
        if win == True:
            wins += 1
        else:
            losses += 1
    if team == "Michigan State":
        pass
    else:
        win = score(team, "Michigan State")
        if win == True:
            wins += 1
        else:
            losses += 1
    if team == "North Carolina":
        pass
    else:
        win = score(team, "North Carolina")
        if win == True:
            wins += 1
        else:
            losses += 1
    if team == "Ohio State":
        pass
    else:
        win = score(team, "Ohio State")
        if win == True:
            wins += 1
        else:
            losses += 1
    if team == "Texas":
        pass
    else:
        win = score(team, "Texas")
        if win == True:
            wins += 1
        else:
            losses += 1
    if team == "UCLA":
        pass
    else:
        win = score(team, "UCLA")
        if win == True:
            wins += 1
        else:
            losses += 1
    if team == "Villanova":
        pass
    else:
        win = score(team, "Villanova")
        if win == True:
            wins += 1
        else:
            losses += 1
    if team == "Xavier":
        pass
    else:
        win = score(team, "Xavier")
        if win == True:
            wins += 1
        else:
            losses += 1
    return wins

def argsort(seq):
    """" Allows for the ranking of the teams

    Args:
        seq (int): order of best ranked team based off wins

    Returns:
        str: sorted list
    """
    return [x for x,y in sorted(enumerate(seq), key = lambda x: x[1])]      

def main():
    """Runs the season and the championship game
    """
    
    team = start()
    season(team)
    arizona = season_quiet("Arizona")
    uconn = season_quiet("UCONN")
    duke = season_quiet("Duke")
    gonzaga = season_quiet("Gonzaga")
    kansas = season_quiet("Kansas")
    kentucky = season_quiet("Kentucky")
    louisville = season_quiet("Louisville")
    maryland = season_quiet("Maryland")
    michigan = season_quiet("Michigan")
    michigan_st = season_quiet("Michigan State")
    unc = season_quiet("North Carolina")
    ohio_state = season_quiet("Ohio State")
    texas = season_quiet("Texas")
    ucla = season_quiet("UCLA")
    villanova = season_quiet("Villanova")
    xavier = season_quiet("Xavier")
    team_score = [arizona, uconn, duke, gonzaga, kansas, kentucky, louisville, maryland, michigan, michigan_st, unc, ohio_state, texas, ucla, villanova, xavier]
    team_name = ["Arizona","UCONN","Duke","Gonzaga","Kansas","Kentucky","Louisville","Maryland","Michigan","Michigan State","North Carolina","Ohio State","Texas","UCLA","Villanova","Xavier"]
    winner = argsort(team_score)
    print(f'The first place team is {team_name[winner[-1]]}, the second place team is {team_name[winner[-2]]} and the third place team is {team_name[winner[-3]]}.')
    
    
    print(f'The first place team is {team_name[winner[-1]]}, the second place team is {team_name[winner[-2]]} and the third place team is {team_name[winner[-3]]}.')  

    if team == team_name[winner[-1]]:
        print(f"Your team finished first place! You now play {team_name[winner[-2]]} in the finals. Good luck :)")
        time.sleep(4)
        final = score(team, team_name[winner[-2]])
        if final == True:
            print("You won the finals! Congratulations!!")
        else:
            print(f"You lost in the final to {team_name[winner[-2]]}")
        time.sleep(3) 
    elif team == team_name[winner[-2]]:
        print(f"Your team finished first place! You now play {team_name[winner[-1]]} in the finals. Good luck :)")
        time.sleep(4)
        final = score(team, team_name[winner[-1]])
        if final == True:
            print("You won the finals! Congratulations!!")
        else:
            print(f"You lost in the final to {team_name[winner[-1]]}")
        time.sleep(3) 
    else:
        print(f"Your team missed the finals :( Good luck next year! The two finalists are {team_name[winner[-1]]} and {team_name[winner[-2]]}.")
        final = score(team_name[winner[-1]], team_name[winner[-2]])
        if final == True:
            print(f"{team_name[winner[-1]]} beat {team_name[winner[-2]]} in the finals!")
        else:
            print(f"{team_name[winner[-2]]} beat {team_name[winner[-1]]} in the finals!")
    graduation(team)

            
def awards(mvp):
    """Selects the best players per rating in the league and gives them an award
    
    """
    df = pd.read_csv("og_players_final.csv")
    mvp = df.groupby("Rating")['Name'].min()
    print(f"The best players in the league by {mvp} are...")
    

def show_team(team):
    """Visulization of the users team

    Args:
        team (str):Users chosen team to play as
    """
    df = pd.read_csv("og_players_final.csv")
    sns.set_theme(style="whitegrid")
    sns.barplot(x= df.loc[df.Team==team].Year, y= df.loc[df.Team==team].Rating, hue = df.loc[df.Team==team].Name)
    plt.show()    
   

if __name__ == "__main__":
    main()
    awards(mvp=99)