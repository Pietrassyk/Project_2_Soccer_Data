import pandas as pd
import tpclean.tpclean as tp

class Season():
    teams_list = []
    games_list = []
    locations_list = []
    def __init__(self,year,divisions = [], database = "database.sqlite"):
        #TODO Insert Initializing of Teams from Database here
        self.year = year
        tp.sql_connect(database)
        divs = "','".join(divisions)
        #df = tp.sql(f""" SELECT * FROM FlatView_Advanced {f" WHERE Div IN('{call}')" if divisions else ''}""")
        df = tp.sql(f""" SELECT * FROM FlatView_Advanced {f" WHERE Div IN('{str(divs)}')" if divisions else ''} 
      AND Season == {year}""")
        self.data = df
