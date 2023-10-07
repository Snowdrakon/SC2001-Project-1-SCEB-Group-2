import math
import random

WEIGHTRANGE = 100


class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        self.matrix = [[0 for i in range(nodes)] for j in range(nodes)]
        self.generate()

    def connect(self, node1, node2, weight):
        if self.matrix[node1][node2] or self.matrix[node2][node1] >= 1:
            return 0
        self.matrix[node1][node2] = weight
        self.matrix[node2][node1] = weight
        return 1

    def generate(self):
        i = 0
        while i < self.edges - 1:
            random1 = random.randint(0, self.nodes - 1)
            random2 = random.randint(0, self.nodes - 1)
            if random1 == random2:
                continue
            else:
                if self.connect(random1, random2, random.randint(0, WEIGHTRANGE)) == 0:
                    continue
                else:
                    self.connect(random1, random2, random.randint(1, WEIGHTRANGE))
                    i += 1


class PriorityQ:
    def __init__(self, size):
        self.size = size
        self.numItems = 0
        self.queue = [PQueueValue(-1, math.inf) for i in range(size)]

    def isEmpty(self):
        return self.numItems == 0

    def enqueue(self, node, distance):
        self.queue[self.numItems].node = node
        self.queue[self.numItems].distance = distance
        self.numItems += 1

    def peekIndex(self):
        smallestDistance = math.inf
        smallestIndex = -1
        for i in range(self.numItems):
            if smallestDistance >= self.queue[i].distance:
                smallestDistance = self.queue[i].distance
                smallestIndex = i

        return smallestIndex

    def remove(self, node):
        nodeIndex = -1
        for i in range(self.numItems):
            if self.queue[i].node == node:
                nodeIndex = i
                break

        if nodeIndex == -1:
            return 0

        for i in range(self.numItems - nodeIndex - 1):
            self.queue[nodeIndex + i] = self.queue[nodeIndex + i + 1]

        self.numItems -= 1

        return 1

    def dequeue(self):
        smallestIndex = self.peekIndex()
        nodeToReturn = self.queue[smallestIndex]
        for i in range(self.numItems - smallestIndex - 1):
            self.queue[smallestIndex + i] = self.queue[smallestIndex + i + 1]

        self.numItems -= 1
        return nodeToReturn

    # sort according to distance
    def sort(self, starti, endi):
        mid = math.floor((starti + endi) / 2)
        if endi - starti <= 0:
            return
        else:
            self.sort(starti, mid)
            self.sort(mid + 1, endi)
            self.merge(starti, mid, mid + 1, endi)

    def merge(self, left1, left2, right1, right2):
        tempolist = [PQueueValue(0, math.inf) for i in range(right2 - left1 + 1)]
        last = 0
        pointer1 = left1
        pointer2 = right1
        # Partial insertion sort
        while pointer1 <= left2 and pointer2 <= right2:
            if self.queue[pointer1].distance <= self.queue[pointer2].distance:
                tempolist[last].node = self.queue[pointer1].node
                tempolist[last].distance = self.queue[pointer1].distance
                pointer1 += 1
            else:
                tempolist[last].node = self.queue[pointer2].node
                tempolist[last].distance = self.queue[pointer2].distance
                pointer2 += 1

            last += 1
        # Putting in remaining objects
        if pointer1 > left2:
            while pointer2 <= right2:
                tempolist[last].node = self.queue[pointer2].node
                tempolist[last].distance = self.queue[pointer2].distance
                last += 1
                pointer2 += 1
        else:
            while pointer1 <= left2:
                tempolist[last].node = self.queue[pointer1].node
                tempolist[last].distance = self.queue[pointer1].distance
                last += 1
                pointer1 += 1
        # copying back
        for obj in tempolist:
            self.queue[left1] = obj
            left1 += 1


class PQueueValue:
    def __init__(self, node, distance):
        self.node = node
        self.distance = distance


# Implementation using adj matrix and array

def Dijkstra1(graph, source):
    dToSource = [math.inf for i in range(graph.nodes)]
    predecessors = [-1 for i in range(graph.nodes)]
    inTree = [0 for i in range(graph.nodes)]
    PQueue = PriorityQ(graph.nodes)

    dToSource[source] = 0
    predecessors[source] = source
    for i  in range(graph.nodes):
        PQueue.enqueue(i, dToSource[i])

    while not PQueue.isEmpty():
        current = PQueue.dequeue().node
        inTree[current] = 1
        for i in range(graph.nodes):
            if graph.matrix[current][i] >= 1 and inTree[i] != 1 and dToSource[i] > dToSource[current] + graph.matrix[current][i]:
                PQueue.remove(i)
                dToSource[i] = dToSource[current] + graph.matrix[current][i]
                predecessors[i] = current
                PQueue.enqueue(i, dToSource[i])

    print("Shortest cost to each node is:")
    for i in range(graph.nodes):
        print("Node: ", i, " Parent: ", predecessors[i], " Cost: ", dToSource[i])


adjGraph = Graph(5, 6)
print(adjGraph.matrix)
Dijkstra1(adjGraph, 0)


"""queue = PriorityQ(10)
queue.enqueue(2, 5)
print(queue.queue[0].distance)
queue.enqueue(1, 3)
print(queue.queue[0].distance)"""
