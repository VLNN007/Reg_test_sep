#!/usr/bin/env python3

import sys
import subprocess


def check_disk_usage(sid):
    print(f"\nChecking disk usage for SID: {sid}")
    print("=" * 60)

    try:
        result = subprocess.run(
            ["df", "-h"],
            capture_output=True,
            text=True,
            check=True
        )

        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Error executing df -h: {e}")
        sys.exit(1)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <SID>")
        print(f"Example: {sys.argv[0]} ABC")
        sys.exit(1)

    sid = sys.argv[1].upper()

    check_disk_usage(sid)
