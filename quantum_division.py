import os,sys
from qiskit import QuantumRegister,ClassicalRegister
from qiskit import QuantumCircuit, execute, IBMQ
import qiskit_aer
import warnings


n1 = 22 # 101 122
n2 = 5 # 101 12

s = 0
f = 0

if n1>= n2:
    s=n1
    f=n2
else:
    s=n2
    f=n1

first_num = ""
second_num = ""


first_num = bin(s).replace("0b", "")
second_num = bin(f).replace("0b", "")


print()
print("first and second",first_num,second_num)
print()

# length_diff = len(first_num) - len(second_num)

# print()
# print('length difference:', length_diff)
# print()

# starting_point = length_diff * 2






answer = 0
previous_answer = int(second_num,2)
quotient = 0
reminder = 0

first = second_num # 11



while answer <= s:
    if n2 == 0 or n1 == 0:
        break
    quotient = quotient +1

    second = second_num # 13

    l = len(first)
    l2 = len(second)
    if l > l2:
        n = l
    else:
        n = l2


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







    #Implementing a carry gate that is applied on all (c[i], a[i], b[i]) #with output fed to c[i+1]
    for i in range(n-1):

        qc.ccx(a[i], b[i], c[i+1])
        qc.cx(a[i], b[i])
        qc.ccx(c[i], b[i], c[i+1])


    # print()
    # print('========>',n)
    # print()


    #For the last iteration of the carry gate, instead of feeding the #result to c[n], we use b[n], which is why c has only n bits, with #c[n-1] being the last carry bit
    qc.ccx(a[n-1], b[n-1], b[n])
    qc.cx(a[n-1], b[n-1])
    qc.ccx(c[n-1], b[n-1], b[n])




    #Reversing the gate operation performed on b[n-1]
    qc.cx(c[n-1], b[n-1])
    #Reversing the gate operations performed during the carry gate implementations
    #This is done to ensure the sum gates are fed with the correct input bit states
    for i in range(n-1):
        # print()
        # print('------------>',(n-2)-i,(n-1)-i)
        # print()
        qc.ccx(c[(n-2)-i], b[(n-2)-i], c[(n-1)-i])
        qc.cx(a[(n-2)-i], b[(n-2)-i])
        qc.ccx(a[(n-2)-i], b[(n-2)-i], c[(n-1)-i])

        qc.cx(c[(n-2)-i], b[(n-2)-i])
        qc.cx(a[(n-2)-i], b[(n-2)-i])






    #Measure qubits and store results in classical register cl
    for i in range(n+1):
        qc.measure(b[i], cl[i])



    #Set chosen backend and execute job

    backend = qiskit_aer.Aer.get_backend('qasm_simulator')
    job_simulator = execute(qc,backend,shots=2)



    result_simulator = job_simulator.result()
    counts = result_simulator.get_counts(qc)


    h = list(counts)
    g = str(int(h[0]))
    
    # print()
    # print('gggggggggg',g,s,first_num)
    # print()
    if int(g,2) <= int(first_num,2):
        previous_answer = int(g,2)
        first = g
    else:
        print()
        print(qc)
        print()

        print(counts)
        answer = int(g,2)
        k = previous_answer
        print('kkkkk',k)
        reminder = s-k
    
        


    # k = int(g,2)
    # print('Binary:',g)
    # print('Number:',k)

if n2 == 0 and n1 != 0:
    print("Answer will be not defined, you cannot divide it by 0.")
    print()
elif n2 == 0 or n1 == 0:
    print('quotient: ', 0)
    print('reminder: ', 0)
else:
    print('quotient: ', quotient)
    print('reminder: ', reminder)
# print('quotient: ', quotient)
