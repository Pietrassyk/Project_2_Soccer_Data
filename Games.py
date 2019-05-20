class Game():
    def __init__(self,ID,home_team,away_team,date,location,score_home,score_away):
        self.ID = ID
        self.home_team = home_team
        self.away_team = away_team
        self.date = date
        self.location = location
        self.score_home = score_home
        self.score_away = score_away
        self.winner = self.winner()
        self.looser = self.looser()
        self.weather = self.weather()

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

    def weather(self):
        pass
