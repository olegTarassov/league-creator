# league-creator

D.D.O Soccer League
-----------------------------------

The goal is to create a league that would add players based on their requirements or randomly.
1) dynamically load teams names and their coaches
2) add players to the teams.
	- players can have requirements
		- team preference
		- player preference
		- coach preference
	- players added across all teams fairly.

## Input Files

### soccer_players.csv

Name,Guardian Name(s),Preference→→
Joe Smith,Joe Parents,→→
Jill Tanner,Jill Parents,friend:Joe Smith→→
Brad Lee, Brad Parents,coach:Oleg→→
Kate Wilson,Maggy Wilson,team:Cosmos→→

### soccer_teams.csv

Team,Coach→→
Cosmos,Oleg→→
Meteor,Joe→→
Flames,→→
