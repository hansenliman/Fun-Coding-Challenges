"""
This problem was asked by Spotify.

You are the technical director of WSPT radio, serving listeners nationwide.
For simplicity's sake we can consider each listener to live along a horizontal line
stretching from 0 (west) to 1000 (east).

Given a list of N listeners, and a list of M radio towers, each placed at various
locations along this line, determine what the minimum broadcast range would have
to be in order for each listener's home to be covered.

Example:
Input: listeners = [1,5,11,20] towers = [4,8,15]
Output: 5
Explanation:
Minimum range would be 5, since that would be required for the tower at position
15 to reach the listener at position 20.

"""

def sol(users, towers):
    if (len(users) == 0 or len(towers) == 0):
        return None
    maximum = 0
    tower_ptr = 0
    while(len(users) > 0 and tower_ptr != len(towers) - 1):
      if (abs(towers[tower_ptr] - users[0]) < abs(towers[tower_ptr + 1] - users[0])):
        if (maximum < abs(towers[tower_ptr] - users[0])):
            maximum = abs(towers[tower_ptr] - users[0])
        users.pop(0)
      else:
        tower_ptr += 1
        # switch to next user
    while(len(users) > 0): # when there is only one tower left
      if (maximum < abs(towers[tower_ptr] - users[0])):
        maximum = abs(towers[tower_ptr] - users[0])
      users.pop(0)
    return maximum
                
            


              
# Compare each of the users to the first two towers,
# and then keep going through the towers as that user while searching
# for the lowest possible connection until the length grows larger,
# in which then we will back out from the connection and compare
# the next user to that tower, while also keeping track of the maximum
# which will be the return value of the function.
# The data structure that will be used is a queue. Users and towers
# will be queues in this problem.
