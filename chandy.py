class DistributedSystem:
    def __init__(self, num_processes):
        self.wfg = {i: [] for i in range(num_processes)}
    
    def add_dependency(self, p1, p2):
        self.wfg[p1].append(p2)
        print(f"[INFO] Process {p1} is now waiting for Process {p2}")
    
    def detect_deadlock(self, initiator):
        print(f"\n[START] Initiating deadlock detection from Process {initiator}\n")
        if self._send_probe(initiator, initiator, set()):
            print("\n[ALERT] Deadlock detected!\n")
        else:
            print("\n[SUCCESS] No deadlock detected.\n")
    
    def _send_probe(self, initiator, current, visited):
        if current in visited:
            return False
        visited.add(current)
        print(f"[TRACE] Process {current} is sending probe messages to {self.wfg[current]}")
        return any(neighbor == initiator or self._send_probe(initiator, neighbor, visited) for neighbor in self.wfg[current])

# Example Usage
dsys = DistributedSystem(4)
for a, b in [(0,1), (1,2), (2,3), (3,0)]:
    dsys.add_dependency(a, b)

dsys.detect_deadlock(0)