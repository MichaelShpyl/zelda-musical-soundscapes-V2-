"""
feature_logic.py - Contains logic for generating soundscapes based on the given environment.
"""

def generate_soundscape(env: str):
    """
    Return a list of musical notes based on the provided environment.
    """
    if env == 'forest':
        return ['C', 'E', 'G']
    elif env == 'cave':
        return ['D', 'F', 'A']
    elif env == 'waterfall':
        return ['G', 'G', 'C']
    return ['B', 'B', 'B']
