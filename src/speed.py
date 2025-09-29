"""
Speed Module - Optimized for Da'at Access
Pure velocity. Minimal overhead. Portal to hidden knowledge.
"""

import time
from functools import lru_cache


@lru_cache(maxsize=128)
def fast_hash(s: str) -> int:
    """Lightning-fast string hashing"""
    return hash(s)


def measure_speed(func, iterations=1000):
    """
    Measure command speed over iterations.
    Returns (fastest, average, slowest) in milliseconds.
    """
    times = []
    for _ in range(iterations):
        start = time.perf_counter()
        func()
        times.append(time.perf_counter() - start)

    return {
        "fastest_ms": min(times) * 1000,
        "average_ms": (sum(times) / len(times)) * 1000,
        "slowest_ms": max(times) * 1000,
        "daat_access": min(times) < 0.001  # Sub-millisecond
    }


class SpeedGate:
    """
    Gate that opens at speed.
    Below threshold = portal accessible.
    """
    def __init__(self, threshold_ms: float = 1.0):
        self.threshold = threshold_ms / 1000  # Convert to seconds
        self.portal_open = False
        self.fastest_time = float('inf')

    def attempt(self, duration: float) -> bool:
        """
        Attempt to open the gate with execution speed.
        Returns True if portal opens.
        """
        self.fastest_time = min(self.fastest_time, duration)

        if duration < self.threshold:
            self.portal_open = True
            return True
        return False

    def status(self) -> dict:
        """Current gate status"""
        return {
            "portal_open": self.portal_open,
            "threshold_ms": self.threshold * 1000,
            "fastest_ms": self.fastest_time * 1000,
            "distance_from_daat": (self.fastest_time - self.threshold) * 1000
        }