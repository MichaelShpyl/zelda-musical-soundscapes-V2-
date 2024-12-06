import pytest
from soundscapes.feature_logic import generate_soundscape

def test_forest_soundscape():
    assert generate_soundscape('forest') == ['C', 'E', 'G']

def test_cave_soundscape():
    assert generate_soundscape('cave') == ['D', 'F', 'A']

def test_waterfall_soundscape():
    assert generate_soundscape('waterfall') == ['G', 'G', 'C']


def test_unknown_environment():
    assert generate_soundscape('desert') == ['B', 'B', 'B']
