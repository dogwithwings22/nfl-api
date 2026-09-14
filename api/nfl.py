from http.server import BaseHTTPRequestHandler
import json
from pyespn import PYESPN

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            away = self.path.split('away=')[1].split('&')[0] if 'away=' in self.path else ''
            home = self.path.split('home=')[1].split('&')[0] if 'home=' in self.path else ''
            
            espn = PYESPN('nfl')
            espn.load_season_schedule(season=2026)
            
            games_data = []
            for game in espn.league.schedule:
                if away in game.away_team.name or home in game.home_team.name:
                    games_data.append({
                        'away': game.away_team.name,
                        'home': game.home_team.name,
                        'date': str(game.date),
                        'status': game.status,
                        'away_score': getattr(game, 'away_score', None),
                        'home_score': getattr(game, 'home_score', None),
                    })
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'games': games_data}).encode())
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'error': str(e)}).encode())
