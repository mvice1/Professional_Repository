###CREATE ROSTERS

#take names from og_players.txt

#assign each name a random overall (40-99), position (5 possible options), and school year

#user picks college team (Choice of 16) 

#every team will have 1 player per position (PG,SG,SF,PF,C)

###SEASON

#teams play against eachother.
#(matches are held by the OVR effecting each players points)
#(the players points are added together and the team with the most points wins)

#after a game, a team needs to have their record updated based on if they win or loose

#Based on the team records, the teams are seeded based on record

#Based on seed, the teams play eachother.

#After the tournament, the user can continiue to the next season


###OFF SEASON

#Top 10 players OVR in league are removed to go to the draft.

#ALL 4th years graduate and are removed from their teams.

#Every player gains 1 grade, and their overall changes randomly slightly

#New HS prospects will get assigned to new teams


###EXTRA THINGS TO ADD

#Injuries

#Player training (user can train their players to make them better)

#championship and record tracker through the seasons

class Players:
    """Identify Players information and team
    Attributes:
	    skill= 
	    position= 
    """
	def __init__(self, rating, position, year...):
        """Initializes a Player with specific attributes

        Args:
            rating (int): Overall rating of each player
            position (String): Position that the player plays
            year (int): How many years into college the players are (1 - High School,
            2 - Freshman, 3 - Sophmore etc.)
        """
		self.rating = rating
		#Etc.
	def assign_team():
        """Assigns a specific team to a player
        """
#Assign players to a team
	def assign_position():
        """Assigns a specific position to a player
        """
#Assign players to a position on their team

class Draft:
    """Assigns new and old players to a team or to no team
    """
	def graduation():
        """Causes the player to graduate
        """
#All seniors graduate
	def best_player():
        """Decides who is the best possible player for a team based on overall rating
        """
#Best players get sent to the NBA
	def highschool_players():
        """Opens the high school players file, and aloows them to be picked in the draft
        """
#Seniors in highschool come up to join teams

class Simulation:
    """Assigns which teams win and lose, and how they place at the end
    """
	def assign_tournaments():
        """Assigns which teams get into the tournament, as well as what seeds each
        team gets
        """
#Assign who will play who in the tournament
	def play():
        """Teams will play a game against each other, and a winner will be chosen
        """
#Teams will “play” each other winner advances
	def nat_champ():
        """National Championship Game. Will show the whole bracket
        """
#National champ game… show whole bracket
                """runs the basketball program simulation
                """
if __name__ == "__main__":
        Simulation()