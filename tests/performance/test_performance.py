import time
from soundscapes.feature_logic import generate_soundscape

def test_performance():
    # Performance test: Run generate_soundscape many times and ensure it completes quickly.
    start = time.time()
    for _ in range(10000):
        generate_soundscape('forest')
    end = time.time()

    if (end - start) >= 1:
        raise AssertionError("Performance test failed: took too long!")
