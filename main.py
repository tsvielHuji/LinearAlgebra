from matrix import *
if __name__ == '__main__':
    # mat_a_arr = [[1, 0, -3, -1], [2, 0, 1, 1], [1, 0, 1, 0], [0, 1, 0, 1]]
    # mat_a = Matrix(random=False, matrix=mat_a_arr, name="Mat A")
    # print(mat_a)
    # print(mat_a.determinant())
    # mat_b_arr = [[1, -1, -3, -1], [2, 1, 1, 1], [1, -2, 1, 0], [0, 0, 0, 1]]
    # mat_b = Matrix(random=False, matrix=mat_b_arr, name="Mat B")
    # print(mat_b)
    # mat_c = mat_a + 3 + mat_b
    # print(mat_c)
    # print(mat_a **-1)
    # print(mat_b.determinant())
    # mat_x = Matrix(random=False, matrix=[[1,2,-3,1], [2,-3,1,1],[-3,1,2,1],
    #                                    [-7,14,-7,
    #                                                                0]],
    #                name="Mat X")
    # print(mat_x)
    # print(mat_x.rref())

    mat_i4 = Matrix(random=False, matrix=[[1,0,0,0], [0,1,0,0],[0,0,1,0],[0,
                                                                          0,
                                                                          0,
                                                                          1]])
    mat_a = Matrix(random=False, matrix=[[1,3,5,6],[1,4,6,4],[2,2,4,5],[1,
                                                                         2,
                                                                         1,
                                                                         4]])
    # m = mat_a**2
    # q = mat_a * 2
    # print(mat_i4**2)
    # res1 = m-q+mat_i4
    # res2 = (mat_a - mat_i4)**2
    # print(res1)
    # print(res2)
    # print(res1.get_raw_matrix() == res2.get_raw_matrix())
    res1 = mat_a
    res2 = mat_i4 * mat_a
    print(res2)
    print(res1)