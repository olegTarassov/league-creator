# league-creator

D.D.O Soccer League
-----------------------------------

The goal is to create a league that would:
1) dynamically load teams and their names
2) add players to the teams.
	- players can have condition
		- team preference
		- player preference play along side
		- coach preference
	- players added across all teams to maintain equilibrium

Alternative

teams = list()

teams.append( make_team( name, coach)

Initializing class with this make sense
def make_team(name):
team = {'name': name, 'coach': coach, 'players': []}
return team
