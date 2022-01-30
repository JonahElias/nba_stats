import datetime
from json import dump
import nba_api.stats.endpoints
from nba_api.stats.static import teams
from nba_api.stats.endpoints.playerdashboardbylastngames import PlayerDashboardByLastNGames


def get_date():
    dt = datetime.datetime.today()
    return str(dt.month) + "." + str(dt.day) + "." + str(dt.year)


def get_ids(team_name):
    print("getting ids")
    ids = {}
    # Call stat object method that returns roster dict
    team = teams.find_teams_by_full_name(team_name)
    team_id = team[0]["id"]
    stat_obj = nba_api.stats.endpoints.CommonTeamRoster(team_id)
    stats = stat_obj.common_team_roster.get_dict()
    data = stats["data"]
    for i in data:
        name = i[3]
        id = i[-1]
        ids[name] = id
    print("complete")
    return ids


def last_ten_games(id):
    # Get dictionary with stats from last 10 games
    stat_obj = PlayerDashboardByLastNGames(id).last10_player_dashboard
    stats = stat_obj.get_dict()
    return stats


def prep_dict(team_name):
    ids = get_ids(team_name)
    d = {team_name: {}}
    c = 0
    print("pulling stats")
    for i in ids:
        x = c / len(ids) * 100
        print(str(round(x)) + "%")
        id = ids[i]
        d[team_name][i] = {}
        d[team_name][i]["id"] = id
        stat_obj = PlayerDashboardByLastNGames(id).last10_player_dashboard
        stats = stat_obj.get_dict()
        headers = stats["headers"]
        data = stats["data"]
        if len(data) != 0:
            d[team_name][i]["playing_state"] = "active"
            data = data[0]
            for count in range(0, len(headers)):
                d[team_name][i][headers[count]] = data[count]
        else:
            d[team_name][i]["playing_state"] = "inactive"
        c += 1

    d["date"] = get_date()
    print("complete")
    return d


def write_file(team_name, file_n="score_prediction/team_one.json"):
    d = prep_dict(team_name)
    print("writing file")
    file = open(file_n, "w")
    dump(d, file)
    file.close()
    print("complete")
