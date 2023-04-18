# import numpy as np

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''#first add up all the gas and all the cost. if total gas is less than cost, then no need to check further
        gtot = sum(gas)
        ctot = sum(cost)
        if gtot < ctot:
            return -1'''

        # get the difference between gas and cost
        diff = [x - y for x, y in zip(gas, cost)]

        # if sum of the diff is negative, that means no matter what combination will be a failure, so exit
        net = sum(diff)
        if net < 0:
            return -1
        n = len(diff)  # length of the list
        start = 0  # correct starting point
        tank = 0  # how much fuel we have in the tank
        flag = 0  # to check if we have traveled one whole loop
        for i in range(2 * n):
            '''#starting point cannot be negative, so skip to next one
            if i < 0 and i == diff[start%n]:
                start += 1
                continue

            #otherwise we are checking if the start we have is a valid index'''
            flag += 1
            tank += diff[i]
            # if tank is ever less than 0 (ex: invalid starting point, cannot make to the next station) we know that
            # our current loop is not a viable starting location
            # we also know that if you start from station a and get stuck at station b, you can't get to station b from any
            # station between a and b so we can skip those
            # b also does not need to be checked as a valid start point since it must be a negative diff value to end journey
            if tank < 0:
                tank = 0
                start = i + 1
                continue

            # if flag equals n, we have traveled one whole loop and whatever our start is, it is correct
            if flag == n:
                return start

            # otherwise tank is zero or positive (valid) and one whole loop has not yet been completed
        return -1
        '''
        ####code i've tried and decided not to use#####
        ###converting to arrays and doing subtraction#####
        gas_arr = np.array(gas)
        cost_arr = np.array(cost)
        diff = [gas_arr[i] - cost_arr[i] for i in range(len(gas_arr))]

        ###first attempt at this problem, only faster than 16% of people###
        n = len(gas)    #gas.length == cost.length
        tank = 0
        i = 0
        while i < n:
            if (gas[i] == 0) and (cost[i] == 0):
                i += 1
                continue
            if gas[i] < cost[i]:
                i += 1
                continue
            tank = gas[i] - cost[i]
            flag = 0
            j = i + 1
            #for j in range(i+1,n+i+1):  #have to travel extra leg since we want to go back to original station. alr checked i
            while j < n + i + 1:
                if j >= n:
                    k = j - n
                else:
                    k = j
                tank = tank + gas[k] - cost[k]
                if tank < 0:
                    flag = 1
                    break
                j += 1
            if flag == 0:
                return i
            i = j
        return -1
        '''

