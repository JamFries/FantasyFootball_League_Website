from django.shortcuts import render

from espn_api.football import League
import pandas as pd

# Temporary solution: put your league_id, year, espn_s2 cookie, and swid cookie into the csv
# Later: Implement login system that can link separate leagues to one account, with leagues stored in database
login = pd.read_csv('C:/Users/jtfra/PycharmProjects/FantasyFootball_League_Website/Data/login.csv')

# defenseVsRB_data = pd.read_csv('C:/Users/jtfra/PycharmProjects/FantasyFootball_League_Website/Data/2020_DefenseVsRB.csv', header=[0,1])
# print(defenseVsRB_data)
# print(defenseVsRB_data.columns)
# print(defenseVsRB_data["FantasyperGame"])
# print(defenseVsRB_data["Tm", "Tm"])
# print(defenseVsRB_data["FantasyperGame", "FantPt"])

# Get player data
player_data = pd.read_csv('C:/Users/jtfra/PycharmProjects/FantasyFootball_League_Website/Data/2020_PlayerStats.csv', header=[0])
# Find ways to use this data to find meaningful conclusions in relation to a specific FF league
# VBD: Value Based Drafting
# VBD Baseline: 12th ranked QB, 24th ranked RB, 30th ranked WR, 12th ranked TE
# VBD Formula: (Fantasy points) - (Fantasy points of the baseline player)
# Its helps determine value due to position scarcity as opposed to overall number of fantasy points, which would just be QBs
# The cons of it being it ignores ADP of players when calculating value which can make it hard to draft big-value guys without reaching if you just follow this

# print(player_data['Player'])
# Cleanup the player name column
for index, row_series in player_data.iterrows():
    cutoff = row_series['Player'].find("*")
    if (cutoff != -1):
        player_data.at[index, 'Player'] = row_series['Player'][:cutoff]
    else:
        cutoff = row_series['Player'].find("\\")
        player_data.at[index, 'Player'] = row_series['Player'][:cutoff]
# print(player_data['Player'])


# print(player_data.loc[(player_data["FantPos"] == "RB") & (player_data["FantasyVBD"] > 0)])
# runningbacks_vbd = player_data.loc[(player_data["FantPos"] == "RB") & (player_data["FantasyVBD"] > 0)]
# for index, row_series in runningbacks_vbd.iterrows():
#     print("Player: "+ str(row_series["Player"]) + " | VBD: " + str(row_series['FantasyVBD']))

# print(runningbacks_vbd["Player"] + "VBD: " + str(runningbacks_vbd["FantasyVBD"]))


# Three separate baselines not included in dataset
# VORP: Value Over Replacement Player -> (Fantasy points) - (Fantasy points of top player on waivers)
# VOLS: Value Over Last Starter -> (Fantasy points) - (Fantasy points of last starting runningback) -> (as in a backup RB on an NFL team, not your FF team)
# VONA: Value Over Next Available -> (Fantasy points) - (Fantasy points of best RB at your next pick)

league = League(league_id=login['league_id'][0], year=login['year'][0], espn_s2=login['espn_s2'][0], swid=login['swid'][0])
print(league)

# # Save ActivityList_week1_2021 for testing purposes
# activity_week1 = league.recent_activity(500)
# # print(activity_week1)
# df = pd.DataFrame(activity_week1, columns=["activity"])
# df.to_csv('activityList_week1_2021.csv', index=False)

# Get boxscores for the most recent week (for the home page)
boxScores_currentWeek = league.box_scores(league.current_week)
games_currentWeek = []
for boxScore in boxScores_currentWeek:
    game = {
        'home_team': boxScore.home_team,
        'away_team': boxScore.away_team,
        'home_score': boxScore.home_score,
        'away_score': boxScore.away_score,
        'home_lineup': boxScore.home_lineup,
        'away_lineup': boxScore.away_lineup,
    }
    games_currentWeek.append(game)


