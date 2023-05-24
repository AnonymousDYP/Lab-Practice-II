# Function to find Waiting Time and Turn Around Time
def findWaitingAndTurnTime(p, n, aTime, bTime):
    wTime = [None]*n
    tTime = [None]*n
    totalTime = [None]*n
    
    wTime[0] = 0
    totalTime[0] = bTime[0] + aTime[0]
    totalWaitingTime = 0
    totalTurnAroundTime = 0

    i = 1
    while i < n:
        totalTime[i] = totalTime[i - 1] + bTime[i]
        wTime[i] = totalTime[i - 1] - aTime[i]
        totalWaitingTime = totalWaitingTime + wTime[i]
        i = i + 1

    i = 0
    while i < n:
        tTime[i] = wTime[i] + bTime[i]
        totalTurnAroundTime = totalTurnAroundTime + tTime[i]
        i = i + 1

    print("------------------------ FCFS CPU SCHEDULING ALGORITHM ------------------------")
    print("Processes\tBurst Time\tTotal Time\tWaiting Time\tTurnAround Time")

    i = 0
    while i < n:
        print(i + 1 , "\t\t   " , bTime[i] , "\t\t  " , totalTime[i] , "\t\t  " , wTime[i] , "\t\t  " , tTime[i])
        i = i + 1

    print("\t\t\t\t\t\t---------\t---------")
    print("\t\t\t\t\t\tTotal : ", totalWaitingTime,"\tTotal : ",totalTurnAroundTime)
    print("Average Waiting Time : ", (totalWaitingTime / n))
    print("Average Turn Around Time : ", (totalTurnAroundTime / n))


print("Enter the number of processes: ")
n = int(input())
p = [None]*n
bTime = [None]*n
aTime = [None]*n

i = 0
while i < len(p):
    p[i] = i
    i = i + 1

i = 0
while i < len(aTime):
    print("Enter Arrival Time for Process ", (i + 1), " : ")
    aTime[i] = int(input())
    i = i + 1

i = 0
while i < len(bTime):
    print("Enter Burst Time for Process ", (i + 1), " : ")
    bTime[i] = int(input())
    i = i + 1

findWaitingAndTurnTime(p, n, aTime, bTime)