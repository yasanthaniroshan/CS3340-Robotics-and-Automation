import numpy as np
import math
class Quaterian:
    q1:list
    q2:list
    q3:np.ndarray

    def __init__(self) -> None:
        pass


    def multiply(self,q1,q2):
        """
        Multiplies two quaternions.

        Input
        :param q1: A 4 element array containing the first quaternion (q01, q11, q21, q31)
        :param q2: A 4 element array containing the second quaternion (q02, q12, q22, q32)

        Output
        :return: A 4 element array containing the final quaternion (q03,q13,q23,q33)

        """
    # Extract the values from q0
        w0 = q1[0]
        x0 = q1[1]
        y0 = q1[2]
        z0 = q1[3]

        # Extract the values from q1
        w1 = q2[0]
        x1 = q2[1]
        y1 = q2[2]
        z1 = q2[3]

        # Computer the product of the two quaternions, term by term
        q0q1_w = w0 * w1 - x0 * x1 - y0 * y1 - z0 * z1
        q0q1_x = w0 * x1 + x0 * w1 + y0 * z1 - z0 * y1
        q0q1_y = w0 * y1 - x0 * z1 + y0 * w1 + z0 * x1
        q0q1_z = w0 * z1 + x0 * y1 - y0 * x1 + z0 * w1

        # Create a 4 element array containing the final quaternion
        self.q3 = np.array([q0q1_w, q0q1_x, q0q1_y, q0q1_z])

        # Return a 4 element array containing the final quaternion (q02,q12,q22,q32)
        return self.q3
                
    def quaternion_inverse(self,q:list):
        inverse_quatarion = [0,0,0,0]
        magnitude =  math.pow(q[0],2) + math.pow(q[1],2) + math.pow(q[2],2) + math.pow(q[3],2)
        inverse_quatarion[0] = q[0]/magnitude
        inverse_quatarion[1] = -q[1]/magnitude
        inverse_quatarion[2] = -q[2]/magnitude
        inverse_quatarion[3] = -q[3]/magnitude
        return inverse_quatarion
