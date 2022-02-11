import subprocess
from score_prediction.write_json import write_file
from score_prediction.datareader import DataReader


class Interface:

    def run(self):
        while True:
            cmd = input("enter command: ")
            self.process_cmd(cmd)

    def process_cmd(self, cmd):
        if cmd == "write_file":
            self.write_file()

        elif cmd == "read_json":
            self.readjson()

        elif cmd == "run_tests":
            self.run_tests()

    def write_file(self):
        team = input("enter team name: ")
        file = input("enter save file (enter 1 or 2, default is 1): ")
        if file not in ["1", "2"]:
            file = "1"

        if file == "1":
            file_path = "team_data/" + "team_one.json"
            write_file(team, file_path)
        else:
            file_path = "team_data/" + "team_two.json"
            write_file(team, file_path)

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

    def run_tests(self):
        subprocess.call(["sh", "./testing/run_tests.sh"])
