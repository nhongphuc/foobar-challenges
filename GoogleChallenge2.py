def solution(h, q):

    def node_coordinates(h):
        k=0
        node_coordinates_list=[]
        while k <=h-1:
            n=0
            while n <= 2**(h-k-1)-1:
                node_coordinates_list.append([(2**k)-1+n*(2**(k+1)),(2**k)-1])
                n+=1
            k+=1
        return node_coordinates_list

    
    def rotated_node_coordinates(h):
        rotated_node_coordinates_list=[]
        for i in range(len(node_coordinates(h))):
            rotated_x_coordinate = 0.70710678*(node_coordinates(h)[i][0]+node_coordinates(h)[i][1])
            rotated_y_coordinate = -0.70710678*(node_coordinates(h)[i][0]-node_coordinates(h)[i][1])
            rotated_node_coordinates_list.append([rotated_x_coordinate,rotated_y_coordinate])
        return rotated_node_coordinates_list



    def postorder_traversal(h):
        dic = {(i+1) : sorted(rotated_node_coordinates(h))[i] for i in range(len(rotated_node_coordinates(h)))}
        return dic

    def postorder_traversal_transpose(h):
        dic = {tuple(sorted(rotated_node_coordinates(h))[i]) : (i+1) for i in range(len(rotated_node_coordinates(h)))}
        return dic


    def rotated_node_coordinates_transpose(h):
        return [[rotated_node_coordinates(h)[i][1],rotated_node_coordinates(h)[i][0]] for i in range(len(rotated_node_coordinates(h)))]
    
        


    p = []
    for node_number in q:
        node_coordinate = postorder_traversal(h)[node_number]
        if node_number == (2**h)-1:
            p.append(-1)    
        elif postorder_traversal(h)[node_number + 1][0] == postorder_traversal(h)[node_number][0]:
            p.append(node_number + 1)
        else:
            transpose_node_coordinates = [node_coordinate[1],node_coordinate[0]]
            index = sorted(rotated_node_coordinates_transpose(h)).index(transpose_node_coordinates)
            root_node_coordinates_transpose = sorted(rotated_node_coordinates_transpose(h))[index+1]
            root_node_coordinates = [root_node_coordinates_transpose[1], root_node_coordinates_transpose[0]]
            root_node_number = postorder_traversal_transpose(h)[tuple(root_node_coordinates)]
            p.append(root_node_number)
    return p
    

print(solution(3,[3,4,2,1]))