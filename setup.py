from os import system
from score_prediction.datareader import DataReader


def setup():
    d = DataReader().read_data("program_info.json")
    if d["setup"] == False:
        system("pip install nba_api")
        system("pip install numpy")
        d["setup"] = True
    DataReader().write_data(d, "program_info.json")
