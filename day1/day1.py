import heapq

rations_file = open('input_1.txt', 'r')
lines = rations_file.readlines()

max_rations = []
heapq.heapify(max_rations)
k = 3

current_rations = 0

for line in lines:
    content = line.strip()

    if content == "":
        if len(max_rations) < k:
            heapq.heappush(max_rations, current_rations)
        else:
            if max_rations[0] < current_rations:
                heapq.heappop(max_rations)
                heapq.heappush(max_rations, current_rations)
        current_rations = 0
    else:
        current_rations += int(content)

print("Sum of top {} rations: {}".format(k, sum(max_rations)))

