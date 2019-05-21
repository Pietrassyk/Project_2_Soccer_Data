class Game():
    def __init__(self,ID,home_team,away_team,season,date,score_home,score_away):
        self.ID = ID
        self.home_team = home_team
        self.away_team = away_team
        self.season = season
        self.date = date
        self.location = "get location"
        self.score_home = score_home
        self.score_away = score_away
        self.winner = self.winner()
        self.looser = self.looser()
        self.is_rain = self.is_rain()

    def winner(self):
        if self.score_away > self.score_home:
            return self.away_team
        if self.score_away < self.score_home:
            return self.home_team
        else:
            return "Tie"

    def looser(self):
        if self.score_away < self.score_home:
            return self.away_team
        if self.score_away > self.score_home:
            return self.home_team
        else:
            return "Tie"

    def is_rain(self):

        pass
