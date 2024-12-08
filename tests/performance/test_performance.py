import time
from soundscapes.feature_logic import generate_soundscape

def test_performance():
    # Performance test: Run generate_soundscape many times and ensure it completes quickly.
    # This checks if my code is efficient enough for large-scale use.
    start = time.time()
    for _ in range(10000):
        generate_soundscape('forest')
    end = time.time()

    # For a simple function, 10000 iterations should be < 1s on CI environment
    assert (end - start) < 1, "Performance test failed: took too long!"
