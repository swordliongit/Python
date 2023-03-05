### Notes
Ordered after Python 3.7, duplicates not allowed

```python
ndict = {'key1' : 1, 'key2': 2, 'key3': [3, 4, 5]}
```
---
**To retrieve keys from a dictionary:**
```python
for key in mdict:
	...
```
**This also returns keys from a dictionary:**
```python
for x in our_dict.items():
	print(x[0]) # x[0] == 'key1'  x[1] == val1
```
**To retrieve values from a dictionary:**
```python
for val in mdict.values():
	...
```
**To retrieve both keys and values from a dictionary:**
```python
for k, v in mdict.items():
	...
```

---
**Dictionary comprehension:**
```python
numbers = [1, 2, 3]
new_dict = {item: item**2 for item in numbers}
```
**Dictionary mapping example:**
```python
# How to map a key in dicts with the same key from other dicts and create a list of them
# e.g. I want ip addresses from the hosts but I want only the devices corresponding to those ips from the modems.

# So I have to map ips from hosts with the macs from modems. That way I only have the devices and their ips from the hosts list.

        modems = [
			       {'x_mac':"1c:4a:18:23:45", 'x_ip':"192.168.5.1", 'x_var3':var3, ...},
                   {'x_mac':"1c:4a:18:30:45", 'x_ip':"192.168.5.4", 'x_var4':var4, ...},
                    ...
                 ]
        hosts =  [
				   {'x_mac':"1c:4a:18:23:45", 'x_ip':"192.168.5.2"},
                   {'x_mac':"1c:4a:18:30:45", 'x_ip':"192.168.5.3"},
                   {'x_mac':"1c:4a:18:30:4b", 'x_ip':"192.168.5.4"},
                    ...
                 ]


        # mapping values we want in dicts
        mapping_dict = {modem['x_mac']: modem['x_ip'] for modem in modems}
        # mapping = {'1c:4a:18:23:45':'192.168.5.2', '1c:4a:18:30:45':'192.168.5.3', ...}
        # now we got only the necessary key:value pairs from the dict list into a dictionary
        # now we want to put only the keys we want from the second dict list if they are in our mapping dict.        
        mapped_list = [host['x_ip'] for host in hosts if host['x_mac'] in mapping_dict]
        # mapped_list = ['192.168.5.2', '192.168.5.3', '192.168.5.4', ...]
```
---
**Dictionary Methods**
```python
dict.pop(__key)
dict.keys()
dict.values()
dict.clear()
dict.get(key)
dict.__reversed__()
dict.update(dict) # e.g. dict.update({k:v})
dict.items() -> dict_items([('key1', val1), ('key2', val2), ('key3', val3)])
```