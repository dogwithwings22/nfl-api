import json
import os

def handler(request):
    try:
        # Lê o ficheiro JSON estático
        with open(os.path.join(os.path.dirname(__file__), '../public/games.json'), 'r') as f:
            games = json.load(f)
        
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps(games)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': str(e)})
        }
