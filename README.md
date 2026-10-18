# Python Reverse Shell — Educational Lab Project

> ⚠️ **DISCLAIMER**: This project is for **educational purposes only**. It is designed to be used in an **isolated lab environment** (e.g., VirtualBox/VMware Host-Only network) to understand how reverse shells work at a low level. Using this code against any system without explicit written permission is **illegal** and **unethical**. The author is not responsible for any misuse.

## 📌 Purpose

This project demonstrates the mechanics of a **reverse shell** using Python's built-in `socket`, `subprocess`, and `threading` modules. It is part of my ethical hacking lab practice, specifically covering the **Exploitation** and **Post-Exploitation** phases of penetration testing.

## 🧠 How It Works

1. The script connects back to a listener (Kali Linux) on a specified IP and port.
2. It spawns a shell (`cmd.exe` on Windows, `/bin/bash` on Linux).
3. Two threads handle bidirectional communication:
   - **Thread 1**: Reads shell output and sends it to the socket.
   - **Thread 2**: Receives commands from the socket and writes them to the shell's stdin.

## 🖥️ Lab Setup

| Component | Details |
| :--- | :--- |
| Attacker Machine | Kali Linux VM (IP: `192.168.56.101`) |
| Target Machine | Windows/Linux VM |
| Network | VirtualBox/VMware **Host-Only** adapter (isolated) |
| Listener | `nc -lvnp 8044` or Metasploit `multi/handler` |

### Steps to Reproduce (Lab Only)

1. Start the listener on Kali:
   nc -lvnp 8044
2. On the target VM, run the script:
   
       python3 reverse_shell.py
   
 Configuration
 
HOST = "192.168.56.101"   # Your Kali VM's IP

PORT = 8044               # Listener port
