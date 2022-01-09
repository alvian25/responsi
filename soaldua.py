print("----------inputan---------")
pro1= int(input("program 1 : "))
pro2= int(input("program 2: "))
pro3= int(input("program 3: "))
pro4= int(input("program 4: "))
pro5= int(input("program 5: "))
pro6= int(input("program 6: "))
Quantum_time = int(input("masukan quantum time: ")) 

putaran_waktu = pro1+pro2+pro3+pro4+pro5+pro6/Quantum_time
waktu_tunggu = pro4+pro1+pro3+pro5+pro6+pro1/Quantum_time
print("========hasil=======")
print("Average turnaround time: ", putaran_waktu)
print("Average waiting time: ", waktu_tunggu)