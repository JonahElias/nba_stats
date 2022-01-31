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
        name = input("enter file name (default is 'team_one.json'): ")
        file_path = "team_data/" + name

        if name == "":
            write_file(team)
        else:
            write_file(team, file_n=file_path)


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
