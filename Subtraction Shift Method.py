import os,sys
from qiskit import QuantumRegister,ClassicalRegister
from qiskit import QuantumCircuit, execute, IBMQ
import qiskit_aer
import warnings



s = 20
f = 7

if s >= f:
    first = bin(s).replace("0b", "")
    second = bin(f).replace("0b", "")

else:
    first = bin(f).replace("0b", "")
    second = bin(s).replace("0b", "")



l = len(first)
l2 = len(second)
if l > l2:
     n = l
else:
     n = l2




a = QuantumRegister(n) 
b = QuantumRegister(n)
c = QuantumRegister(n)
cl = ClassicalRegister(n) #Classical output
qc = QuantumCircuit(a, b, c, cl)



#Setting up the registers using the values inputted
for i in range(l):
    if first[i] == "1":
       qc.x(a[l - (i+1)]) #Flip the qubit from 0 to 1
for i in range(l2):
   if second[i] == "1":
      qc.x(b[l2 - (i+1)]) #Flip the qubit from 0 to 1


borrow = '0'
first = first.zfill(n)
second = second.zfill(n)

first = first[::-1]
second = second[::-1]
borrow = borrow.zfill(n)
borrow = list(borrow)

print()
print(first, second, borrow)
print()
print(qc)
print()


for i in range(n):

    if i == 0:

        qc.cnot(a[i],b[i])

        if first[i] < second[i]:
            qc.x(c[i+1])
            borrow[i+1] = '1'
    
    
    else:

        if borrow[i] != '0':
            
            if first[i] <= second[i]:
            
                qc.cnot(c[i],a[i])
                qc.cnot(a[i],b[i])
            
                if i+1 > n: # made change i+1 >= n
                    break
            
                qc.x(c[i+1])
                borrow[i+1] = '1'
            
            else:
                qc.cnot(c[i],a[i])
                qc.cnot(a[i],b[i])


        
        else:

            qc.cnot(c[i],a[i])
            qc.cnot(a[i],b[i])

            if first[i] < second[i]:
            
                if i+1 > n:
                    break
            
                qc.x(c[i+1])
                borrow[i+1] = '1'


print()
print('borrow:',borrow)
print()

#Measure qubits and store results in classical register cl
for i in range(n):
    qc.measure(b[i], cl[i])




#Set chosen backend and execute job

backend = qiskit_aer.Aer.get_backend('qasm_simulator')
job_simulator = execute(qc,backend,shots=2)



result_simulator = job_simulator.result()
counts = result_simulator.get_counts(qc)

print()
print(qc)
print()
print()
print('counts:',counts)
print()

# if int(second,2) > int(first,2):
#     a = list(counts)
if s >= f:
    h = list(counts)
    g = str(int(h[0]))
    k = int(g,2)
    print('Binary:',g)
    print('Number:',k)
else:
    h = list(counts)
    g = str(-int(h[0]))
    k = int(g,2)
    print('Binary:',g)
    print('Number:',k)

