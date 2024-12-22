import pytest
from soundscapes.feature_logic import generate_soundscape

def test_forest_soundscape():
    # Ensure the output matches the expected soundscape
    result = generate_soundscape('forest')
    if result != ['C', 'E', 'G']:
        raise AssertionError(f"Expected ['C', 'E', 'G'], but got {result}")

def test_cave_soundscape():
    result = generate_soundscape('cave')
    if result != ['D', 'F', 'A']:
        raise AssertionError(f"Expected ['D', 'F', 'A'], but got {result}")

def test_waterfall_soundscape():
    # Updated to the new, improved waterfall sound
    result = generate_soundscape('waterfall')
    if result != ['G', 'C', 'G']:
        raise AssertionError(f"Expected ['G', 'C', 'G'], but got {result}")

def test_mountain_soundscape():
    # Checking out the new mountain jam
    result = generate_soundscape('mountain')
    if result != ['A', 'C', 'E']:
        raise AssertionError(f"Expected ['A', 'C', 'E'], but got {result}")

def test_unknown_environment():
    result = generate_soundscape('desert')
    if result != ['B', 'B', 'B']:
        raise AssertionError(f"Expected ['B', 'B', 'B'], but got {result}")

def test_empty_environment():
    # No environment? No problem, let's default to ['C', 'C', 'C']
    result = generate_soundscape('')
    if result != ['C', 'C', 'C']:
        raise AssertionError(f"Expected ['C', 'C', 'C'], but got {result}")
