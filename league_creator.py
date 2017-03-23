#! /usr/bin/env python3
"""
D.D.O League Creator
Input csv for players.
"""

__author__ = "Oleg Tarassov"
__email__ = "oleg.tarassov@outlook.com"
__version__ = "1.0"
__status__ = "In Progress"
__date__ = "11-03-2017"

import csv
import sys

FILE_PLAYERS = 'soccer_players.csv'
FILE_TEAMS = 'soccer_teams.csv'

class Player:
    """ Holds Player information
        mandatory: name, parent/responsible,
        optional : preference (team, player, coach)
        at the end: team assigned
    """
    __slots__ = ['name', 'guardian', 'team', 'pref']

    def __init__(self, name=None, guardian=None, pref=None):
        """Initialize all variables"""
        self.name = name
        self.guardian = guardian
        self.team = None

        if pref == '':
            self.pref = None
        else:
            req, cond = tuple(pref.split(":"))
            self.pref = dict()
            self.pref[req] = cond

    def __str__(self):
        """Print Players attributes"""
        return '(name:%s, parent:%s, preference:%s)' % (self.name, self.guardian, self.pref)


class League:
    """ Holds teams,coaches,players
    """
    __slots__ = ['teams', 'coaches', 'players']

    def __init__(self):
        self.teams = dict()
        self.coaches = dict()
        self.players = list()

    def __str__(self):
        buff = list()
        buff.append("Coach\tTeam")

        for key in self.coaches:
            buff.append("{}\t{}".format(key, self.coaches[key]))

        buff.append("")
        buff.append("Team\tPlayers")

        for key in self.teams:
            buff.append("{}\t{}".format(key, self.teams[key]))

        return "\n".join(buff)

    def load_from_file(self, filename, load):
        """Read CSV and loads the appropriate type of data into the corresponding attributes"""
        with open(filename, 'r') as csvfile:
            data_extract = csv.DictReader(csvfile, delimiter=',')

            if load == 'teams':
                for team in data_extract:
                    if team['Coach'] != '':
                        self.coaches[team['Coach']] = team['Team']

                    self.teams[team['Team']] = list()
            elif load == 'players':
                for player in data_extract:
                    player_details = Player(player['Name'], player['Guardian Name(s)'],
                                            player['Preference'])

                    # append each player's details the players list
                    self.players.append(player_details)
            else:
                sys.exit("ERROR: Incorrect load type:{}".format(load))

    def list_filter(self, req):
        """ Split list using filter on player requirements"""
        return [free_agent for free_agent in self.players
                if free_agent.pref is not None and req in free_agent.pref]


#Add player to team function

def main():
    """ Main Program"""

    u7 = League()

    u7.load_from_file(FILE_TEAMS, 'teams')
    u7.load_from_file(FILE_PLAYERS, 'players')

    #Debug
    #print(u7)

    players_team_pref = u7.list_filter('team')
    players_coach_pref = u7.list_filter('coach')
    players_friend_pref = u7.list_filter('friend')

#    for free_agent in u7.players:
        #Iterate and assign in priority
        #1) condition team,2) condition coach,3)no condition,4)condition friend
 #       if free_agent.pref is not None:
 #           if 'team' in free_agent.pref:
 #               print("Player:{} wants Team:{}".format(free_agent.name, free_agent.pref['team']))
 #           elif 'coach' in free_agent.pref:
 #               print("Player:{} wants Coach:{}".format(free_agent.name, free_agent.pref['coach']))
 #           elif 'friend' in free_agent.pref:
 #           print("Player:{} wants Friend:{}".format(free_agent.name, free_agent.pref['friend']))





#    for x in players_team_pref:
#        print("Player:{} wants Team:{}".format(x.name, x.pref['team']))
#
#    test = players_team_pref.pop()

   # test.team = 'cowboy'
   # for free_agent in u7.players:
   #     if test == free_agent:
   #         print("team is {}".format(free_agent.team))


    del u7


if __name__ == '__main__':
    main()
