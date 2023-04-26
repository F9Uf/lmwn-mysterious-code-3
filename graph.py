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
    while not finished:
        curr_dis, curr_pos = heapq.heappop(hq)
        y, x = curr_pos
        if x < lenx - 1:
            if dist[(y, x + 1)] > matrix[y][x + 1] + dist[(y, x)] and not visited[(y, x + 1)]:
                dist[(y, x + 1)] = matrix[y][x + 1] + dist[(y, x)]
                heapq.heappush(hq, (dist[(y, x + 1)], (y, x)))
        
        if x > 0:
            if dist[(y, x - 1)] > matrix[y][x - 1] + dist[(y, x)] and not visited[(y, x - 1)]:
                dist[(y, x - 1)] = matrix[y][x - 1] + dist[(y, x)]
                heapq.heappush(hq, (dist[(y, x - 1)], (y, x)))

        if y < leny - 1:
            if dist[(y + 1, x)] > matrix[y + 1][x] + dist[(y, x)] and not visited[(y + 1, x)]:
                dist[(y + 1, x)] = matrix[y + 1][x] + dist[(y, x)]
                heapq.heappush(hq, (dist[(y + 1, x)], (y, x)))
        
        if y > 0:
            if dist[(y - 1, x)] > matrix[y -1][x] + dist[(y, x)] and not visited[(y - 1, x)]:
                dist[(y - 1, x)] = matrix[y -1][x] + dist[(y, x)]
                heapq.heappush(hq, (dist[(y - 1, x)], (y, x)))
        
        visited[(y, x)] = True
        print(dist)
        time.sleep(1)
    return 0

started = time.time()
matrix = read_file_to_matrix("in-1.txt")
print("read matrix ==> ", time.time() - started)
print(shortest_path(matrix))
print(time.time() - started)