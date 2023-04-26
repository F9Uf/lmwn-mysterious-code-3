import time
import heapq

def read_file_to_matrix(filename: str) -> list[list[int]]:
    return [
        [int(x) for x in line.strip().split(" ")]
        for line in open(filename, 'r')
    ]

def shortest_path(matrix, start=(0,0)):
    leny = len(matrix)
    lenx = len(matrix[0])

    dist = {}
    for i in range(leny):
        for j in range(lenx):
            dist[(i, j)] = float('inf')

    finished = False
    dist[(0, 0)] = 0

    # x,y = start[0], start[1]
    hq = [(0, (0, 0))]
    while len(hq) != 0:
        curr_dis, curr_pos = heapq.heappop(hq)
        y, x = curr_pos

        if x == lenx-1 and y == leny -1:
            return curr_dis + matrix[0][0]
        
        if x < lenx - 1:
            distance = curr_dis + matrix[y][x + 1]
            if distance < dist[(y, x + 1)]:
                dist[(y, x + 1)] = distance
                heapq.heappush(hq, (distance, (y, x + 1)))
        
        if x > 0:
            distance = curr_dis + matrix[y][x - 1]
            if distance < dist[(y, x - 1)]:
                dist[(y, x - 1)] = distance
                heapq.heappush(hq, (distance, (y, x - 1)))

        if y < leny - 1:
            distance = curr_dis + matrix[y + 1][x]
            if distance < dist[(y + 1, x)]:
                dist[(y + 1, x)] = distance
                heapq.heappush(hq, (distance, (y + 1, x)))

        if y > 0:
            distance = curr_dis + matrix[y - 1][x]
            if distance < dist[(y - 1, x)]:
                dist[(y - 1, x)] = distance
                heapq.heappush(hq, (distance, (y - 1, x)))
    return 0

started = time.time()
file_path = "in-4.txt"
matrix = read_file_to_matrix(file_path)
result = shortest_path(matrix)
duration = time.time() - started
print("matrix size: %d x %d" % (len(matrix), len(matrix[0])))
print("result of '%s' is %d" % (file_path, result))
print("duration: %fs" % (duration))