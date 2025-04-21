import numpy as np, random

task_comm_cost = np.array([
    [0, 6, 4, 0, 0, 12], [6, 0, 8, 12, 3, 0], [4, 8, 0, 0, 11, 0],
    [0, 12, 0, 0, 5, 0], [0, 3, 11, 5, 0, 0], [12, 0, 0, 0, 0, 0]
])

task_exec_cost = np.array([[5, 10], [2, 0], [4, 4], [6, 3], [5, 2], [0, 4]])

def compute_cost(mapping):
    exec_cost = sum(task_exec_cost[i][mapping[i]] for i in range(6))
    comm_cost = sum(task_comm_cost[i][j] for i in range(6) for j in range(i+1, 6) if mapping[i] != mapping[j])
    return exec_cost, comm_cost, exec_cost + comm_cost

for name, mapping in zip(["Serial", "Random"], [[0, 0, 0, 1, 1, 1], random.sample([0, 0, 0, 1, 1, 1], 6)]):
    exec_cost, comm_cost, total_cost = compute_cost(mapping)
    print(f"{name} Assignment:")
    [print(f"t{i+1} -> n{node+1}") for i, node in enumerate(mapping)]
    print(f"Execution Cost: {exec_cost}\nCommunication Cost: {comm_cost}\nTotal Cost: {total_cost}\n")