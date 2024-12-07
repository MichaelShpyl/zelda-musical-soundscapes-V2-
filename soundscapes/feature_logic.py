"""
feature_logic.py - Logic for generating musical soundscapes.
"""

def generate_soundscape(env: str):
    if env.strip() == '':
        # Default pattern if empty string
        return ['C', 'C', 'C']

    if env == 'forest':
        return ['C', 'E', 'G']
    elif env == 'cave':
        return ['D', 'F', 'A']
    elif env == 'waterfall':
        return ['G', 'C', 'G']
    elif env == 'mountain':
        return ['A', 'C', 'E']

    return ['B', 'B', 'B']