# store epoch timestamps in milliseconds at the cutoff dates for each week
week1_dateCutoff = 1600127999000 # Sep 14, 2020
week2_dateCutoff = 1600732799000 # Sep 21, 2020
week3_dateCutoff = 1601337599000 # Sep 28, 2020
week4_dateCutoff = 1601942399000 # Oct 5, 2020
week5_dateCutoff = 1602633599000 # Oct 13, 2020
week6_dateCutoff = 1603151999000 # Oct 19, 2020
week7_dateCutoff = 1603756799000 # Oct 26, 2020
week8_dateCutoff = 1604361599000 # Nov 2, 2020
week9_dateCutoff = 1604966399000 # Nov 9, 2020
week10_dateCutoff = 1605571199000 # Nov 16, 2020
week11_dateCutoff = 1606175999000 # Nov 23, 2020
week12_dateCutoff = 1606953599000 # Dec 2, 2020
week13_dateCutoff = 1607471999000 # Dec 8, 2020
week14_dateCutoff = 1607990399000 # Dec 14, 2020
week15_dateCutoff = 1608595199000 # Dec 21, 2020
week16_dateCutoff = 1609199999000 # Dec 28, 2020
week17_dateCutoff = 1609718399000 # Jan 3, 2021
# Helper function that separates all league activity in their respective weeks of the season
def getActivitesByWeek(activies, week):
    retVal = []
    for a in activies:
        if (week == 1):
            if (a.date <= week1_dateCutoff):
                retVal.append(a)
        elif (week == 2):
            if ((a.date <= week2_dateCutoff) and (a.date > week1_dateCutoff)):
                retVal.append(a)
        elif (week == 3):
            if ((a.date <= week3_dateCutoff) and (a.date > week2_dateCutoff)):
                retVal.append(a)
        elif (week == 4):
            if ((a.date <= week4_dateCutoff) and (a.date > week3_dateCutoff)):
                retVal.append(a)
        elif (week == 5):
            if ((a.date <= week5_dateCutoff) and (a.date > week4_dateCutoff)):
                retVal.append(a)
        elif (week == 6):
            if ((a.date <= week6_dateCutoff) and (a.date > week5_dateCutoff)):
                retVal.append(a)
        elif (week == 7):
            if ((a.date <= week7_dateCutoff) and (a.date > week6_dateCutoff)):
                retVal.append(a)
        elif (week == 8):
            if ((a.date <= week8_dateCutoff) and (a.date > week7_dateCutoff)):
                retVal.append(a)
        elif (week == 9):
            if ((a.date <= week9_dateCutoff) and (a.date > week8_dateCutoff)):
                retVal.append(a)
        elif (week == 10):
            if ((a.date <= week10_dateCutoff) and (a.date > week9_dateCutoff)):
                retVal.append(a)
        elif (week == 11):
            if ((a.date <= week11_dateCutoff) and (a.date > week10_dateCutoff)):
                retVal.append(a)
        elif (week == 12):
            if ((a.date <= week12_dateCutoff) and (a.date > week11_dateCutoff)):
                retVal.append(a)
        elif (week == 13):
            if ((a.date <= week13_dateCutoff) and (a.date > week12_dateCutoff)):
                retVal.append(a)
        elif (week == 14):
            if ((a.date <= week14_dateCutoff) and (a.date > week13_dateCutoff)):
                retVal.append(a)
        elif (week == 15):
            if ((a.date <= week15_dateCutoff) and (a.date > week14_dateCutoff)):
                retVal.append(a)
        elif (week == 16):
            if ((a.date <= week16_dateCutoff) and (a.date > week15_dateCutoff)):
                retVal.append(a)
        elif (week == 17):
            if ((a.date <= week17_dateCutoff) and (a.date > week16_dateCutoff)):
                retVal.append(a)
        return retVal

def getStatsByWeek(league, week):
    boxScores = league.box_scores(week)
    weeklyStats = [] # List to store tuples of (Team, Score, Lineup) for that week
    for boxScore in boxScores:
        weeklyStats.append((boxScore.home_team, boxScore.home_score, boxScore.home_lineup))
        weeklyStats.append((boxScore.away_team, boxScore.away_score, boxScore.away_lineup))
    return weeklyStats

# Functions to calculate accolades per week rather than the entire season
def getTeamMostPoints(stats):
    maxScore = -1
    topTeam = (None, maxScore)
    for team, score, lineup in stats:
        if (score > maxScore):
            maxScore = score
            topTeam = (team, score)
    return topTeam

def getTeamLeastPoints(stats):
    minScore = 10000
    worstTeam = (None, minScore)
    for team, score, lineup in stats:
        if (score < minScore):
            minScore = score
            worstTeam = (team, score)
    return worstTeam

def getHighestScoringPlayer(stats):
    maxScore = -1
    topPlayer = (None, maxScore, None) # Tuple of player, player-score, team
    for team, score, lineup in stats:
        for player in lineup:
            if (player.points > maxScore):
                maxScore = player.points
                topPlayer = (player, player.points, team)
    return topPlayer

