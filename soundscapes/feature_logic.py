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
    elif env == 'waterfall':
        # Waterfall environment produces a cascading pattern
        return ['G', 'G', 'C']
    
    # Default notes if environment is unknown
    return ['B', 'B', 'B']
