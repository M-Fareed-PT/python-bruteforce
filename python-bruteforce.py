#!/usr/bin/env python3
"""
bruteforce.py - Lab-only brute-force simulation (does NOT attack external services).
This script demonstrates credential testing logic against a local verifier function.
Use it to learn rate-limiting detection and logging.
"""
import argparse
import time
from itertools import product

# Demo verifier (replace with lab-target function, NEVER use against unauthorized systems)
def verify_credentials(username, password):
    # Very simple "truth" for demo: username 'admin' password 'P@ssw0rd!'
    return username == "admin" and password == "P@ssw0rd!"

def main():
    p = argparse.ArgumentParser(description="Brute-force simulation (lab-only)")
    p.add_argument("--userfile", help="File with usernames (one per line)", required=True)
    p.add_argument("--passfile", help="File with passwords (one per line)", required=True)
    p.add_argument("--delay", type=float, default=0.2, help="Delay between attempts (seconds)")
    args = p.parse_args()

    users = [u.strip() for u in open(args.userfile) if u.strip()]
    passwords = [p.strip() for p in open(args.passfile) if p.strip()]

    print(f"[+] Loaded {len(users)} users and {len(passwords)} passwords (lab-only)")

    for u, pw in product(users, passwords):
        ok = verify_credentials(u, pw)
        print(f"Trying {u}:{pw} -> {'OK' if ok else 'FAIL'}")
        if ok:
            print(f"[!] Found valid credentials: {u}:{pw}")
            break
        time.sleep(args.delay)

if __name__ == "__main__":
    main()