# Currently doesnt work. Does not correctly compare position with the player's position
def getHighestScoringPlayerByPosition(stats, position):
    maxScore = -1
    topPlayer = (None, maxScore, None) # Tuple of player, player-score, team
    for team, score, lineup in stats:
        for player in lineup:
            if (player.slot_position == position):
                if (player.points > maxScore):
                    maxScore = player.points
                    topPlayer = (player, player.points, team)
    return topPlayer

def getDraftPicksByRound(draft, round):
    retVal = []
    for pick in draft:
        if (pick.round_num == round):
            retVal.append(pick)
    return retVal

# Gather statistics by a specific week
teamStats_week1 = getStatsByWeek(league, 1)
teamStats_week2 = getStatsByWeek(league, 2)
teamStats_week3 = getStatsByWeek(league, 3)
teamStats_week4 = getStatsByWeek(league, 4)
teamStats_week5 = getStatsByWeek(league, 5)
teamStats_week6 = getStatsByWeek(league, 6)
teamStats_week7 = getStatsByWeek(league, 7)
teamStats_week8 = getStatsByWeek(league, 8)
teamStats_week9 = getStatsByWeek(league, 9)
teamStats_week10 = getStatsByWeek(league, 10)
teamStats_week11 = getStatsByWeek(league, 11)
teamStats_week12 = getStatsByWeek(league, 12)
teamStats_week13 = getStatsByWeek(league, 13)
teamStats_week14 = getStatsByWeek(league, 14)
teamStats_week15 = getStatsByWeek(league, 15)
teamStats_week16 = getStatsByWeek(league, 16)
teamStats_week17 = getStatsByWeek(league, 17)




# homepage will have a basic overview of the most recent week of the league
def home(request):
    context = {
        'games_currentWeek': games_currentWeek,
        'current_week': league.current_week,
    }
    return render(request, 'main/home.html', context)

# Weekly stats page will be a travel page to a specific week in the season
def weeklyStats(request):
    context = {
        'current_week': league.current_week,
    }
    return render(request, 'main/weeklyStats.html', context)

# Week is the base html page that shows details about a week in the season
# def week(request):
#     return render(request, 'main/week.html')

def week1(request):
    context = {
        'boxScores': league.box_scores(1),
        'power_rankings': league.power_rankings(1),
        'awards_mostPoints': getTeamMostPoints(teamStats_week1),
        'awards_leastPoints': getTeamLeastPoints(teamStats_week1),
        'awards_highestScoringPlayer': getHighestScoringPlayer(teamStats_week1),
        # 'activity': league.recent_activity(25),
        # 'week1_dateCutoff': week1_dateCutoff,
        'league': league,
    }
    return render(request, 'main/week1.html', context)

def week2(request):
    context = {
        'boxScores': league.box_scores(2),
        'power_rankings': league.power_rankings(2),
        'power_rankings_previousWeek': league.power_rankings(1),
        'awards_mostPoints': getTeamMostPoints(teamStats_week2),
        'awards_leastPoints': getTeamLeastPoints(teamStats_week2),
        'awards_highestScoringPlayer': getHighestScoringPlayer(teamStats_week2),
        # 'activity': league.recent_activity(25),
        # 'week1_dateCutoff': week1_dateCutoff,
        'league': league,
    }
    return render(request, 'main/week2.html', context)

def week3(request):
    context = {
        'boxScores': league.box_scores(3),
        'power_rankings': league.power_rankings(3),
        'power_rankings_previousWeek': league.power_rankings(2),
        'awards_mostPoints': getTeamMostPoints(teamStats_week3),
        'awards_leastPoints': getTeamLeastPoints(teamStats_week3),
        'awards_highestScoringPlayer': getHighestScoringPlayer(teamStats_week3),
        # 'activity': league.recent_activity(25),
        # 'week1_dateCutoff': week1_dateCutoff,
        'league': league,
    }
    return render(request, 'main/week3.html', context)

def week4(request):
    context = {
        'boxScores': league.box_scores(4),
        'power_rankings': league.power_rankings(4),
        'power_rankings_previousWeek': league.power_rankings(3),
        'awards_mostPoints': getTeamMostPoints(teamStats_week4),
        'awards_leastPoints': getTeamLeastPoints(teamStats_week4),
        'awards_highestScoringPlayer': getHighestScoringPlayer(teamStats_week4),
        # 'activity': league.recent_activity(25),
        # 'week1_dateCutoff': week1_dateCutoff,
        'league': league,
    }
    return render(request, 'main/week4.html', context)

