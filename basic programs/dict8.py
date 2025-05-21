'''
Scenario 3: Voting System
 # You are building a voting system.
 # Each vote is recorded as a string (e.g., "Vikas", "Shivu", "Vikas")
 votes = ["Vikas", "Shivu", "Vikas", "Vikas", "Shivu", "Ravi"]
 # Tasks:
 #- Count the total votes each candidate received
 #- Find the winner
'''

votes = ["Vikas", "Shivu", "Vikas", "Vikas", "Shivu", "Ravi"]

vote_count = {}

for candidate in votes:
    vote_count[candidate] = vote_count.get(candidate , 0) + 1

winner = max(vote_count , key = vote_count.get)
print(f"The winner is : {winner} with {vote_count[winner]} votes")