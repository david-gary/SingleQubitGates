import qiskit as q
import matplotlib as mpl
from qiskit import visualization as v

qr_X = q.QuantumRegister(1, "qr")
cr_X = q.ClassicalRegister(1, "cr")
qc_X = q.QuantumCircuit(qr_X)

print(qc_X.x(qr_X[0]))

qc_X.draw('mpl')

backend = q.Aer.get_backend('statevector_simulator')

result = q.execute(qc_X, backend).result().get_statevector(qc_X, decimals=3)

print(f"Quantum State is {result}")

newBackend = q.Aer.get_backend('qasm_simulator')
job = q.execute(qc_X, newBackend, shots = 1000)
jobResult = job.result()
counts = jobResult.get_counts(qc_X)
print(f"Total Counts: {counts}")

v.plot_histogram(counts)

qc_X2 = q.QuantumCircuit(2,2,name='qc')
#2 qubits, 2 classical bits
qc_X2.x(0)
qc_X2.barrier() #cleans up the gates
qc_X2.measure(0,0) #measured into first classical bit
qc_X2.measure(1,1) #measured into second classical bit
qc_X2.draw('mpl')

qc_X3 = q.QuantumCircuit(2, name='qc')
qc_X3.x(0)
qc_X3.measure_all()
qc_X3.draw('mpl')
