#!/usr/bin/env python3
"""Select random scene plans for fashion try-on batches."""

from __future__ import annotations

import argparse
import json
import random
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
SCENE_BANK = SKILL_DIR / "references" / "scene-bank.json"


def load_scenes() -> list[dict]:
    with SCENE_BANK.open("r", encoding="utf-8") as f:
        scenes = json.load(f)
    if not isinstance(scenes, list):
        raise ValueError("scene-bank.json must contain a list")
    return scenes


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Select unique try-on scenes.")
    parser.add_argument("--count", type=int, default=30, help="Number of scenes to select.")
    parser.add_argument("--seed", default=None, help="Optional random seed for repeatability.")
    parser.add_argument("--category", action="append", default=[], help="Allowed category; repeatable.")
    parser.add_argument("--exclude", action="append", default=[], help="Scene slug to exclude; repeatable.")
    parser.add_argument("--format", choices=["json", "markdown"], default="json")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    scenes = load_scenes()

    categories = set(args.category)
    excludes = set(args.exclude)
    filtered = [
        scene
        for scene in scenes
        if scene.get("slug") not in excludes
        and (not categories or scene.get("category") in categories)
    ]

    if args.count < 1:
        raise SystemExit("--count must be at least 1")
    if args.count > len(filtered):
        raise SystemExit(
            f"Requested {args.count} scenes, but only {len(filtered)} scenes match filters."
        )

    rng = random.Random(args.seed)
    selected = rng.sample(filtered, args.count)

    if args.format == "json":
        print(json.dumps(selected, ensure_ascii=False, indent=2))
    else:
        for index, scene in enumerate(selected, start=1):
            print(
                f"{index:02d}. {scene['slug']} "
                f"({scene['category']}): {scene['description']}"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
