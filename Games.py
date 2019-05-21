import weathergetter as wg
class Game():
    def __init__(self,ID,home_team,away_team,season,date,score_home,score_away):
        self.ID = ID
        self.home_team = home_team #Team Object
        self.away_team = away_team #Team Object
        self.season = season
        self.date = date
        self.location = home_team.stadium_location
        self.score_home = score_home
        self.score_away = score_away
        self.winner = self.winner()
        self.looser = self.looser()
        self.is_rain = self.get_rain()

        #Set Records
        self.home_team.goal_counter += self.score_home
        self.home_team.num_of_games_played += 1
        self.away_team.goal_counter += self.score_away
        self.away_team.num_of_games_played += 1

        if self.winner:
            self.winner.win_counter +=1
        if self.looser:
            self.looser.loss_counter +=1
        if self.tie():
            for team in self.tie():
                team.tie_counter +=1


    def winner(self):
        if self.score_away > self.score_home:
            return self.away_team
        if self.score_away < self.score_home:
            return self.home_team
        else:
            return None

    def looser(self):
        if self.score_away < self.score_home:
            return self.away_team
        if self.score_away > self.score_home:
            return self.home_team
        else:
            return None

    def tie(self):
        if self.score_away == self.score_home:
            return [self.home_team, self.away_team]
        else:
            return None

    def get_rain(self):
        return "du da"
        #return wg.WeatherGetter().is_rain(self.date , self.home_team.name + " stadium", False)