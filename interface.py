from score_prediction.write_json import write_file

class Interface:

    def run(self):
        while True:
            cmd = input("enter command: ")
            self.process_cmd(cmd)

    def process_cmd(self, cmd):
        if cmd == "writefile":
            self.write_file()

    def write_file(self):
        team = input("enter team name: ")
        file_path = input("enter file path (default is 'score_prediction/team_one.json'): ")
        if file_path == "":
            write_file(team)
        else:
            write_file(team, file_n=file_path)