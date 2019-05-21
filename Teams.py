class Team():
    def __init__(self,ID,name):
        self.id = ID
        self.name = name
        self.goal_counter = 0
        self.win_counter = 0
        self.loss_counter = 0
        self.winning_percentage = 0
        self.stadium_location = "undefined"
        self.num_of_games_played = 0

    def to_dict(self):
        #TODO This should return a dictionary with key value pairs
        pass