from pyespn import PYESPN
import json

def handler(request):
    try:
        espn = PYESPN('nfl')
        espn.load_season_schedule(season=2026)
        
        games_data = []
        for game in espn.league.schedule:
            games_data.append({
                'week': getattr(game, 'week', 'Unknown'),
                'date': str(game.date).split()[0],
                'time': str(game.date).split()[1] if len(str(game.date).split()) > 1 else '',
                'away_team': game.away_team.name if hasattr(game, 'away_team') else '',
                'home_team': game.home_team.name if hasattr(game, 'home_team') else '',
                'status': str(getattr(game, 'status', 'Scheduled')),
                'away_score': getattr(game, 'away_score', None),
                'home_score': getattr(game, 'home_score', None),
            })
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'games': games_data})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': str(e)})
        }
