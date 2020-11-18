# G6-T24
# Kam Lee Min

# Q1

# Replace the content of this function with your own algorithm
# inputs: 
#   W: weight limit of the vehicle used for deliveries.
#   packages: 2D list [[packageID, reward, weight], [packageID, reward, weight], ...]
# returns:
#   1D list of package IDs to represent a package selection. e.g. ["P001", "P003, "P010]

def select_packageSet(W, packages):
  reward_list=[]
  weight_list=[]
  id_list=[]

  for i in packages:
    id_list.append(i[0])
    reward_list.append(i[1])
    weight_list.append(i[2])
    
  n=len(packages)

  dp = [0]*(W+1)
  id_dp = [[0] for i in range(W+1)]

  for i in range(n):
    for j in range(W,weight_list[i]-1,-1):
        prev = dp[j]
        dp[j] = max(dp[j] , reward_list[i] + dp[j-weight_list[i]])
        if dp[j] > prev:
          curr = id_dp[j-weight_list[i]][:]
          curr.append(id_list[i])
          id_dp[j] = curr
          
  return id_dp[W][1:]



# you may insert other functions here, but all statements must be within functions
# before submitting to red, check that there are no print statements in your code. Nothing should be printed when your code runs.