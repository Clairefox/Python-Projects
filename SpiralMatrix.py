def spiralMatrixPrint(row, col, arr):
    # Defining the boundaries of the matrix.
    top = 0
    bottom = row-1
    left = 0
    right = col - 1

    # Defining the direction in which the array is to be traversed.
    dir = 0
    
    while (top <= bottom and left <=right):    
        if dir ==0:
            for i in range(left,right+1): # moving left->right
                print (arr[top][i], end=" ")

            # Since we have traversed the whole first
            # row, move down to the next row.
            top +=1
            dir = 1

        elif dir ==1:
            for i in range(top,bottom+1): # moving top->bottom
                print (arr[i][right], end=" ")

            # Since we have traversed the whole last
            # column, move down to the previous column.
            right -=1 
            dir = 2
            
        elif dir ==2:
            for i in range(right,left-1,-1): # moving right->left
                print (arr[bottom][i], end=" ")

            # Since we have traversed the whole last
            # row, move down to the previous row.
            bottom -=1
            dir = 3
            
        elif dir ==3:
            for i in range(bottom,top-1,-1): # moving bottom->top
                print (arr[i][left], end=" ")
            # Since we have traversed the whole first
            # column, move down to the next column.
            left +=1
            dir = 0

# Driver code
# Change the following array and the corresponding row and
# column arguments to test on some other input
array = [
        [11, 7,46,16, 7,16,36,40,18,14],
        [26,26,35, 7,43,45,40, 2,14,27],
        [16,23,14,11,28,10,38,22, 4,17],
        [19,46,50,17,19,17,47,10,22,32],
        [23,30,23,41, 2,10,20,18, 1, 3],
        [39,30,50,22, 2, 5,39,48,25,35],
        [13, 7,34,45,28,32,12,42,23,28],
        [37,48,49,30,12,25,38,48,20,15],
        [ 8,32,34,29, 1,40,33,10,31,28],
        [27,21,31, 8,14, 5, 5,39, 3,12],
        [20, 7,42,35,21, 9,44,11,28,44],
        [23,47,29,30,38,11,34,23,50,29],
        [46,31,21,50,25,48,35,18,35,44],
        ]

spiralMatrixPrint(13, 10, array)