def week5(request):
    context = {
        'boxScores': league.box_scores(5),
        'power_rankings': league.power_rankings(5),
        'power_rankings_previousWeek': league.power_rankings(4),
        'awards_mostPoints': getTeamMostPoints(teamStats_week5),
        'awards_leastPoints': getTeamLeastPoints(teamStats_week5),
        'awards_highestScoringPlayer': getHighestScoringPlayer(teamStats_week5),
        # 'activity': league.recent_activity(25),
        # 'week1_dateCutoff': week1_dateCutoff,
        'league': league,
    }
    return render(request, 'main/week5.html', context)

def week6(request):
    context = {
        'boxScores': league.box_scores(6),
        'power_rankings': league.power_rankings(6),
        'power_rankings_previousWeek': league.power_rankings(5),
        'awards_mostPoints': getTeamMostPoints(teamStats_week6),
        'awards_leastPoints': getTeamLeastPoints(teamStats_week6),
        'awards_highestScoringPlayer': getHighestScoringPlayer(teamStats_week6),
        # 'activity': league.recent_activity(25),
        # 'week1_dateCutoff': week1_dateCutoff,
        'league': league,
    }
    return render(request, 'main/week6.html', context)

def week7(request):
    context = {
        'boxScores': league.box_scores(7),
        'power_rankings': league.power_rankings(7),
        'power_rankings_previousWeek': league.power_rankings(6),
        'awards_mostPoints': getTeamMostPoints(teamStats_week7),
        'awards_leastPoints': getTeamLeastPoints(teamStats_week7),
        'awards_highestScoringPlayer': getHighestScoringPlayer(teamStats_week7),
        # 'activity': league.recent_activity(25),
        # 'week1_dateCutoff': week1_dateCutoff,
        'league': league,
    }
    return render(request, 'main/week7.html', context)

def week8(request):
    context = {
        'boxScores': league.box_scores(8),
        'power_rankings': league.power_rankings(8),
        'power_rankings_previousWeek': league.power_rankings(7),
        'awards_mostPoints': getTeamMostPoints(teamStats_week8),
        'awards_leastPoints': getTeamLeastPoints(teamStats_week8),
        'awards_highestScoringPlayer': getHighestScoringPlayer(teamStats_week8),
        # 'activity': league.recent_activity(25),
        # 'week1_dateCutoff': week1_dateCutoff,
        'league': league,
    }
    return render(request, 'main/week8.html', context)

def week9(request):
    context = {
        'boxScores': league.box_scores(9),
        'power_rankings': league.power_rankings(9),
        'power_rankings_previousWeek': league.power_rankings(8),
        'awards_mostPoints': getTeamMostPoints(teamStats_week9),
        'awards_leastPoints': getTeamLeastPoints(teamStats_week9),
        'awards_highestScoringPlayer': getHighestScoringPlayer(teamStats_week9),
        # 'activity': league.recent_activity(25),
        # 'week1_dateCutoff': week1_dateCutoff,
        'league': league,
    }
    return render(request, 'main/week9.html', context)

def week10(request):
    context = {
        'boxScores': league.box_scores(10),
        'power_rankings': league.power_rankings(10),
        'power_rankings_previousWeek': league.power_rankings(9),
        'awards_mostPoints': getTeamMostPoints(teamStats_week10),
        'awards_leastPoints': getTeamLeastPoints(teamStats_week10),
        'awards_highestScoringPlayer': getHighestScoringPlayer(teamStats_week10),
        # 'activity': league.recent_activity(25),
        # 'week1_dateCutoff': week1_dateCutoff,
        'league': league,
    }
    return render(request, 'main/week10.html', context)

def week11(request):
    context = {
        'boxScores': league.box_scores(11),
        'power_rankings': league.power_rankings(11),
        'power_rankings_previousWeek': league.power_rankings(10),
        'awards_mostPoints': getTeamMostPoints(teamStats_week11),
        'awards_leastPoints': getTeamLeastPoints(teamStats_week11),
        'awards_highestScoringPlayer': getHighestScoringPlayer(teamStats_week11),
        # 'activity': league.recent_activity(25),
        # 'week1_dateCutoff': week1_dateCutoff,
        'league': league,
    }
    return render(request, 'main/week11.html', context)

def week12(request):
    context = {
        'boxScores': league.box_scores(12),
        'power_rankings': league.power_rankings(12),
        'power_rankings_previousWeek': league.power_rankings(11),
        'awards_mostPoints': getTeamMostPoints(teamStats_week12),
        'awards_leastPoints': getTeamLeastPoints(teamStats_week12),
        'awards_highestScoringPlayer': getHighestScoringPlayer(teamStats_week12),
        # 'activity': league.recent_activity(25),
        # 'week1_dateCutoff': week1_dateCutoff,
        'league': league,
    }
    return render(request, 'main/week12.html', context)

