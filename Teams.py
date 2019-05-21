import matplotlib.pyplot as plt
class Team():
    def __init__(self,ID,name):
        self.id = ID
        self.name = name
        self.goal_counter = 0
        self.win_counter = 0
        self.loss_counter = 0
        self.tie_counter = 0
        self.winning_percentage = 0
        self.stadium_location = "implement location getter"
        self.num_of_games_played = 0
        self.figure = 0
        self.figure_path = ""

    #TODO This should return a dictionary with key value pairs
    # Just run .__dict__
    def get_win_percentage(self):
        self.winning_percentage = self.win_counter/self.num_of_games_played
        return self.winning_percentage

    def plot(self, save = False, dir =""):
        plt.style.use('ggplot')
        fig = plt.figure(figsize=(5, 6));
        x = [1, 2, 3]
        y = [self.win_counter, self.loss_counter, self.tie_counter]
        plt.bar(x, y, tick_label=["Win", "Loss", "Tie"], color=("g", "r", "y"))
        plt.ylim((0, 34))
        plt.title(f"{self.name} - game results")
        plt.ylabel("Number of Games (#)")
        if save:
            plt.savefig(dir+self.name+".png");
            self.figure_path = dir+self.name[0:]
            self.figure = fig
            plt.close(fig)