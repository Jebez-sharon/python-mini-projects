from nba_api.stats.endpoints import ScoreboardV2

def get_scoreboard():
    try:
        scoreboard = ScoreboardV2()

        games = scoreboard.get_data_frames()[0]

        if games.empty:
            print("No games available today.")
            return

        print("=" * 60)

        for _, game in games.iterrows():
            home = game["HOME_TEAM_ABBREVIATION"]
            away = game["VISITOR_TEAM_ABBREVITATION"]

            print(f"{away} vs {home}")

        print("=" * 60)

    except Exception as e:
        print(e)