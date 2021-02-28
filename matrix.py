import numpy as np
import sympy
from typing import *

VALID_MULTIPLIER = Union[List, int, float]


class Matrix:

    def __init__(self, random=True, row=None, column=None, min_val=None,
                 max_val=None, name="", matrix=None):
        self.__matrix = []
        self.__name = name
        if random:
            properties = [row, column, min_val, max_val]
            self.__generate_matrix(*properties)
        else:
            self.__matrix = matrix

    def __repr__(self):
        title = self.__name + "\n"
        output = str(np.array(self.__matrix))
        output = " " + "".join(output[1:-1])
        output = output.replace('[', '')
        output = output.replace(']', '')
        return title + output

    def __pow__(self, other):
        if other == "t":
            output = "The transposed matrix of %s" % self.__name
            return output + str(self.transpose())
        if other == -1:
            output = "The conjugated matrix of %s" % self.__name
            return output + str(self.conjugate())
        mat = np.array(self.__matrix)
        result = np.linalg.matrix_power(mat, other)
        title = "%s" % self.__name + " raised to the power of %s" % other
        return Matrix(random=False, matrix=result, name=title)

    def __sub__(self, other):
        title, result, original_matrix, other_mat_arr = "", None, \
                                                        self.__matrix, None
        if type(other) == int:
            title = "When you subtract from Matrix %s the scalar %s you get " \
                    "the matrix:" % (self.__name, other)
            result = np.array(original_matrix) - other
        elif type(other) == list or type(other) == Matrix:
            title = "When you subtract from Matrix the provided matrix you " \
                    "get " \
                    "the matrix: "
            original_mat_arr = np.array(original_matrix)
            if type(other) == Matrix:
                other_mat_arr = np.array(other.get_raw_matrix())
            else:
                other_mat_arr = np.array(other)

            result = np.subtract(original_mat_arr, other_mat_arr)
        else:
            raise ValueError("Invalid argument for the substracter, can be " +
                             "either another matrix \ vector \ scalar")
        return Matrix(random=False, matrix=result, name=title)

    def __add__(self, other):
        title, result, original_matrix, other_mat_arr = "", None, \
                                                        self.__matrix, None
        if type(other) == int:
            title = "When you add to Matrix %s the scalar %s you get " \
                    "the matrix:" % (self.__name, other)
            result = np.array(original_matrix) + other
        elif type(other) == list or type(other) == Matrix:
            title = "When you add to a Matrix the provided matrix you get " \
                    "the matrix: "
            original_mat_arr = np.array(original_matrix)
            if type(other) == Matrix:
                other_mat_arr = np.array(other.get_raw_matrix())
            else:
                other_mat_arr = np.array(other)

            result = np.add(original_mat_arr, other_mat_arr)
        else:
            raise ValueError("Invalid argument for the addative, can be " +
                             "either another matrix \ vector \ scalar")
        return Matrix(random=False, matrix=result, name=title)

    def __truediv__(self, other):
        title, result, original_matrix, other_mat_arr = "", None, \
                                                        self.__matrix, None
        if type(other) == int:
            title = "When you multiply Matrix %s by the scalar %s you get " \
                    "the matrix:" % (self.__name, other)
            result = np.array(original_matrix) / other
        else:
            raise ValueError("Invalid argument for the multiplier, can be " +
                             "scalar only")
        return Matrix(random=False, matrix=result, name=title)

    def __floordiv__(self, other):
        title, result, original_matrix, other_mat_arr = "", None, \
                                                        self.__matrix, None
        if type(other) == int:
            title = "When you multiply Matrix %s by the scalar %s you get " \
                    "the matrix:" % (self.__name, other)
            result = np.array(original_matrix) // other
        else:
            raise ValueError("Invalid argument for the multiplier, can be " +
                             "scalar only")
        return Matrix(random=False, matrix=result, name=title)

    def __mul__(self, other):
        title, result, original_matrix, other_mat_arr = "", None, \
                                                        self.__matrix, None
        if type(other) == int:
            title = "When you multiply Matrix %s by the scalar %s you get " \
                    "the matrix:" % (self.__name, other)
            result = np.array(original_matrix) * other
        elif type(other) == list or type(other) == Matrix:
            title = "When you multiply Matrix %s by the provided matrix you " \
                    % self.__name
            title += "get the matrix: "
            original_mat_arr = np.array(original_matrix)
            if type(other) == Matrix:
                other_mat_arr = np.array(other.get_raw_matrix())
            else:
                other_mat_arr = np.array(other)

            result = np.matmul(original_mat_arr, other_mat_arr)
        else:
            raise ValueError("Invalid argument for the multiplier, can be " +
                             "either another matrix \ vector \ scalar")
        return Matrix(random=False, matrix=result, name=title)

    def __generate_matrix(self, row, column, min_val, max_val):
        for _ in range(row):
            self.__row = [np.random.randint(min_val, max_val)
                          for _ in range(column)]
            self.__matrix.append(self.__row)

    def get_raw_matrix(self):
        return self.__matrix

    def transpose(self):
        transposed = np.array(self.__matrix)
        transposed = list(np.transpose(transposed))
        return Matrix(random=False, matrix=transposed)

    def conjugate(self):
        conjugated = np.array(self.__matrix)
        conjugated = list(np.conjugate(conjugated))
        return Matrix(random=False, matrix=conjugated)

    def solve(self, dependent_variables_array):
        title = "The results of the equation set by matrix %s are: \n" % \
                self.__name
        output = np.linalg.solve(self.__matrix, dependent_variables_array)
        result = ""
        i = 0
        for item in output:
            result += "X_%s = " % i
            result += str(item)
            result += "\n"
            i += 1
        return title + result

    def rref(self):
        mat_arr = np.array(self.__matrix)
        title = "The reduced echelon form of matrix %s: \n" % self.__name
        output_matrix = str(np.array(sympy.Matrix(mat_arr).rref()[0]))[1:-1]
        more = str(np.array(sympy.Matrix(mat_arr).rref()[1]))
        pivot_columns = "The columns in which pivots appear in Matrix %s " \
                        "are: %s \n" % (self.__name, str(more)[1:-1])
        return title + " " + output_matrix + "\n" + "\n" + pivot_columns

    def determinant(self):
        mat_arr = np.array(self.__matrix)
        return str("\nDet(%s)" % self.__name) + ":" + "\n" + str(
            round(np.linalg.det(mat_arr)))
