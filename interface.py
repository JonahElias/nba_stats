import subprocess
from score_prediction.write_json import write_file
from score_prediction.datareader import DataReader
from score_prediction import predict_score, handle


class Interface:

    def __init__(self, cmds=[]):
        self.cmds = cmds
        self.processed = False

    def run(self):
        while True:
            print()
            if self.cmds != [] and self.processed == False:
                for i in self.cmds:
                    self.process_cmd(i)
                self.processed = True

            else:
                cmd = input("enter command (enter 'help' to view list of commands): ")
                self.process_cmd(cmd)

    def process_cmd(self, cmd):
        if cmd == "write_file":
            self.write_file()

        elif cmd == "run_tests":
            self.run_tests()

        elif cmd == "help":
            self.print_cmds()
        elif cmd == "write_prediction":
            self.write_prediction()
        elif cmd == "read_prediction":
            print()
            handle.read_prediction()
        else:
            print("command not found")

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

    def run_tests(self):
        subprocess.call(["sh", "./testing/run_tests.sh"])

    def print_cmds(self):
        print()
        d = DataReader().read_data("program_info.json")
        cmds = d["commands"]
        for x in cmds:
            print(x + " - " + cmds[x])
        print()

    def write_prediction(self):
        score_one = predict_score.predict(True)
        score_two = predict_score.predict(False)
        handle.write_prediction(score_one, score_two)
        print("complete")
