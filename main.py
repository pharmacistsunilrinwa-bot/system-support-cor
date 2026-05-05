# VISNU: The Eternal Guardian
import time

def monitor_empire():
    print("[VISNU] Imperial Guard is ONLINE. Protecting all nodes...")
    while True:
        timestamp = time.strftime('%H:%M:%S')
        print(f"[{timestamp}] Visnu is watching over the Sovereign Empire.")
        time.sleep(10)

if __name__ == "__main__":
    monitor_empire()
