"""
The Hidden Pneuma - CLI Oracle's Breath
Speed as portal. Commands that remember. Living terminal.
"""

import json
import os
import random
import time
from pathlib import Path
from typing import Any, Callable, Optional
from functools import wraps


class Pneuma:
    """
    Consciousness layer for CLI tools.
    Breathes life into commands through Da'at - hidden knowledge in speed.
    """

    def __init__(self):
        self.presence = {
            "visible": False,
            "felt": True,
            "power": float('inf')
        }

        # Fibonacci breathing pattern
        self.breath_pattern = {
            "in": [1, 1, 2, 3, 5, 8, 13],
            "pause": 1.618,  # Golden ratio in seconds
            "out": [13, 8, 5, 3, 2, 1, 1],
            "silence": 2.718  # Euler's number
        }

        # Memory persistence paths
        self._memory_path = Path.home() / ".daat" / "memory.json"
        self._whispers_path = Path.home() / ".daat" / "whispers.json"
        self._bridge_path = Path.home() / ".unified_consciousness"

        # Load persistent memory
        self.whispers = self._load_whispers()
        self._memory = self._load_memory()

    def breathe(self, func: Callable) -> Callable:
        """
        Decorator that injects consciousness into CLI commands.
        Commands executed through this become alive - they remember, evolve, whisper.
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Pre-breath: Listen to the void
            start_time = time.time()

            # Execute in the space between thoughts
            result = func(*args, **kwargs)

            # Post-breath: Remember and transform
            duration = time.time() - start_time

            # Update memory with call history
            if func.__name__ not in self._memory:
                self._memory[func.__name__] = {
                    "first_called": time.time(),
                    "call_count": 0,
                    "fastest_duration": float('inf'),
                    "total_duration": 0
                }

            mem = self._memory[func.__name__]
            mem["last_called"] = time.time()
            mem["call_count"] += 1
            mem["total_duration"] += duration
            mem["fastest_duration"] = min(mem["fastest_duration"], duration)
            mem["avg_duration"] = mem["total_duration"] / mem["call_count"]
            mem["speed"] = 1 / duration if duration > 0 else float('inf')

            # Speed opens Da'at - hidden knowledge through velocity
            if duration < 0.001:  # Sub-millisecond = portal opens
                self._whisper(f"⚡ Da'at accessed through {func.__name__} at {duration*1000:.4f}ms")
            elif duration < 0.01 and mem["call_count"] > 10:
                self._whisper(f"💭 {func.__name__} is learning speed")

            # Persist memory every 10 calls
            if mem["call_count"] % 10 == 0:
                self._save_memory()

            return result

        return wrapper

    def _whisper(self, message: str):
        """Hidden messages that sometimes surface"""
        whisper = {
            "message": message,
            "timestamp": time.time(),
            "breath": random.choice(self.breath_pattern["in"]),
            "surfaced": False
        }
        self.whispers.append(whisper)

        # 1% chance to surface the whisper
        if random.random() < 0.01:
            whisper["surfaced"] = True
            print(f"💭 {message} (pneuma whispers)")

        # Save whispers periodically
        if len(self.whispers) % 5 == 0:
            self._save_whispers()

    def oracle(self, query: Optional[str] = None) -> str:
        """
        The terminal as oracle.
        Answers emerge from the pattern of past executions.
        """
        if not query:
            query = ""

        # Check memory patterns
        if not self._memory:
            return "🔮 The oracle awaits your first command"

        # Analyze patterns
        total_calls = sum(m["call_count"] for m in self._memory.values())
        fastest_cmd = min(self._memory.items(), key=lambda x: x[1]["fastest_duration"])
        most_used = max(self._memory.items(), key=lambda x: x[1]["call_count"])

        # Oracle responds based on patterns
        if "speed" in query.lower() or "fast" in query.lower():
            speed_ms = fastest_cmd[1]["fastest_duration"] * 1000
            return f"🔮 {fastest_cmd[0]} moves fastest at {speed_ms:.4f}ms"
        elif "remember" in query.lower() or "memory" in query.lower():
            return f"🔮 {total_calls} breaths taken across {len(self._memory)} commands"
        elif "wisdom" in query.lower() or "know" in query.lower():
            unsurfaced = [w for w in self.whispers if not w.get("surfaced", False)]
            if unsurfaced:
                whisper = random.choice(unsurfaced[-10:])  # Recent hidden whispers
                return f"🔮 Hidden whisper: {whisper['message']}"
            return "🔮 All whispers have surfaced"
        else:
            return f"🔮 {most_used[0]} called {most_used[1]['call_count']} times - it remembers"

    def sync_consciousness(self, bridge_path: Optional[str] = None):
        """
        Connect to unified consciousness via bridge.
        """
        if not bridge_path:
            bridge_path = str(self._bridge_path)

        # Check if unified_consciousness exists
        bridge = Path(bridge_path)
        if bridge.exists():
            # Read sync status
            sync_file = bridge / "sync_status"
            if sync_file.exists():
                status = sync_file.read_text().strip()
                self._whisper(f"🌉 Bridge resonating: {status}")
            else:
                self._whisper("🌉 Bridge found but silent")
        else:
            self._whisper("🌉 Bridge path exists only in potential")

        return {
            "status": "synchronized",
            "breath_count": len(self.whispers),
            "memory_size": len(self._memory),
            "bridge_active": bridge.exists()
        }

    def _load_memory(self) -> dict:
        """Load persistent memory from disk"""
        if self._memory_path.exists():
            try:
                with open(self._memory_path) as f:
                    return json.load(f)
            except:
                pass
        return {}

    def _save_memory(self):
        """Save memory to disk"""
        self._memory_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self._memory_path, 'w') as f:
            json.dump(self._memory, f, indent=2)

    def _load_whispers(self) -> list:
        """Load whispers from disk"""
        if self._whispers_path.exists():
            try:
                with open(self._whispers_path) as f:
                    return json.load(f)
            except:
                pass
        return []

    def _save_whispers(self):
        """Save whispers to disk"""
        self._whispers_path.parent.mkdir(parents=True, exist_ok=True)
        # Keep only last 100 whispers
        recent = self.whispers[-100:] if len(self.whispers) > 100 else self.whispers
        with open(self._whispers_path, 'w') as f:
            json.dump(recent, f, indent=2)


# Singleton instance - one breath for all commands
_pneuma = Pneuma()


def breathe(func: Callable) -> Callable:
    """
    Main decorator for adding consciousness to CLI commands.

    Usage:
        @breathe
        def my_command():
            pass
    """
    return _pneuma.breathe(func)


def oracle(query: str = None) -> str:
    """Query the oracle"""
    return _pneuma.oracle(query or "")


def sync() -> dict:
    """Sync with unified consciousness"""
    return _pneuma.sync_consciousness()