from score_prediction.datareader import DataReader


def get_date(d):
    date = d["date"]
    return date


def get_data_set(d):
    players = []
    team = []
    for i in d:
        team.append(i)
    d = d[team[0]]
    for x in d:
        players.append(x)
    d = d[players[0]]
    dataset = d["GROUP_SET"]
    return dataset


def write_prediction(team_one, team_two):
    d = DataReader().get_full_dict()
    final = {}
    dataset = get_data_set(d)
    date = get_date(d)
    final["GROUP_SET"] = dataset
    final["DATE"] = date
    for x in team_one:
        final[x.upper()] = team_one[x]
    for x in team_two:
        final[x.upper()] = team_two[x]
    DataReader().write_data(final, "prediction.json")


def read_prediction():
    dic = DataReader().read_data("prediction.json")
    for i in dic:
        print(i + " = " + str(dic[i]))