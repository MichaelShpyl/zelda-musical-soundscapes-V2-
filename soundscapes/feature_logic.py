"""
feature_logic.py - Core logic for generating musical soundscapes.

"""

def generate_soundscape(env: str) -> list[str]:
    """
    Generate a list of musical notes based on the provided environment.

    Args:
        env (str): The environment type, for example "forest", "cave", "waterfall", or "mountain".
                   Passing an empty string defaults to a safe fallback pattern.

    Returns:
        list[str]: A list of notes that represent the soundscape for the specified environment.

    """
    if env.strip() == '':
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
