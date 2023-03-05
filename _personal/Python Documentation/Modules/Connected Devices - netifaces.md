
**Scanning connected devices**
```python
netifaces.interfaces() # -> Obtain a list of the interfaces available on this machine. (cryptic names)
netifaces.ifaddresses(interface)[netifaces.AF_INET] # -> Obtain information about the specified network interface.
# Returns a dict whose keys are equal to the address family constants,
# e.g. netifaces.AF_INET, and whose values are a list of addresses in
# that family that are attached to the network interface. e.g:
for interface in netifaces.interfaces():
    for link in netifaces.ifaddresses(interface)[netifaces.AF_INET]:
        print(link['addr']) # prints all ipv4 addresses

# gateways
import netifaces
netifaces.gateways()["default"][netifaces.AF_INET]
```
	