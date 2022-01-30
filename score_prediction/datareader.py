from json import load


class DataReader:

    def __init__(self, file="score_prediction/team_one.json"):
        self.file = file


    def readbasicdict(self, dictionary, key=""):
        # prints out nba_api dict formatted with headers and data
        # optional parameter "key" prints out corresponding key-value pair
        headers = dictionary["headers"]
        data = dictionary["data"][0]
        if key != "":
            d = {}
            for count in range(0, len(data)):
                d[headers[count]] = data[count]
            try:
                print(key + " = " + str(d[key]))
            except:
                print("key does not exist")

        else:
            for i in range(0, len(data)):
                print(headers[i] + " : " + str(data[i]))

    def return_value(self, dictionary, key=""):
        # returns value from nba_api dict
        headers = dictionary["headers"]
        data = dictionary["data"][0]
        d = {}
        for count in range(0, len(data)):
            d[headers[count]] = data[count]
        try:
            value = d[key]
            return value
        except:
            print("there was a problem")

    def read_json(self, player="", key=""):
        # prints out data from json file
        # by default it prints out data for every player on the team
        # optional param player prints out the given players data
        # optional param key prints out stat from a player based on the given key/player
        team = []
        file = open(self.file, "r")
        d = load(file)
        for i in d:
            team.append(i)
        d = d[team[0]]
        if player != "":
            if key != "":
                try:
                    d = d[player]
                    value = d[key]
                    print(value)
                except:
                    print("there was a problem")

            else:
                try:
                    player = player.lower().title()
                    d = d[player]

                    print(player + "\n" + ("-" * len(player)) + "\n")
                    for i in d:
                        print(i + " = " + str(d[i]))
                except:
                    print("there was a problem")
        else:
            for i in d:
                print(i + "\n" + ("-" * len(i)))
                for x in d[i]:
                    print(x + " = " + str(d[i][x]))
                print("\n\n")

    def return_json_data(self, player="", key=""):
        # returns data from json file
        # optional param player returns json data from given player
        # optional param key returns value from given player and key
        file = open(self.file, "r")
        d = load(file)
        team = []
        for i in d:
            team.append(i)
        d = d[team[0]]
        if player != "":
            if key != "":
                try:
                    d = d[player]
                    if d["playing_state"] != "inactive":
                        value = d[key]
                    else:
                        value = 0

                    return value

                except:
                    print("there was a problem")
            else:
                try:
                    d = d[player]
                    return d
                except:
                    print("there was a problem")
        else:
            return d

    def get_sorted_dict(self, key):
        # Returns a dict with {player_name : data} format from high to low
        dic = DataReader().return_json_data()
        d = {}
        for player in dic:
            data = DataReader().return_json_data(player=player, key=key)
            d[player] = data

        sorted_dict = {}
        sorted_keys = sorted(d, key=d.get)
        sorted_keys = list(reversed(sorted_keys))
        for w in sorted_keys:
            sorted_dict[w] = d[w]
        return sorted_dict
