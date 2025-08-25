from pypresence import Presence
import time

RPC = Presence("clienid")
RPC.connect()
RPC.update(details="nah bro", state="in nigga", large_image="largeimagekei", large_text="nobro", small_image="smallimagekei", small_text="popadise")

print("rpc running")
try:
    while True:
        time.sleep(15)  
except KeyboardInterrupt:
    RPC.close()
    print("rpc bomobmo")
