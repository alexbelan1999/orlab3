import math
def FordFalk(nodes,edges_with_weight,edges_with_weight1):
    vertex = len(nodes)
    edge = len(edges_with_weight1)
    flux = 0
    iteration = 1
    isBreak = False
    while (True):
        markedEdge =[1]
        viewedEdge =[1]
        marks = [0] * (vertex + 1)
        marks[1] =[1, 0, math.inf]
        print(iteration, " итерация")
        iteration += 1

        while (vertex not in markedEdge):
            edge_ = markedEdge[0]
            print("  ")
            print("   Просмотр ",edge_," вершины")
            newEdges = []
            weight =[0] * edge

            for i in range(0,edge):
                if (edge_ == edges_with_weight[i][0]) and (edges_with_weight[i][1] not in viewedEdge) and (edges_with_weight[i][2] > 0):
                    markedEdge.append(edges_with_weight[i][1])
                    viewedEdge.append(edges_with_weight[i][1])
                    marks[edges_with_weight[i][1]] = [edges_with_weight[i][1], edge_, min(marks[edge_][2], edges_with_weight[i][2])]
                    newEdges.append(edges_with_weight[i][1])
                    weight[edges_with_weight[i][1]] = edges_with_weight[i][2]

            for i in range(0,len(newEdges)):
                print("Добавили вершину " , newEdges[i] , ": [" , marks[newEdges[i]][1] , ", " , marks[newEdges[i]][2] , "]")

            print("Вершина " , edge_ , " просмотрена")

            markedEdge.pop(0)
            if (len(markedEdge)==0) and (vertex not in viewedEdge):
                isBreak = True
                break

        if isBreak:
            break

        print(" ")
        print("----------Step 2----------")
        arr_route = []
        arr_route.append(vertex)
        route = vertex
        flow = marks[route][2]
        flux += flow

        while route != 1:
            for i in range(0,edge):
                if (edges_with_weight[i][0] == marks[route][1]) and (edges_with_weight[i][1] == route):
                    edges_with_weight[i][2] -= flow
                    route = edges_with_weight[i][0]
                    arr_route.append(route)
                    break

        str_route = (" <--- ").join(str(x) for x in arr_route)
        print(str_route)
        print("Увеличили поток на " , flow)
        print(" ")

    print(" ")
    Y1 = [1]
    Y1_ = []
    for i in range(0,len(Y1)):
        for j in range(0,edge):
            if (Y1[i] == edges_with_weight[j][0]) and (edges_with_weight[j][2] > 0) and (edges_with_weight[j][1] not in Y1):
                Y1.append(edges_with_weight[j][1])
            elif (Y1[i] == edges_with_weight[j][1]) and (edges_with_weight[j][2] != edges_with_weight1[j][2]) and (edges_with_weight[j][0] not in Y1):
                Y1.append(edges_with_weight[j][0])

    for i in range(1,vertex+1):
        if (i not in Y1):
            Y1_.append(i)

    print("--------- Разрез ---------")
    print("I1: " , Y1)
    print("I1_: " , Y1_)
    fluxCheck = 0
    weight = 0
    print("(I1, I1_): ")

    for i in range(0,edge):
        if (edges_with_weight[i][0] in Y1) and (edges_with_weight[i][1]in Y1_) and (edges_with_weight[i][2] == 0):
            fluxCheck += edges_with_weight1[i][2]
            weight += edges_with_weight1[i][2]
            print("(" , edges_with_weight[i][0] , ", " , edges_with_weight[i][1] , ")")

    print("d = " , weight)
    pass
