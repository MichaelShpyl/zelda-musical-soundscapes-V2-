def generate_soundscape(env: str):
    # If env is empty, return a default pattern
    if env.strip() == '':
        # Let's go super simple if they didn't specify anything
        # Just a soothing all-C triad
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
