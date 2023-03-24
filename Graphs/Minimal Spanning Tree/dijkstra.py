from heapq import heapify, heappush, heappop
from math import inf

g = {
        's': [(7, 'u'), (5, 'v'), (3, 'x')],
        'u': [(1, 'x')],
        'v': [(1, 'x'), (2, 'y')],
        'x': [(0, 't'), (3, 'y')],
        't': [(3, 'u')],
        'y': [(5, 't')]
    }

def initialize_single_source(g, s):

    d = {}
    pred = {}                               

    for v in g:                        
        d[v] = inf
        pred[v] = None
    
    d[s] = 0

    return d, pred

def relax(total, u, Q, d, p):

    for distance, v in g[u]:
        new_total = total + distance
        if new_total < d[v]:
             d[v] = new_total
             p[v] = u
             heappush(Q, (new_total, v))


def dijkstra(g, s):

    d, p = initialize_single_source(g, s)
    Q = [(0, s)]

    while Q:

        total, u = heappop(Q)      # extract_min

        relax(total, u, Q, d, p)

    return d, p

if __name__ == "__main__":

    choices = [v for v in g]
    choice = ""
    
    while choice not in choices:
        print("Pick a starting point from the following list:")
        for _choice in choices:
            print(" - " + _choice)
        choice = input("> ")

    d, pred = dijkstra(g, choice)

    print(d)
    print(pred)