def week13(request):
    context = {
        'boxScores': league.box_scores(13),
        'power_rankings': league.power_rankings(13),
        'power_rankings_previousWeek': league.power_rankings(12),
        'awards_mostPoints': getTeamMostPoints(teamStats_week13),
        'awards_leastPoints': getTeamLeastPoints(teamStats_week13),
        'awards_highestScoringPlayer': getHighestScoringPlayer(teamStats_week13),
        # 'activity': league.recent_activity(25),
        # 'week1_dateCutoff': week1_dateCutoff,
        'league': league,
    }
    return render(request, 'main/week13.html', context)

def week14(request):
    context = {
        'boxScores': league.box_scores(14),
        'power_rankings': league.power_rankings(14),
        'power_rankings_previousWeek': league.power_rankings(13),
        'awards_mostPoints': getTeamMostPoints(teamStats_week14),
        'awards_leastPoints': getTeamLeastPoints(teamStats_week14),
        'awards_highestScoringPlayer': getHighestScoringPlayer(teamStats_week14),
        # 'activity': league.recent_activity(25),
        # 'week1_dateCutoff': week1_dateCutoff,
        'league': league,
    }
    return render(request, 'main/week14.html', context)

def week15(request):
    context = {
        'boxScores': league.box_scores(15),
        'power_rankings': league.power_rankings(15),
        'power_rankings_previousWeek': league.power_rankings(14),
        'awards_mostPoints': getTeamMostPoints(teamStats_week15),
        'awards_leastPoints': getTeamLeastPoints(teamStats_week15),
        'awards_highestScoringPlayer': getHighestScoringPlayer(teamStats_week15),
        # 'activity': league.recent_activity(25),
        # 'week1_dateCutoff': week1_dateCutoff,
        'league': league,
    }
    return render(request, 'main/week15.html', context)

def week16(request):
    context = {
        'boxScores': league.box_scores(16),
        'power_rankings': league.power_rankings(16),
        'power_rankings_previousWeek': league.power_rankings(15),
        'awards_mostPoints': getTeamMostPoints(teamStats_week16),
        'awards_leastPoints': getTeamLeastPoints(teamStats_week16),
        'awards_highestScoringPlayer': getHighestScoringPlayer(teamStats_week16),
        # 'activity': league.recent_activity(25),
        # 'week1_dateCutoff': week1_dateCutoff,
        'league': league,
    }
    return render(request, 'main/week16.html', context)

def week17(request):
    context = {
        'boxScores': league.box_scores(17),
        'power_rankings': league.power_rankings(17),
        'power_rankings_previousWeek': league.power_rankings(16),
        'awards_mostPoints': getTeamMostPoints(teamStats_week17),
        'awards_leastPoints': getTeamLeastPoints(teamStats_week17),
        'awards_highestScoringPlayer': getHighestScoringPlayer(teamStats_week17),
        # 'activity': league.recent_activity(25),
        # 'week1_dateCutoff': week1_dateCutoff,
        'league': league,
    }
    return render(request, 'main/week17.html', context)

# teampage will have a description of each team in the league
def teams(request):
    context = {
        'teams': league.teams,
        'players': player_data,
    }
    return render(request, 'main/teams.html', context)

def draft(request):
    context = {
        'draft_round1': getDraftPicksByRound(league.draft, 1),
        'draft_round2': getDraftPicksByRound(league.draft, 2),
        'draft_round3': getDraftPicksByRound(league.draft, 3),
        'draft_round4': getDraftPicksByRound(league.draft, 4),
        'draft_round5': getDraftPicksByRound(league.draft, 5),
        'draft_round6': getDraftPicksByRound(league.draft, 6),
        'draft_round7': getDraftPicksByRound(league.draft, 7),
        'draft_round8': getDraftPicksByRound(league.draft, 8),
        'draft_round9': getDraftPicksByRound(league.draft, 9),
        'draft_round10': getDraftPicksByRound(league.draft, 10),
        'draft_round11': getDraftPicksByRound(league.draft, 11),
        'draft_round12': getDraftPicksByRound(league.draft, 12),
        # 'draft': league.draft,
    }
    return render(request, 'main/draft.html', context)

def about(request):
    return render(request, 'main/about.html')