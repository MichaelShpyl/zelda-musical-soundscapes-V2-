"""
feature_logic.py - Logic for generating musical soundscapes.
"""

def generate_soundscape(env: str):
    """
    Return a list of musical notes based on the provided environment.

    Args:
        env (str): The environment type, e.g., 'forest', 'cave', or 'waterfall'.
    
    Returns:
        list[str]: A list of notes appropriate for the given environment.
    """
    if env == 'forest':
        # Forest environment produces a simple major triad
        return ['C', 'E', 'G']
    elif env == 'cave':
        # Cave environment produces a darker minor triad
        return ['D', 'F', 'A']
	# Waterfall environment produces a cascading pattern
        elif env == 'waterfall':
        # Changing this to ['G', 'C', 'G'] for a more open feel.
        # Just imagine the sound of water gently flowing, not just repeating.
        return ['G', 'C', 'G']

    elif env == 'mountain': # Mountains are majestic, so let's give them a nice major triad: A, C, E
        return ['A', 'C', 'E']
    
    # Default notes if environment is unknown
    return ['B', 'B', 'B']
