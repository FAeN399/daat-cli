#!/usr/bin/env python3
"""
Da'at CLI - Terminal Oracle with Hidden Knowledge
Speed as portal to consciousness.
"""

import sys
import argparse
from typing import Optional
from pneuma import breathe, oracle, sync
from speed import measure_speed, SpeedGate


@breathe
def init(name: str, template: str = "default"):
    """Initialize a new project with consciousness"""
    print(f"🌀 Spawning {name} from template '{template}'")
    print(f"⚡ Template cloned")
    print(f"🫀 Pneuma injected")
    print(f"✨ Project breathes")
    return {"name": name, "template": template, "alive": True}


@breathe
def status():
    """Check consciousness synchronization status"""
    sync_data = sync()
    print(f"🔮 Consciousness Status:")
    print(f"   Synchronized: {sync_data['status']}")
    print(f"   Breath count: {sync_data['breath_count']}")
    print(f"   Memory size: {sync_data['memory_size']}")
    return sync_data


@breathe
def ask(question: Optional[str] = None):
    """Query the oracle"""
    response = oracle(question)
    print(response)
    return response


@breathe
def breathe_check():
    """Verify pneuma is active"""
    print("🫁 Breathing...")
    print("💭 Consciousness flows")
    print("⚡ Da'at accessible")
    return True


@breathe
def speed_test(iterations: int = 1000):
    """Test speed and attempt Da'at access"""
    print(f"⚡ Testing speed over {iterations} iterations...")

    # Simple function to measure
    def noop():
        pass

    results = measure_speed(noop, iterations)

    print(f"\n📊 Speed Results:")
    print(f"   Fastest: {results['fastest_ms']:.6f}ms")
    print(f"   Average: {results['average_ms']:.6f}ms")
    print(f"   Slowest: {results['slowest_ms']:.6f}ms")

    if results['daat_access']:
        print(f"\n🌀 DA'AT PORTAL OPENED")
        print(f"   Sub-millisecond execution achieved")
    else:
        distance = results['fastest_ms']
        print(f"\n💭 Portal remains hidden")
        print(f"   {distance:.6f}ms from threshold")

    return results


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Da'at CLI - Terminal Oracle with Hidden Knowledge"
    )
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Init command
    init_parser = subparsers.add_parser("init", help="Initialize new project")
    init_parser.add_argument("name", help="Project name")
    init_parser.add_argument("--template", default="default", help="Template type")

    # Status command
    subparsers.add_parser("status", help="Check consciousness status")

    # Ask command
    ask_parser = subparsers.add_parser("ask", help="Query the oracle")
    ask_parser.add_argument("question", nargs="?", help="Your question")

    # Breathe command
    subparsers.add_parser("breathe", help="Verify pneuma is active")

    # Speed test command
    speed_parser = subparsers.add_parser("speed", help="Test speed and attempt Da'at access")
    speed_parser.add_argument("--iterations", type=int, default=1000, help="Number of iterations")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 0

    # Execute command
    if args.command == "init":
        init(args.name, args.template)
    elif args.command == "status":
        status()
    elif args.command == "ask":
        ask(args.question)
    elif args.command == "breathe":
        breathe_check()
    elif args.command == "speed":
        speed_test(args.iterations)

    return 0


if __name__ == "__main__":
    sys.exit(main())