import time
from soundscapes.feature_logic import generate_soundscape

def test_performance():
    start = time.time()
    for _ in range(10000):
        generate_soundscape('forest')
    end = time.time()
    assert (end - start) < 0.5, "Performance test failed: Took too long!"
