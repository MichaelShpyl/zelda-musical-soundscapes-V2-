"""
<<<<<<< HEAD
feature_logic.py - Core logic for generating musical soundscapes.

=======
feature_logic.py - Logic to generate musical soundscapes based on environment.
We use simple logic: each environment returns a different triad of notes.
This is a core function tested by unit tests and measured by performance tests.
Docstrings used by pdoc for auto doc generation.
>>>>>>> ef43be7 (feat: Finalize infrastructure, add performance tests, bandit security checks, docs, and CI updates for eu-west-1)
"""

def generate_soundscape(env: str) -> list[str]:
    """
<<<<<<< HEAD
    Generate a list of musical notes based on the provided environment.

    Args:
        env (str): The environment type, for example "forest", "cave", "waterfall", or "mountain".
                   Passing an empty string defaults to a safe fallback pattern.

    Returns:
        list[str]: A list of notes that represent the soundscape for the specified environment.

=======
    Generate a list of musical notes based on the given environment.

    Args:
        env (str): environment name ('forest', 'cave', 'waterfall', 'mountain', or empty)
                   Empty means a default pattern (C, C, C).

    Returns:
        list[str]: The notes representing the soundscape.
>>>>>>> ef43be7 (feat: Finalize infrastructure, add performance tests, bandit security checks, docs, and CI updates for eu-west-1)
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

    # For unknown environments, return a fallback pattern.
    return ['B', 'B', 'B']
