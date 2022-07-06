#  File: Adjacency.py
#  Description: Converts an edge list into an adjacency matrix
#  Student Name: Thomas Kuo
#  Student UT EID: tck574
#  Course Name: CS 313E
#  Unique Number:

def edge_to_adjacency(edge_list):
# Add Your code here!

    vertices = []
    for i in range(len(edge_list)):
        one = edge_list[i][0]
        two = edge_list[i][1]
        if one in vertices:
            pass
        else:
            vertices.append(one)
        if two in vertices:
            pass
        else:
            vertices.append(two)
    vert_num = len(vertices)
    vertices.sort()
    init_array = []


    for y in range(vert_num):
        temp = []
        for x in range(vert_num):
            temp.append(0)
        init_array.append(temp)
    vertices.sort()

    vert_dict = {}
    key = 0
    for x in range(len(vertices)):
        vert_dict[vertices[x]] = key
        key += 1

    for j in range(len(edge_list)):
        init_array[vert_dict[edge_list[j][0]]][vert_dict[edge_list[j][1]]] = edge_list[j][2]
    return(init_array)

# ------ DO NOT CHANGE BELOW HERE ------ #
import ast

def main():
    matrix = edge_to_adjacency(ast.literal_eval(input()))

    print('\n'.join([' '.join([str(cell) for cell in row]) for row in matrix]))

if __name__ == "__main__":
    main()
