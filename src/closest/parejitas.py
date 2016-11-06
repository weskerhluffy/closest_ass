'''
Created on 06/11/2016

@author: ernesto
https://www.hackerrank.com/challenges/closest-numbers/submissions/code/31624162
'''

import sys


def insert_sort(numeros):
        alist=list(numeros)
        for index in range(1,len(alist)):

                currentvalue = alist[index]
                position = index
                while position>0 and alist[position-1]>currentvalue:
                        alist[position]=alist[position-1]
                        position = position-1

                alist[position]=currentvalue

        return alist

def parejitas_core(numeros):
#       print("ich")
        dif_min=sys.maxsize
        parejas_min_dif=[]
#        numeros_ord=sorted(numeros)
        numeros_ord=insert_sort(numeros)

        for idx_nume, nume in enumerate(numeros_ord[:-1]):
                max_num=0
                min_num=0
                nume_sig=numeros_ord[idx_nume+1]
#               print("nume %u nume sig %u"%(nume,nume_sig))
                if(nume<nume_sig):
                        min_num=nume
                        max_num=nume_sig
                else:
                        min_num=nume_sig
                        max_num=nume
                dif_act=abs(max_num -min_num)
#               print("la dif abso %u"%dif_act)
                if(dif_act<dif_min):
#                       print("nueva dif min")
                        dif_min=dif_act
                        parejas_min_dif=[(min_num,max_num)]
                        continue
                if(dif_act==dif_min):
#                       print("appendeando a %s"%parejas_min_dif)
                        parejas_min_dif.append((min_num,max_num))

#       print("la dif minima %u, las parejas %s"%(dif_min,parejas_min_dif))
        return parejas_min_dif

def parejitas_main():
        parejas=[]
        parejas_list=[]
        lineas=list(sys.stdin)
        numeros=[int(x) for x in lineas[1].strip().split(" ")]
#       print("numeros %s"%numeros)
        parejas=parejitas_core(numeros)

        for pareja in parejas:
                parejas_list.append(pareja[0])
                parejas_list.append(pareja[1])

        print("%s"%(" ".join([str(x) for x in parejas_list])))

if __name__ == "__main__":
        parejitas_main()

