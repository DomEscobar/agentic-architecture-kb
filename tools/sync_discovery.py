#!/usr/bin/env python3
"""Download and verify the current non-canonical discovery snapshot."""

import argparse
import os

from discovery_cache import DEFAULT_SNAPSHOT_URL, sync_snapshot


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", default=os.getenv("AI_ARCHITECT_DISCOVERY_SNAPSHOT_URL", DEFAULT_SNAPSHOT_URL))
    parser.add_argument("--timeout", type=float, default=30.0)
    args = parser.parse_args()
    artifact = sync_snapshot(args.url, timeout=args.timeout)
    print(f"Verified discovery snapshot: {artifact}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
