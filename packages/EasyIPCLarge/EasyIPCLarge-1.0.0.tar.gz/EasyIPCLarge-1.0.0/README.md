### Server example.


Start the server:
```python
from EasyIPCLarge.MemoryServer import MemoryServer

srv = MemoryServer(port=1234)
while True:
    seq, delayUS, b = srv.GetData()
    if b is not None:
        print("Received: {:5d}, delay({}us), bytes({})".format(seq, delayUS,
              len(b)))
```

Stop the server:
```python
srv.Stop()
```


### Client example.


Client send data:
```python
from EasyIPCLarge.MemoryClient import MemoryClient
import time

b = bytes(4*1024*1024)

cli = MemoryClient(port=1234)
cli.SharedMemoryOpen(64*1024*1024)

for seq in range(16):
    while True:
        r = cli.SharedMemorySend(seq, b)
            if r:
                print("Client: sent {}".format(seq))
                break
            else:
                print("Client: fail {}".format(seq))

while not cli.SharedMemoryEmpty():
    time.sleep(0.01)

cli.SharedMemoryClose()
del cli
```
