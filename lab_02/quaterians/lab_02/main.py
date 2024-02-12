from Quatarians import Quaterian
import re,os


def main():
    path = os.getcwd() + "/quanterians.txt"

    with open(path,"r") as file:
        lines = file.readlines()
        for line in lines:
            quaternion_1,quaternion_2 = line.split(',')
            real_1  = re.search(r'\d+',quaternion_1).group()
            imag_i_1 = re.search(r'(\d+)i',quaternion_1).group(1)
            imag_j_1 = re.search(r'(\d+)j',quaternion_1).group(1)
            imag_k_1 = re.search(r'(\d+)k',quaternion_1).group(1)
            real_2  = re.search(r'\d+',quaternion_2).group()
            imag_i_2 = re.search(r'(\d+)i',quaternion_2).group(1)
            imag_j_2 = re.search(r'(\d+)j',quaternion_2).group(1)
            imag_k_2 = re.search(r'(\d+)k',quaternion_2).group(1)
            q1 = [int(x) for x in [real_1,imag_i_1,imag_j_1,imag_k_1]]
            q2 = [int(x) for x in [real_2,imag_i_2,imag_j_2,imag_k_2]]
            quaternion = Quaterian()
            inverse_q1 = quaternion.quaternion_inverse(q1)
            product = quaternion.multiply(inverse_q1,q2)
            print(f"{product[0]} {product[1]}i {product[2]}j  {product[3]}k" )



            

main()