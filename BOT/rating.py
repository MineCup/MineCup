async def rating(services):
    difference = {1000: 20,
                  950: 19,
                  850: 18,
                  800: 17,
                  700: 16,
                  600: 15,
                  550: 14,
                  500: 13,
                  450: 12,
                  400: 11,
                  350: 10,
                  300: 9,
                  250: 8,
                  200: 7,
                  150: 6,
                  125: 5,
                  100: 4,
                  75: 3,
                  50: 2,
                  25: 1}
    sheet = "1OaMpmMMFR_NIzmqtEh12XJ6N4X9R723S4g709FKvj_8"
    teamDict = {}
    diff = 0

    getMatches = services["rating"].spreadsheets().values().get(spreadsheetId=sheet,
                                                                range=f'matches!A2:E4000',
                                                                majorDimension='ROWS').execute()
    if "values" not in getMatches:
        print("В таблице нет матчей.")
        return
    teamRating = services["rating"].spreadsheets().values().get(spreadsheetId=sheet,
                                                                range=f'work!A2:D1000',
                                                                majorDimension='ROWS').execute()
    if "values" not in teamRating:
        print("В листе work нет команд. ВТФ?")
        return
    getMatches2 = services["rating"].spreadsheets().values().get(spreadsheetId=sheet,
                                                                 range=f'matches!G2:K4000',
                                                                 majorDimension='ROWS').execute()
    if "values" not in getMatches2:
        getMatches2.update(values=[])

    for team in teamRating["values"]:
        newDict = {team[0]: {"Name": team[0],
                             "Rating": team[2],
                             "Games": team[3]}}
        teamDict.update(newDict)

    for match in getMatches["values"]:
        matchTeams = {"winner": None,
                      "loser": None}

        for team in teamDict:
            if match[0] == team:
                matchTeams["winner"] = teamDict[team]
                continue
            if match[1] == team:
                matchTeams["loser"] = teamDict[team]
                continue

        if not matchTeams["winner"] or not matchTeams["loser"]:
            continue

        for d in difference:
            if abs(int(matchTeams["winner"]["Rating"]) - int(matchTeams["loser"]["Rating"])) >= d:
                diff = difference[d]
                break

        if int(matchTeams["winner"]["Rating"]) >= int(matchTeams["loser"]["Rating"]):
            matchTeams["winner"]["Rating"] = int(matchTeams["winner"]["Rating"]) + 25 - diff
            matchTeams["winner"]["Games"] = int(matchTeams["winner"]["Games"]) + 1
            matchTeams["loser"]["Rating"] = int(matchTeams["loser"]["Rating"]) - 20 + diff
            matchTeams["loser"]["Games"] = int(matchTeams["loser"]["Games"]) + 1
        else:
            matchTeams["winner"]["Rating"] = int(matchTeams["winner"]["Rating"]) + 25 + diff
            matchTeams["winner"]["Games"] = int(matchTeams["winner"]["Games"]) + 1
            matchTeams["loser"]["Rating"] = int(matchTeams["loser"]["Rating"]) - 20 - diff
            matchTeams["loser"]["Games"] = int(matchTeams["loser"]["Games"]) + 1

        teamDict[matchTeams["winner"]["Name"]] = matchTeams["winner"]
        teamDict[matchTeams["loser"]["Name"]] = matchTeams["loser"]

    for team in range(len(teamRating["values"])):
        name = teamRating["values"][team][0]
        if name == "":
            continue
        teamRating["values"][team] = [teamDict[name]["Name"], f"=E{team + 2}", teamDict[name]["Rating"], teamDict[name]["Games"]]

    services["rating"].spreadsheets().values().batchUpdate(spreadsheetId=sheet,
                                                           body={
                                                               "valueInputOption": "USER_ENTERED",
                                                               "data": [{
                                                                   "range": f'work!A2:D{len(teamRating["values"]) + 2}',
                                                                   "majorDimension": "ROWS",
                                                                   "values": teamRating["values"]}]}
                                                           ).execute()
    services["rating"].spreadsheets().values().batchUpdate(spreadsheetId=sheet,
                                                           body={"valueInputOption": "USER_ENTERED",
                                                                 "data": [{
                                                                     "range": f'matches!G{len(getMatches2["values"]) + 2}:K{len(getMatches2["values"]) + 2 + len(getMatches["values"]) + 2}',
                                                                     "majorDimension": "ROWS",
                                                                     "values": getMatches["values"]}]}
                                                           ).execute()
    services["rating"].spreadsheets().values().batchUpdate(spreadsheetId=sheet,
                                                           body={"valueInputOption": "USER_ENTERED",
                                                                 "data": [{
                                                                     "range": f'matches!A{2}:K{len(getMatches["values"]) + 2}',
                                                                     "majorDimension": "COLUMNS",
                                                                     "values": [[""] * len(getMatches["values"]),
                                                                                [""] * len(getMatches["values"]),
                                                                                [""] * len(getMatches["values"]),
                                                                                [""] * len(getMatches["values"]),
                                                                                [""] * len(getMatches["values"])]}]}
                                                           ).execute()
    print("Рейтинг просчитан. Иду на 3 часовой сон.")
