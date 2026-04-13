# SDN-Based Access Control System using POX & Mininet

## 📌 Problem Statement

The objective of this project is to implement an SDN-based access control system using Mininet and POX controller. The system enforces a whitelist policy to allow only authorized hosts to communicate, while blocking unauthorized traffic.

---

## ⚙️ Tools Used

* Mininet (Network simulation)
* POX Controller (SDN Controller)
* OpenFlow Protocol

---

## 🌐 Network Topology

* 1 Switch (s1)
* 3 Hosts (h1, h2, h3)
* Remote Controller (POX)

---

## 🔐 Access Control Logic

A whitelist is maintained:

* Allowed: h1 ↔ h2
* Blocked: h1 ↔ h3, h2 ↔ h3

Controller checks each packet and:

* Allows if in whitelist
* Blocks otherwise (installs drop rule)

---

## 🚀 Execution Steps

### 1. Run Controller

```bash
cd ~/sdn-project/pox
./pox.py forwarding.l2_learning access_control openflow.of_01 --port=6634
```

### 2. Run Mininet

```bash
sudo mn --topo single,3 --controller=remote,ip=127.0.0.1,port=6634
```

---

## 🧪 Test Scenarios

### ✅ Allowed Traffic

```bash
h1 ping h2
```

### ❌ Blocked Traffic

```bash
h1 ping h3
```

---

## 📊 Expected Output

* h1 → h2: Success
* h1 → h3: Failure
* Logs show ALLOWED / BLOCKED

---

## 📸 Proof of Execution

Screenshots included:

* Mininet ping results
* Controller logs
* Flow table entries

---

## 🎯 Conclusion

This project demonstrates centralized access control using SDN. The controller dynamically enforces policies using match-action flow rules.
