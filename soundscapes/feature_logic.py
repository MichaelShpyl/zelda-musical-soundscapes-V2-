"""
Core logic for generating musical soundscapes.
For now, this is a simple placeholder that returns a list of notes based on the environment.
"""

def generate_soundscape(environment: str):
    if environment == 'forest':
        return ['C', 'E', 'G']
    elif environment == 'cave':
        return ['D', 'F', 'A']
    elif environment == 'waterfall':
        return ['G', 'G', 'C']
    else:
        return ['B', 'B', 'B']

