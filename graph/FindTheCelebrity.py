## def knows(a: int, b: int) -> bool
## If a knows b then true, else false

class Solution:
    # If knows is constant, linear runtime.
    def findCelebrity(self, n: int):
        # Found the candidate
        candidate = 0
        for person in range(n):
            if knows(candidate, person): candidate = person

        # Don't need to check against the whole thing again
        # Check if candidate knows anyone
        if any(knows(candidate, person) for person in range(candidate)): return -1

        # Check if everyone knows candidate
        if any(not knows(person, candidate) for person in range(n)): return -1
        return candidate
