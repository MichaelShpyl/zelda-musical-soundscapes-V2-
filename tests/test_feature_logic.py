import pytest
from soundscapes.feature_logic import generate_soundscape

def test_forest_soundscape():
    assert generate_soundscape('forest') == ['C', 'E', 'G']

def test_cave_soundscape():
    assert generate_soundscape('cave') == ['D', 'F', 'A']

def test_waterfall_soundscape():
    # Updated to the new, improved waterfall sound
    assert generate_soundscape('waterfall') == ['G', 'C', 'G']


def test_mountain_soundscape():
    # Checking out the new mountain jam
    assert generate_soundscape('mountain') == ['A', 'C', 'E']


def test_unknown_environment():
    assert generate_soundscape('desert') == ['B', 'B', 'B']
