import os,sys
from qiskit import QuantumRegister,ClassicalRegister
from qiskit import QuantumCircuit, execute, IBMQ
import qiskit_aer
import warnings

# qreg = QuantumRegister(1)
# creg = ClassicalRegister(1)
# circ = QuantumCircuit(qreg, creg)

# circ.x(qreg[0])
# circ.measure(qreg[0], creg[0])


# result = execute(circ, backend='ibmq_qasm_simulator', shots=2).result()
# print(result.get_counts())


# first = input("Enter a binary number with less than 8 digits")
# second = input("Enter another binary number with less than 8 digits")

# first = '10101'
# second = '11010'

first = '0000001' # 11
second = '1101' # 13

l = len(first)
l2 = len(second)
if l > l2:
     n = l
else:
     n = l2
#Initializing the registers; two quantum registers with n bits each
#1 more with n+1 bits, which will also hold the sum of the two #numbers
#The classical register has n+1 bits, which is used to make the sum #readable
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


# for i in range(l):
#     print()
#     print(l-(i+1),i,first[i])
#     print()
#     if first[i] == "1":
#        qc.x(a[i]) #Flip the qubit from 0 to 1
# for i in range(l2):
#    if second[i] == "1":
#       qc.x(b[i]) #Flip the qubit from 0 to 1





#Implementing a carry gate that is applied on all (c[i], a[i], b[i]) #with output fed to c[i+1]
for i in range(n-1):
    # print()
    # print(c[i+1],i)
    # print()
    qc.ccx(a[i], b[i], c[i+1])
    qc.cx(a[i], b[i])
    qc.ccx(c[i], b[i], c[i+1])


print()
print('========>',n)
print()


#For the last iteration of the carry gate, instead of feeding the #result to c[n], we use b[n], which is why c has only n bits, with #c[n-1] being the last carry bit
qc.ccx(a[n-1], b[n-1], b[n])
qc.cx(a[n-1], b[n-1])
qc.ccx(c[n-1], b[n-1], b[n])








#Reversing the gate operation performed on b[n-1]
qc.cx(c[n-1], b[n-1])
#Reversing the gate operations performed during the carry gate implementations
#This is done to ensure the sum gates are fed with the correct input bit states
for i in range(n-1):
    print()
    print('------------>',(n-2)-i,(n-1)-i)
    print()
    qc.ccx(c[(n-2)-i], b[(n-2)-i], c[(n-1)-i])
    qc.cx(a[(n-2)-i], b[(n-2)-i])
    qc.ccx(a[(n-2)-i], b[(n-2)-i], c[(n-1)-i])
    #These two operations act as a sum gate; if a control bit is at                
    #the 1> state then the target bit b[(n-2)-i] is flipped
    qc.cx(c[(n-2)-i], b[(n-2)-i])
    qc.cx(a[(n-2)-i], b[(n-2)-i])




# print()
# print(qc)
# print()









#Measure qubits and store results in classical register cl
for i in range(n+1):
    qc.measure(b[i], cl[i])






# print()
# print(qc)
# print()



#Set chosen backend and execute job

backend = qiskit_aer.Aer.get_backend('qasm_simulator')
job_simulator = execute(qc,backend,shots=2)

# num_shots = 2 #Setting the number of times to repeat measurement
# selected_backend = "local_qasm_simulator"
# job = execute(qc, selected_backend, shots=num_shots)


#Get results of program
# job_stats = job.result().get_counts()

result_simulator = job_simulator.result()
counts = result_simulator.get_counts(qc)

print()
print(qc)
print()

print(counts)