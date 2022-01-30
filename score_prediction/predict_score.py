from score_prediction.datareader import DataReader


def pare(d, length=10,):
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
    pct =  (fgm - fg3m) / (fga - fg3a)
    return round(pct, 3)


def weighted_avg(player, fg2w=.35):
    # weighted avg of 2pt and 3pt shots
    fg3w = 1 - fg2w
    datareader = DataReader()
    fg3 = datareader.return_json_data(player=player, key="FG3_PCT")
    fg2 = two_pt_pct(datareader, player)
    w_avg = (fg2 * fg2w) + (fg3 * fg3w)
    print(player)
    print(w_avg)



