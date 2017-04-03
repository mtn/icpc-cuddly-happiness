from importantAlgs import Dykstra, BellmanFord, Kruskall, FordFulkerson

ex1 = {1:{2:1},2:{3:1},3:{1:1}}

ex2 = { "A" : {"B":5, "C":7},
        "B" : {"C":1, "F":5},
        "C" : {"A":7, "B":7, "F":3, "D":9},
        "D" : {"E":2, "G":5},
        "E" : {"A":3},
        "F" : {"G":15},
        "G" : {"C":8, "F":2,"H":1},
        "H" : dict()
        }

def testDyk():

    print('-'*10)
    print('Dykstra: 1')
    print(Dykstra(ex1,1))

    print('-'*10)
    print('Dykstra: 2')
    print(Dykstra(ex2,'A'))

ex3 = {
    'A':{'B':1,'C':-1},
    'B':{'C':1,'A':2},
    'C':{'A':1,'B':-1},
}


def testBell():
    print('-'*10)
    print('BellmanFord: 1')
    print(BellmanFord(ex1,1))

    print('-'*10)
    print('BellmanFord: 2A')
    print(BellmanFord(ex2,'A'))

    print('-'*10)
    print('BellmanFord: 2B')
    print(BellmanFord(ex3,'B'))

    print('-'*10)
    print('BellmanFord: 2C')
    print(BellmanFord(ex3,'C'))

def testKruskal():
    print('-'*10)
    print('Kruskal:1')
    print(Kruskall(ex1))
    print('-'*10)
    print('Kruskal:2')
    print(Kruskall(ex2))
    print('-'*10)
    print('Kruskal:3')
    print(Kruskall(ex3))

testKruskal()
