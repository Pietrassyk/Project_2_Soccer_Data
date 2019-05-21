#Libraries
import pandas as pd
import tpclean.tpclean as tp
import os

#Locals Files
import Teams
import Games

#TODO Checkout Methods for inheritable and noninheritable Functions

####################
#######CLASS########
####################

class Season():
    teams_list = []
    games_list = []
    locations_list = []

    def __init__(self,year,divisions = [], database = "database.sqlite"):
        self.year = year
        self.figure_directory = "/Figures"

        #establish connection to database and run querry
        tp.sql_connect(database)
        divs = "','".join(divisions)
        df = tp.sql(f""" SELECT * FROM FlatView_Advanced {f" WHERE Div IN('{str(divs)}')" if divisions else ''} 
                    AND Season == {year}""")
        #df = df.drop_duplicates("Match_ID")
        self.data = df

        #populate Season
        self.fill_teams()
        self.fill_games()
        self.get_statistics()


    def get_team(self,team_to_check):
        #print(self.teams_list[0:4])
        for team in self.teams_list:
            #print(f"{team.name} == {team_to_check}")
            if(team.name == team_to_check):
                return team
        return "error"

    def fill_teams(self):
        df = self.data
        self.teams_list = [Teams.Team(i, df.HomeTeam.unique()[i]) for i in range(len(df.HomeTeam.unique()))]

    def fill_games(self):
        self.games_list = []
        df = self.data[["Match_ID", "HomeTeam", "AwayTeam", "Season", "Date", "FTHG", "FTAG"]]
        for i in range(len(df)):
            ID = df.Match_ID[i]
            home_team = self.get_team(df.HomeTeam[i])
            away_team = self.get_team(df.AwayTeam[i])
            season = df.Season[i]
            date_list = df.Date[i].split("-")
            date = "/".join([date_list[1], date_list[2], date_list[0]])
            score_home = df.FTHG[i]
            score_away = df.FTAG[i]
            ID_list = [game.ID for game in self.games_list]
            if ID in ID_list:
                continue
            else:
                self.games_list.append(Games.Game(ID,home_team,away_team,season,date,score_home,score_away))

    def get_statistics(self):
        for team in self.teams_list:
            team.get_win_percentage()

    def create_image_directory(self):
        # define the name of the directory to be created
        path = self.figure_directory
        try:
            os.mkdir(path)
        except OSError:
            print("Creation of the directory %s failed" % path)
        else:
            print("Successfully created the directory %s " % path)



