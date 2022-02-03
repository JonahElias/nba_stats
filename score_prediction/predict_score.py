from score_prediction.datareader import DataReader


def get_team_name(d):
    team = []
    for i in d:
        team.append(i)
    return team[0]


def pare(d, length=10, ):
    dic = {}
    count = 1
    for i in d:
        if count <= length:
            dic[i] = d[i]
        count += 1

    return dic


def two_pt_pct(datareader, player):
    fga = datareader.return_json_data(player=player, key="FGA")
    fgm = datareader.return_json_data(player=player, key="FGM")
    fg3a = datareader.return_json_data(player=player, key="FG3A")
    fg3m = datareader.return_json_data(player=player, key="FG3M")
    if fga - fg3a == 0:
        return 0
    pct = (fgm - fg3m) / (fga - fg3a)
    return round(pct, 3)


def weighted_avg(datareader, player, fg2w=.35):
    # weighted avg of 2pt and 3pt shots
    fg3w = 1 - fg2w
    fg3 = datareader.return_json_data(player=player, key="FG3_PCT")
    fg2 = two_pt_pct(datareader, player)
    w_avg = (fg2 * fg2w) + (fg3 * fg3w)
    return w_avg


def base_score(datareader):
    d = datareader.get_sorted_dict("FGA")
    d = pare(d, 10)
    t = 0
    for x in d:
        pts = datareader.return_json_data(x, "PTS")
        pts = pts / 10
        t += pts
    t = round(t)
    return t


def base_score_v2(datareader):
    t = 0
    new = {}
    d = datareader.get_sorted_dict("FGA")
    d = pare(d, 10)
    for x in d:
        new[x] = two_pt_pct(datareader, x)
    for x in new:
        pct = new[x]
        fga = d[x]
        t += pct * fga * 2.5
    t = round(t / 10)
    return t


def get_avg(d):
    total = 0
    count = 0
    for x in d:
        total += d[x]
        count += 1
    return total / count


def get_adj_factor(datareader):
    if datareader.file == "team_data/team_two.json":
        blks = DataReader().get_sorted_dict("BLK")
    else:
        blks = DataReader("team_data/team_two.json").get_sorted_dict("BLK")
    turnovers = datareader.get_sorted_dict("TOV")
    total_turnovers = get_avg(turnovers)
    total_blks = get_avg(blks)
    total_blks = total_blks * .66
    return round(total_turnovers + total_blks)


def score(datareader):
    base_one = base_score(datareader)
    base_two = base_score_v2(datareader)
    score = (base_one + base_two) / 2
    adj = get_adj_factor(datareader)
    score = score - (adj * .8)
    return round(score)


def predict(team_one):
    if team_one:
        datareader = DataReader()
    else:
        datareader = DataReader("team_data/team_two.json")
    scr = score(datareader)
    d = datareader.get_full_dict()
    name = get_team_name(d)
    return {name: scr}
