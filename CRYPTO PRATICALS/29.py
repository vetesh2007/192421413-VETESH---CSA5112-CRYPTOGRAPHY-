# filename: 29_sha3_capacity_lane_spread.py
"""
Simulate lane spread between rate and capacity ignoring permutation as requested.
Assumes lane size 64 and state matrix 5x5 lanes; capacity portion lanes tracked.
This script demonstrates propagation counting until all capacity lanes have at least one nonzero bit.
"""
from collections import deque

# For the simplified interpretation: mark which lanes in capacity are nonzero after absorbing P0's nonzero lanes.
# We'll simulate by saying each message lane maps to some state lane positions in capacity portion over successive absorptions.
# Because the problem asked to "Ignore the permutation", we treat positions as fixed and count how many steps until all capacity lanes touched.
def demo():
    # For SHA3-1024 rate=1024, capacity=1600? (Note: SHA3-1024 is nonstandard; this is demonstrative)
    capacity_lanes = 25 - (1024 // 64)  # simplified
    print("Capacity lanes (approx):", capacity_lanes)
    print("If every lane in P0 has at least one nonzero bit and absorption places them into rate lanes only,")
    print("then capacity lanes (initially zero) remain zero UNTIL permutation mixes them.")
    print("Since permutation is ignored, they never become nonzero. So answer: never (without permutation).")

if __name__=='__main__':
    demo()
