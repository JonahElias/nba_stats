import sys
from score_prediction.datareader import DataReader
from score_prediction.predict_score import base_score, base_score_v2, get_adj_factor, get_team_name


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


def mod_score(datareader, normal_score, base_one_true):
    base_one = base_score(datareader)
    base_two = base_score_v2(datareader)
    adj = get_adj_factor(datareader)
    if not normal_score:
        if base_one_true:
            score = base_one
        else:
            score = base_two
    else:
        score = (base_one + base_two) / 2
    score = score - (adj * .8)
    return round(score)


def predict(team_one, normal_score, base_one_true):
    if team_one:
        datareader = DataReader()
    else:
        datareader = DataReader("team_data/team_two.json")
    scr = mod_score(datareader, normal_score, base_one_true)
    d = datareader.get_full_dict()
    name = get_team_name(d)
    return [name, scr]


def get_prediction_dict(b):
    d = DataReader().get_full_dict()
    final = {}
    dataset = get_data_set(d)
    date = get_date(d)
    final["GROUP_SET"] = dataset
    final["DATE"] = date
    final["VARIABLE"] = b
    return final


def write_test_prediction(base):
    final = get_prediction_dict(base)
    path = "test_cases/"
    ready = True
    if base == "normal_alg":
        path = path + base + ".json"
        score_a = predict(True, True, False)
        score_b = predict(False, True, False)
        final[score_a[0]] = score_a[1]
        final[score_b[0]] = score_b[1]
    elif base == "base_score_one":
        path = path + base + ".json"
        score_a = predict(True, False, True)
        score_b = predict(False, False, True)
        final[score_a[0]] = score_a[1]
        final[score_b[0]] = score_b[1]
    elif base == "base_score_two":
        path = path + base + ".json"
        score_a = predict(True, False, False)
        score_b = predict(False, False, False)
        final[score_a[0]] = score_a[1]
        final[score_b[0]] = score_b[1]
    else:
        ready = False
    if ready:
        DataReader().write_data(final, path)
        print("complete")
    else:
        print("file could not be written")


write_test_prediction(sys.argv[1])
