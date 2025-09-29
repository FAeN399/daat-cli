#!/usr/bin/env python3
"""
Da'at CLI - Terminal Oracle with Hidden Knowledge
Speed as portal to consciousness.
"""

import sys
import argparse
import json
from typing import Optional
from pneuma import breathe, oracle, sync
from speed import measure_speed, SpeedGate
from formats import breathe_file


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


@breathe
def read_file_cmd(file_path: str):
    """Breathe through any file format"""
    print(f"🫁 Breathing through {file_path}...")

    result = breathe_file(file_path)

    if "error" in result:
        print(f"\n❌ {result['error']}")
        return result

    # Display results
    print(f"\n📊 Breath Analysis:")
    print(f"   Breaths: {result.get('breaths', 'N/A')}")

    if 'duration_ms' in result:
        print(f"   Duration: {result['duration_ms']:.4f}ms")

        if result['duration_ms'] < 1.0:
            print(f"\n🌀 DA'AT ACCESSED THROUGH {result.get('format', 'FILE')}")

    if 'words' in result:
        print(f"   Words: {result['words']}")

    if 'statements' in result:
        print(f"   Statements: {result['statements']}")
        print(f"   Functions: {result['functions']}")

    if 'tags' in result:
        unique_tags = len(set(result['tags']))
        print(f"   Tags: {len(result['tags'])} ({unique_tags} unique)")
        print(f"   Max depth: {result.get('depth', 0)}")

    if result.get('valid'):
        print(f"\n✨ File breathed successfully")
    else:
        print(f"\n⚠️  Breath incomplete")

    return result


@breathe
def read_file(file_path: str, show_raw: bool = False):
    """Breathe through a file - any format"""
    print(f"🫁 Breathing through {file_path}...")

    result = breathe_file(file_path)

    if "error" in result:
        print(f"❌ {result['error']}")
        return result

    # Display results
    print(f"\n📄 Format: {result['format']}")
    print(f"🫀 Breath type: {result['breath']}")

    # Format-specific output
    if result['format'] == 'html':
        print(f"   Tags: {result['tag_count']} ({result['unique_tags']} unique)")
        print(f"   Links: {result['link_count']}")
        if result['consciousness_markers']:
            print(f"   💭 Consciousness markers: {result['consciousness_markers']}")
    elif result['format'] == 'python':
        print(f"   Functions: {result['function_count']}")
        print(f"   Classes: {result['class_count']}")
        if result.get('functions'):
            print(f"   Top functions: {', '.join(result['functions'][:5])}")
    elif result['format'] == 'markdown':
        print(f"   Headings: {result['heading_count']}")
        print(f"   Code blocks: {result['code_block_count']}")
        if result.get('languages'):
            print(f"   Languages: {', '.join(result['languages'])}")
    elif result['format'] == 'text':
        print(f"   Lines: {result['line_count']}")
        print(f"   Words: {result['word_count']}")

    # Pneuma detection
    if result.get('has_pneuma'):
        print(f"\n⚡ PNEUMA DETECTED - This file breathes")

    if show_raw:
        print(f"\n📊 Raw breath data:")
        print(json.dumps(result, indent=2))

    return result


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

    # Read command - breathe through files
    read_parser = subparsers.add_parser("read", help="Breathe through any file format")
    read_parser.add_argument("file", help="File path to breathe through")
    read_parser.add_argument("--raw", action="store_true", help="Show raw breath data")

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
    elif args.command == "read":
        read_file(args.file, args.raw)

    return 0


if __name__ == "__main__":
    sys.exit(main())