# G6-T24
# Kam Lee Min

# Q2

# Replace the content of this function with your own algorithm
# inputs: 
#   n: the number of members in your team
#   W: weight limit of each vehicle used for deliveries.
#   packages: 2D list [[packageID, reward, weight], [packageID, reward, weight], ...]
# returns:
#   2D list of package IDs to represent n sets of packages. 
#   e.g. if n = 2, this is a possible solution: [["P001", "P003"], ["P010"]]

import heapq

def select_packageSets(n, W, packages):

  for i in packages:
    i.append(i[1]/i[2])

  packages.sort(key=lambda x:x[3],  reverse=True)

  hp = [[0, 0 ,[]] for i in range(n)]
  heapq.heapify(hp)

  for i in range(len(packages)):
    prev_people = []
    for j in range(n):
      curr_person = heapq.heappop(hp)
      prev_people.append(curr_person)
      if curr_person[1] + packages[i][2] <= W:
        curr_person[0] += packages[i][1]
        curr_person[1] += packages[i][2]
        curr_person[2].append(packages[i][0])
        break
    for k in range(len(prev_people)):
      heapq.heappush(hp, prev_people[k])

  res = []
  while hp:
    res.append(heapq.heappop(hp)[2])

  return res


# you may insert other functions here, but all statements must be within functions
# before submitting to red, check that there are no print statements in your code. Nothing should be printed when your code runs.