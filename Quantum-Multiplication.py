import os,sys
from qiskit import QuantumRegister,ClassicalRegister
from qiskit import QuantumCircuit, execute, IBMQ
import qiskit_aer
import warnings



s = 11 # 100
f = 1 # 11

first = ""
second = ""

if s >= f:
    first = bin(s).replace("0b", "")
    second = bin(f).replace("0b", "")

else:
    first = bin(f).replace("0b", "")
    second = bin(s).replace("0b", "")

print()
print("first and second",first,second)
print()

list1=[]
list2=[]

for i in range(len(second)):
    if second[i] == '1':
        list1.append(i)

for i in range(len(second)):
    if second[i] == '0':
        list2.append(i)

print()
print("number of one and zero in second value: ",list1,list2)
print()
# for i in range()

list3=[]
for i in list1:
    x=s<<i
    list3.append(x)
    x=0

print()
print("List 3: ",list3)
print()


counts=0

if list3 == []:
    pass   


else:
    for i in range(len(list3)):

        if (i+1) > len(list3) or len(list3) == 1:
            break

        if i==0:
            first = bin(list3[i]).replace("0b", "")
            second = bin(list3[i+1]).replace("0b", "")
            


            l = len(first)
            l2 = len(second)

            if l > l2:
                n = l
            else:
                n = l2

            print()
            print(i,"1.First and Second number to be added",first,second)
            print()

            a = QuantumRegister(n) #First number
            b = QuantumRegister(n+1) #Second number, then sum
            c = QuantumRegister(n) #Carry bits
            cl = ClassicalRegister(n+1) #Classical output
            #Combining all of them into one quantum circuit
            qc = QuantumCircuit(a, b, c, cl)




            #Setting up the registers using the values inputted
            for i in range(l):
                if first[i] == "1":
                    qc.x(a[l - (i+1)]) #Flip the qubit from 0 to 1
            for i in range(l2):
                if second[i] == "1":
                    qc.x(b[l2 - (i+1)]) #Flip the qubit from 0 to 1







            for i in range(n-1):
                qc.ccx(a[i], b[i], c[i+1])
                qc.cx(a[i], b[i])
                qc.ccx(c[i], b[i], c[i+1])






            qc.ccx(a[n-1], b[n-1], b[n])
            qc.cx(a[n-1], b[n-1])
            qc.ccx(c[n-1], b[n-1], b[n])









            qc.cx(c[n-1], b[n-1])

            for i in range(n-1):

                qc.ccx(c[(n-2)-i], b[(n-2)-i], c[(n-1)-i])
                qc.cx(a[(n-2)-i], b[(n-2)-i])
                qc.ccx(a[(n-2)-i], b[(n-2)-i], c[(n-1)-i])
                qc.cx(c[(n-2)-i], b[(n-2)-i])
                qc.cx(a[(n-2)-i], b[(n-2)-i])

            for i in range(n+1):
                qc.measure(b[i], cl[i])



            #Set chosen backend and execute job

            backend = qiskit_aer.Aer.get_backend('qasm_simulator')
            job_simulator = execute(qc,backend,shots=1)



            result_simulator = job_simulator.result()
            counts = result_simulator.get_counts(qc)

            h = list(counts)
            second = str(int(h[0]))


        
        else:

            if (i+1) >= len(list3) or len(list3) == 1:
                break

            first = second
            second = bin(list3[i+1]).replace("0b", "")
            
            l = len(first)
            l2 = len(second)

            if l > l2:
                n = l
            else:
                n = l2

            print()
            print(i,"2.First and Second number to be added",first,second)
            print()

            a = QuantumRegister(n) #First number
            b = QuantumRegister(n+1) #Second number, then sum
            c = QuantumRegister(n) #Carry bits
            cl = ClassicalRegister(n+1) #Classical output
            #Combining all of them into one quantum circuit
            qc = QuantumCircuit(a, b, c, cl)




            #Setting up the registers using the values inputted
            for i in range(l):
                if first[i] == "1":
                    qc.x(a[l - (i+1)]) #Flip the qubit from 0 to 1
            for i in range(l2):
                if second[i] == "1":
                    qc.x(b[l2 - (i+1)]) #Flip the qubit from 0 to 1







            for i in range(n-1):
                qc.ccx(a[i], b[i], c[i+1])
                qc.cx(a[i], b[i])
                qc.ccx(c[i], b[i], c[i+1])






            qc.ccx(a[n-1], b[n-1], b[n])
            qc.cx(a[n-1], b[n-1])
            qc.ccx(c[n-1], b[n-1], b[n])









            qc.cx(c[n-1], b[n-1])

            for i in range(n-1):

                qc.ccx(c[(n-2)-i], b[(n-2)-i], c[(n-1)-i])
                qc.cx(a[(n-2)-i], b[(n-2)-i])
                qc.ccx(a[(n-2)-i], b[(n-2)-i], c[(n-1)-i])
                qc.cx(c[(n-2)-i], b[(n-2)-i])
                qc.cx(a[(n-2)-i], b[(n-2)-i])


            for i in range(n+1):
                qc.measure(b[i], cl[i])



            #Set chosen backend and execute job

            backend = qiskit_aer.Aer.get_backend('qasm_simulator')
            job_simulator = execute(qc,backend,shots=1)



            result_simulator = job_simulator.result()
            counts = result_simulator.get_counts(qc)

            h = list(counts)
            second = str(int(h[0]))

    










#Measure qubits and store results in classical register cl
# for i in range(n+1):
#     qc.measure(b[i], cl[i])



# #Set chosen backend and execute job

# backend = qiskit_aer.Aer.get_backend('qasm_simulator')
# job_simulator = execute(qc,backend,shots=2)



# result_simulator = job_simulator.result()
# counts = result_simulator.get_counts(qc)

if bin(f).replace("0b", "") == '1':
    print()
    print(bin(list3[0]).replace("0b", ""))
    k = int(bin(list3[0]).replace("0b", ""),2)
    print('Binary:',bin(list3[0]).replace("0b", ""))
    print('Number:',k)
    print()

elif list3 == []:
    print()
    print('Binary:',0)
    print('Number:',0)
    print()

else:

    if list2 == []:
        print()
        print(qc)
        print()
        print(counts)
        print()

        h = list(counts)
        g = str(int(h[0]))
        k = int(g,2)
        print('Binary:',g)
        print('Number:',k)

    else:
        print()
        print(qc)
        print()
        print(counts)
        print()
        
        
        v = bin(list3[0]).replace("0b", "")
        for i in range(len(list2)):
            v=v+'0'
        print(v)

        k = int(v,2)
        print('Binary:',v)
        print('Number:',k)