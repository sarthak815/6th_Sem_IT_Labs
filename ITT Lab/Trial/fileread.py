import os
# fs  = open(r'C:\Users\Sanjay\OneDrive - Manipal Academy of Higher Education\Documents\GitHub\6th_Sem_IT_Labs\ITT Lab\Trial\sample.txt', 'a')
# for i in range(5):
#     fs.write(f"{i}\n")
# for i in range(10,20):
#     fs.write(f"{i}\n")

with open(r'C:\Users\Sanjay\OneDrive - Manipal Academy of Higher Education\Documents\GitHub\6th_Sem_IT_Labs\ITT Lab\Trial\sample.txt',"r") as fo:
    for line in fo.readlines():
        print(line)
