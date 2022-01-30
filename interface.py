from score_prediction.write_json import write_file
from score_prediction.datareader import DataReader


class Interface:

    def run(self):
        while True:
            cmd = input("enter command: ")
            self.process_cmd(cmd)

    def process_cmd(self, cmd):
        if cmd == "writefile":
            self.write_file()

        elif cmd == "readjson":
            self.readjson()

    def write_file(self):
        team = input("enter team name: ")
        file_path = input("enter file path (default is 'score_prediction/team_one.json'): ")
        try:
            if file_path == "":
                write_file(team)
            else:
                write_file(team, file_n=file_path)
        except:
            print("there was an error")

    def readjson(self):
        dr = DataReader()
        player = input("enter player name (optional): ").title()

        try:
            if player != "":
                key = input("enter key (optional): ").upper()
                if key != "":
                    dr.read_json(player, key)
                else:
                    dr.read_json(player)
            else:
                dr.read_json()

        except:
            print("there was an error")
        print("\n")
