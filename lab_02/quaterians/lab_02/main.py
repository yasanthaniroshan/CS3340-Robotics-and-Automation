from Quatarians import Quaterian
import re,os


def main():
    path = os.getcwd() + "/quanterians.txt"

    with open(path,"r") as file:
        lines = file.readlines()
        for line in lines:
            quaternion_1,quaternion_2 = line.split('|')
            real_1,imag_i_1,imag_j_1,imag_k_1 = quaternion_1.replace('(',"").replace(")","").replace("−",'-').split(",")
            real_2,imag_i_2,imag_j_2,imag_k_2 = quaternion_2.replace('(',"").replace(")","").replace("−",'-').split(",")
            q1 = [int(x) for x in [real_1,imag_i_1,imag_j_1,imag_k_1]]
            q2 = [int(x) for x in [real_2,imag_i_2,imag_j_2,imag_k_2]]
            quaternion = Quaterian()
            inverse_q1 = quaternion.quaternion_inverse(q1)
            product = quaternion.multiply(q2,inverse_q1)
            print(f"V_r - {product[0]} {product[1]}i {product[2]}j  {product[3]}k" )



            

main()