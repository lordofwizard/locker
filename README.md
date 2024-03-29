Locker example

```py
lck = Locker()

lck.lock()

while True:
    #do something idk
    if lck.is_locked():
      # don't to anything
        lck.release()
        pass
    else:
        run()
```
