from nba_api.stats.endpoints import LeagueLeaders

def get_stats():
    leaders = LeagueLeaders()
    df = leaders.get_data_frames()[0]

    print("=" * 60)

    for i , row in df.head(20).iterrows():
        player = row["PLAYER"]
        team = row["TEAM"]
        pts = row["PTS"]

        print(f"{i+1}. {player:25} {team:5} {pts}")

    print("=" * 60)

