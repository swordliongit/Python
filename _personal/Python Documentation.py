

"""
How to turn your .py into .exe
"""

# pip install pyinstaller
# pyinstaller main.py --onefile

# Python major.minor.patch => Python 3.11.2

"""
You are correct that if not mlist: will not always work as expected. This is because in Python, an empty list is considered a "falsy" value, but there are other "falsy" values such as None, False, and the integer 0.

Therefore, if not mlist: will evaluate to True only if mlist is an empty list. If mlist is None, False, or 0, the condition will evaluate to False.

To properly check if a list is empty, you should use if len(mlist) == 0: or if not mlist:, but be aware that the latter will not work if the variable is None, False, or 0.
"""

dir(list)
dir(str)

help(str.capitalize())

"""
Shallow and Deep Copy
"""

list1 = [1, 2, 3]

list2 = list1

list2[0] = 4 # Also changes list1 - Shallow copy

------------

list2 = list1[:]

list2[0] = 4 # Doesn't change list1

#but if;
list1 = [1, 2, 3, [4, 5]]

list2 = list1[:]

list2[3][0] = 6 # Also changes list1's sublist

------------

from copy import deepcopy

list2 = deepcopy(list1)

list2[3][0] = 6 #Doesn't change list1's sublist now


"""
######################################
Important things to know
######################################
"""
# whitespace counts as a character inside strings
# empty string = False
# for a and b    -> if a is False then b won't be evaluated
# for a or b     -> if a is True then b won't be evaluated
# in = containment test operator
# *arg -> variable argument
# objects are passed as references(e.g. -> Queue() )
# floating points are approximations so 0.1+0.2 == 0.3 will return false

# TODO: used to indicate a task that needs to be done
# FIXME: used to indicate a problem that needs to be fixed
# XXX: used to indicate a potential issue that needs attention
# HACK: used to indicate a temporary solution to a problem that needs a better solution in the future
# NOTE: used to add a note or additional information to the code
# OPTIMIZE: used to indicate a section of code that can be optimized for performance
# REVIEW: used to indicate that a section of code needs to be reviewed by a team member
# BUG: used to indicate a known bug in the code


None # null
...  # -> means we don't know what to come
pass # empty code

""""""""""""""""""""""""
""""""""""""""""""""""""
# XXX MODULES XXX
""""""""""""""""""""""""
""""""""""""""""""""""""

#module:            #main                       #alternative
def func():         from module import func     import module       #executes functions definitions and function calls
    print("")       func()                      module.func()


#module

if __name__ == "__main__":    # if module is ran, its __name__ is __main__, if the module is imported and executed from,
    print("ran from here")  # somewhere else, then __name__ is name of the module itself.

"""
Directory access
"""

#testD/test.py        #main

def func():         from testD.test import func
    print("")       func()


"""
Constants
"""

CONST = 100 #all capital letters to define a constant

dir(module_name) # -> CONST will show up here


"""
Underscore operator _
"""

    """
    Python automatically stores the value of the last expression in
    the interpreter to a particular variable called "_."
    You can also assign these value to another variable if you want.
    """
        >>> 5 + 4
        9
        >>> _     # stores the result of the above expression
        9
        >>> _ + 6
        15
    
    """
    Used in loop as anonymous filler
    """
        for _ in range(0, 5):
            ...

    """
    Ignoring values
    """
        a, _, b = (1, 2, 3) # a = 1, b = 3
    
    
    """
    Separating digits of numbers
    """
        million = 1_000_000 # prints 1000000
        binary = 0b_0010
        octa = 0o_64
        hexa = 0x_23_ab
        


""""""""""""""""""""""""
""""""""""""""""""""""""
# XXX DATA TYPES XXX
""""""""""""""""""""""""
""""""""""""""""""""""""

"""
String
"""

    """
    Multiline Strings
    """
        _str = """
        sdasds
        asdsasa
        asdasdsadsadsa
        asdsadsa
        """

    """
    Formatted Strings
    """
        varfetch = 5
        print(f"bla bla bla {varfetch}")

    """
    String Methods
    """

        str.split("@") # -> list
        str.index("kcl_")
        str.find("abc)
        str.strip("ch to strip from")
        str.title()
        str.capitalize()
        str.replace(".", "-" ,...)
        str.join(["item1", "item2"])
        str.replace("str to be replaced", "str to replace")
        str.startswith("str to find") # -> returns True/False
        str.endswith("str to find") # -> returns True/False
        str.upper()
        str.lower()
        str.isdigit() # if all chars are digit, True

"""
List
"""
nlist = [1, 2, [3, 4]]

    """
    List Comprehensions
    """
        x = [i for i in range(5) if i > 1] # assigns [2, 3, 4] to x variable

    """
    List Methods
    """

        list.sort()
        list.clear()
        list.pop()
        list.remove()
        list.__setitem(1, "house")__
        list.__getitem(1)__
        list.count(obj)  # -> returns number of occurrences of obj
        list.append(obj)


"""
Tuple
"""
# immutable list

ntuple = (1, 2, 3)

"""
Dictionary
"""

ndict = {'key1' : 1, 'key2': 2, 'key3': [3, 4, 5]}

for key in ndict: # retrieves keys from ndict
    ...

for val in ndict.items(): # retrieves values from ndict
    ...


    """
    Dictionary Comprehension
    """


        dict = {key_expr:val_expr for item in iterable}
        # XXX #

        dict = {'key1' : 1, 'key2': 2, 'key3': 3}

        key_list = ['key1', 'key2']

        filtered_dict = {key: dict[key] for key in key_list} # creates a dictionary that's filtered by the key_list's items as keys
                                                            # and values as the dictionary's values which we want to filter

        numbers = [1, 2, 3]

        new_dict = {item: item**2 for item in numbers} # creates a dictionary that has value as square of items in the numbers list and keys
                                                    # as those numbers in the list


    """
    Dictionary Mapping
    """

        # How to map a key in dicts with the same key from other dicts and create a list of them.
        # e.g. I want ip addresses from the hosts but I want only the devices corresponding to those ips from the modems.
        # So I have to map ips from hosts with the macs from modems. That way I only have the devices and their ips from the hosts list.
        modems =    [
                        {'x_mac':"1c:4a:18:23:45", 'x_ip':"192.168.5.1", 'x_var3':var3, ...}, 
                        {'x_mac':"1c:4a:18:30:45", 'x_ip':"192.168.5.4", 'x_var4':var4, ...},
                        ...
                    ]

        hosts =     [
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


    """
    Dictionary methods
    """
        dict.pop(__key)
        dict.keys()
        dict.values()
        dict.clear()
        dict.get(key)
        dict.__reversed__()
        dict.update(dict) # e.g. dict.update({k:v})

        dict.items() -> dict_items([('key1', val1), ('key2', val2), ('key3', val3)])
        for x in our_dict.items():
            print(x[0]) # x[0] == 'key1'  x[1] == val1


""""""""""""""""""""""""
""""""""""""""""""""""""
# XXX CONTROL FLOW XXX
""""""""""""""""""""""""
""""""""""""""""""""""""


"""
While
"""
while True:
    ...

"""
For
"""
for item in range(10):
    ...
    
"""
Match - Case
"""
while True:
    inp = input()

    match inp:
        case 1:
            ...
        case 2:
            ...
        case default:
            break
"""
Loop Operations - Enumerate(), Zip()
"""
for index, item in enumerate(['a', 'b', 'c']):
    #1 a  -> index = 1    item = a
    #2 b
    #3 c

for list1_items, list2_items in zip(list1, list2)
    #list1_items = list1[0]
    #list2_items = list2[0]

"""
Ternary
"""
x = 1 if ... else


"""
Exception Handling
"""
try:
    ...
except ValueError: # Catch all exceptions if empty e.g. except:
    ...
else: # if not caught anything
    ...
finally: # run this no matter what
    ...
    """
    How to get caught exception's name
    """

        try:
            raise Exception("Dummy Exception")
        except Exception as e:
            print(e.__class__.__name__) # prints the name of exception -> Exception
            print(e.args[0]) # prints the exception's message -> Dummy Exception

"""
With Context Manager
"""
# built in exception handling, no need to close files
with open(..., "w") as file:
    file.read()


""""""""""""""""""""""""
""""""""""""""""""""""""
# XXX FUNCTIONS XXX
""""""""""""""""""""""""
""""""""""""""""""""""""
"""
Parameter order
"""

1-Standard arguments
2-*args arguments
3-**kwargs arguments


"""
Function type hint
"""
def func(word: str)  -> str: # argument hint and return type hint
    return word

"""
Function return multiple
"""

def func(var1, var2)
    return var1, var2 # --> (var1, var2)


"""
Anonymous functions - Lambda
"""

# XXX lambdas can't contain statements XXX

func_name = lambda arg: arg*arg  #  func_name is now a function returning arg and can be called like func_name(3)
multiparam = lambda x, y: x*y

    """
    Lambda list comprehension
    """

        is_even_list = [lambda arg = x: arg * 10 for x in range(1, 5)]

        # iterate on each lambda function
        # and invoke the function to get the calculated value
        for item in is_even_list:
            print(item())

"""
Decorator
"""

# In short, decorators are useful when you have behavior which you want to apply to one or more functions,
# without having to modify the function directly. It allows for cleaner and more compact code.
# good for function testing

def caller(func):
    def wrapper():
        print("========")
        func()
        print("========")
    return wrapper


def printer(): # ->   same  as    @caller
    print("hello")                # def printer():


printer = caller(printer)         # printer()
printer()

    """
    How to use parameters with decorator
    """

        def caller(func):
            def wrapper(*args, **kwargs):
                print("========")
                func(*args, **kwargs)
                print("========")
            return wrapper


        @caller
        def adder(x, y):
            print(x+y)


        adder(2, 3)

"""
Generator
"""

# Used when we want to fetch elements from a large list, useful for performance,
#           * Don't use for small files/data,
#           * Called only once, will provide 0 if called again

def generator():
    for i in range(10):
        yield i ** 2    # Returns 1 item at a time when it's called, can also yield a tuple with yield item1, item2


for i in generator(): # Can be used in loops like an iterable
    print(i)


gen = (i for i in range(10)) # same thing, () creates generator expressions


"""
Closure
"""
# maintains the value of the variables between function calls. Counter of global variable usage.

def outer_function():
    
    mlist = []
    
    def inner_function(item):
        mlist.append(item)
        print(mlist)
    return inner_function

closure = outer_function()
closure(1) # mlist = [1]
closure(2) # mlist = [1, 2]

"""
Unpacking values - Variable arguments
"""

    """
    Variable arguments
    """
    
        """
        *args
        """
        
            def func(*args): # arguments are packed into a tuple
                for item in args:
                    sum += item
                print(sum)
                    
            func(1, 2) # variable number of arguments
            func(1, 2, 3)
        
        
        """
        **kwargs
        """
        
            def func(**kwargs): # arguments are packed into a dictionary
                for k, v in kwargs.items():
                    print(k, v)

            func(key1=value1, key2=value2) # variable number of keyword arguments
            func(key1=value1, key2=value2, key3=value3)
    #4EC9B0
    """
    Unpacking 
    """
        def func(a, b, c): # a=1, b=2, c=3
            print(a+b+c)
        
        mlist = [1,2,3]
        func(*mlist) # unpacked as 1 2 3
        
        # XXX XXX XXX
        
        def func(*args):
            res = 0
            for item in args:
                res+=item
            return res
        
        mlist1 = [1,2,3]
        mlist2 = [4,5,6,7]
        mlist3 = [8,9]
        
        print(func(*mlist1, *mlist2, *mlist3)) # evaluates to : func(1,2,3,4,5,6,7,8,9)
        
        # sums up all of the elements of all the lists
    
        """
        Split
        """
        
            my_list = [1, 2, 3, 4, 5, 6]

            a, *b, c = my_list # first value goes into a, last value goes into c, all inbetween goes to b

            print(a) # 1
            print(b) # [2, 3, 4, 5]
            print(c) # 6
        
        """
        Merge
        """
        
            my_first_list = [1, 2, 3]
            my_second_list = [4, 5, 6]
            my_merged_list = [*my_first_list, *my_second_list]

            print(my_merged_list) # [1, 2, 3, 4, 5, 6]
            
            # XXX XXX XXX
            
            my_first_dict = {"A": 1, "B": 2}
            my_second_dict = {"C": 3, "D": 4}
            my_merged_dict = {**my_first_dict, **my_second_dict}

            print(my_merged_dict) # {"A": 1, "B": 2, "C": 3, "D": 4}
        
        """
        Unpacking strings
        """
        
            a = [*"Python"] # a = ['P', 'y', 't', 'h', 'o', 'n']

            *a, = "Python"  # a = ['P', 'y', 't', 'h', 'o', 'n']


""""""""""""""""""""""""
""""""""""""""""""""""""
# XXX FILE CONTROL XXX
""""""""""""""""""""""""
""""""""""""""""""""""""

file.readlines() # -> list
file.read() # -> string --- Places the cursor at the end after executing
file = open("storage.txt", 'w') # -> open() has default "r" already
file = open(r"C\Users\Downloads\st.txt", "w") # -> r to bypass special characters
file = open("../files/doc.txt", "w") # -> .. goes up 1 directory
file.writelines(str(list)) # -> list
file.write("txt") # -> string

"""
How to check if a file is empty
"""

import os

if os.stat("total amount.txt").st_size == 0: # if empty


"""
Directories
"""
import os

def create_directory(filename): # create directory based on filename e.g. = "./hosts/"
    # Extract the directory name from the file path
    dirname = os.path.dirname(filename)
    
    # Create the directory if it does not exist
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    """
    Listing directory content
    """
        content = os.listdir("C:/odoo-15/odoo/") # -> list
    
    """
    Concatenating paths
    """
        from os.path import join
        full_path = join("C:/odoo-15/odoo", "bla.txt") # join(path, *paths) -> full_path == "C:/odoo-15/odoo/bla.txt"
    
    """
    Check if it's directory
    """
        from os.path import isdir
        if isdir("C:/odoo-15/odoo/"):
            ...
    

""""""""""""""""""""""""
""""""""""""""""""""""""
# XXX FUNCTIONS, MODULES, METHODS XXX
""""""""""""""""""""""""
""""""""""""""""""""""""

input() # --> str
len()
isinstance(item, type)
type(item)
round(float, digit)
Counter(iterable) # from collections import Counter
sum(iterable)
print()
exit("msg") # shows red text
help(func_name)
all(iterable) # --> True if all elements are True or the list is empty

"""
Map
"""

map(func, *iterables)  # -> map object
# calls the function on each element of the iterable

def addition(n):
    return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))


"""
Filter
"""

filter(function or None, iterable) # --> filter object
#  Return an iterator yielding those items of iterable for which function(item)
#  is true. If function is None, return the items that are true.

# a list contains both even and odd numbers.
seq = [0, 1, 2, 3, 5, 8, 13]

# result contains odd numbers of the list
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))

# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))

# Dictionary Filter

# Original dictionary
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Use filter() to filter out odd values
filtered_dict = dict(filter(lambda x: x[1] % 2 == 0, d.items()))


"""
Sorted 
"""
sorted(iterable, /, *, key=None, reverse=False) -> iterable
sorted_list_of_dicts = sorted(list_of_dicts, key=lambda x: x['x_ip']) # how to sort a list of dicts

sorted_dict = sorted(mydict) # sort by keys

sorted_dict = sorted(mydict, key=mydict.get) # sort by values


"""
Time & Date & perf_counter
"""

import time
print(time.strftime("%Y")) #year format %A : current day - Thursday, a% - Thu 

import datetime
print(datetime.datetime.now())


    """
    Checking how much time passed
    """
        from time import perf_counter
        
        start = perf_counter()
        ...
        ...
        ...
        end = perf_counter()
        
        print(end-start)


"""
Glob 
"""
import glob
filepaths = glob.glob("*.txt") # --> a list containing all file names ending with .txt

"""
Json
"""

import json                                                       #.json file, must enclose in [] or {}
with open("questions.json") as file:                                     [
                                                                             ...
    data = json.loads(file.read())      # --> list of the content        ]
    
    json.dump(data_list, file, indent=5) # --> write a list into a json file

"""
CSV
"""

import csv                                                              #.csv file
with open("weather.csv") as file:                                       "Antalya", "40"
                                                                        "Mersin", "38"
    data = list(csv.reader(file))     # --> list of lines as lists      "İstanbul", "30"   

"""
Webbrowser
"""

import webbrowser
webbrowser.open("https://www.google.com/search?q=" + "steam") #searches "steam" on google

"""
Shutil - Zip/Archive
"""
import shutil
shutil.make_archive("output", "zip", "folder") #creates zip named "output" from the folder named "folder"


"""
Math
"""
import math
rads = math.radians(degree)

"""
Random numbers
"""

import random
print(random.randint(a, b)) # --> random int

"""
Queue
"""

# XXX Thread safe, dynamic XXX

from queue import Queue

queue = Queue()

queue.put(obj)

print(queue.get())

"""
functools
"""

    """
    cache
    """
    
    @cache # speeds up time you can use lru_cache() as well
    def func():
        ...

""""""""""""""""""""""""
""""""""""""""""""""""""
# XXX Networking XXX
""""""""""""""""""""""""
""""""""""""""""""""""""

"""
Local device scan 
"""
import netifaces

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



"""
Local network scan - Scapy
"""

from scapy.all import ARP, Ether, srp
#target_ip = "192.168.5.0/24"
# IP Address for the destination
# create ARP packet
arp = ARP(pdst=target_ip)
# create the Ether broadcast packet
# ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
# stack them
packet = ether/arp
result = srp(packet, timeout=3, verbose=0)[0]
# a list of clients, we will fill this in the upcoming loop
clients = []
for sent, received in result:
    # for each response, append ip and mac address to `clients` list
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})


""""""""""""""""""""""""
""""""""""""""""""""""""
# XXX WEB SCRAPING - SELENIUM XXX
""""""""""""""""""""""""
""""""""""""""""""""""""

"""
Web driver init
"""
from selenium import webdriver

driver = webdriver.Chrome("chromedriverpath/chromedriver")

"""
Silent web browser
"""
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless") 
    
driver = webdriver.Chrome("chromedriver", options=chrome_options)

"""
Open a url
"""

driver.get(url)

"""
How to find an element
"""
from selenium.webdriver.common.by import By

driver.find_element(By.ID, "username") # -> element

"""
Defensive search for an element
"""
from selenium.webdriver.support.ui import WebDriverWait

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))

"""
How to clear and change a field element
"""
from selenium.webdriver.common.keys import Keys

element = driver.find_element(By.ID, "username") #By.ID, By.NAME, By.CSS_SELECTOR
element.clear()
element.send_keys(username)

"""
How to click on the element
"""
element.click()

"""
Defensive clicking, will throw exception if the element is not clickable after 10 seconds
"""
from selenium.webdriver.support.ui import WebDriverWait

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))).click()

"""
How to get the text field of an element
"""
field_text = driver.find_element(By.ID, "username").text

"""
How to get an attribute of an element
"""
value = element.get_attribute('value')

"""
How to know if a checkbox element is checked
"""
is_fieldselected = True if field.is_selected() else False

"""
How to accept alert pop-ups
"""
from selenium.webdriver.common.alert import Alert

WebDriverWait(driver, 10).until(lambda d: Alert(d)).accept()


""""""""""""""""""""""""
""""""""""""""""""""""""
# XXX PARALLEL COMPUTING XXX
""""""""""""""""""""""""
""""""""""""""""""""""""
"""
THREADS
"""

    import threading

    """
    Simple threading
    """

        def func():
            thread = threading.Thread(target=another_func, args=(arg1,)) # calls another function while running this function
            thread.start()

    """
    Multi threading
    """

        threads = []

        for ip in ip_list: # call multiple versions of the function simultaneously
            t = threading.Thread(target=modem_login, args=(driver, ip, output))
            threads.append(t)
            t.start()
            
        for t in threads: # wait for all threads to finish
            t.join() # parent thread is waiting

        """
        Returning values from Multithreaded functions
        """

            # XXX You can return values from threaded functions using Queue. This also works in multithreaded environment
            # Queue object can be shared between different threads.

            -- main.py --                                                       -- _module.py --

            from _module import func                                            def func(queue):
            from queue import Queue                                                 item = int(input())
                                                                                    queue.put(item)
            queue = Queue()

            thread = threading.Thread(target=func, args=(queue,))

            print(queue.get())
    
    """
    Multithreading with ThreadPoolExecutor
    """
        """
        ThreadPoolExecutor Submit
        """
            # XXX XXX
            It is to submit one function at a time.
            # XXX XXX
            
            from concurrent.futures import ThreadPoolExecutor
            
            # XXX XXX Calls func1 and func2 simultaneously
            executor = ThreadPoolExecutor(max_workers=2)
            future1 = executor.submit(func1, arg1, arg2) 
            future2 = executor.submit(func2, arg1, arg2) 
            executor.shutdown() # Release the resources held by executor

        """
        ThreadPoolExecutor Context Manager
        """
            # XXX XXX 
            Automatically handles shutdown()
            # XXX XXX
            
            def func1(arg1):
                return arg1
            
            with ThreadPoolExecutor() as executor:
                future1 = executor.submit(func1, arg1) 
                future2 = executor.submit(func2, arg1) 
                
                print(future1.result()) # result() gets the return value from the future object
                                        # that is the return value
            # XXX XXX 
            as_completed()
            An iterator over the given futures that yields each as it completes.
            # XXX XXX
            
            with ThreadPoolExecutor() as executor:
                for arg in range(50): # 50 threads
                    future = executor.submit(func, arg)
                    futures.append(future)
            
                for future in as_completed(futures):
                    print(future.result())                           
            
        
        """
        ThreadPoolExecutor multithreading with MAP
        """
            # XXX XXX 
            Mainly used for calling the same function
            Calls the function as many times as the length of the iterable by passing each item from the iterable as argument 
            # XXX XXX
            
            with ThreadPoolExecutor() as executor:
                results = executor.map(func1, [1, 2, 3]) # results is a generator that yields return values of each function call
            
            # XXX XXX
            
            with ThreadPoolExecutor() as executor:
                results = executor.map(func, [i for i in range(50)]) # 50 threads

            for res in results:
                print(res)
                

    
    """
    Thread Synchronisation with Mutex lock (Mutual exclusion object)
    """
        # XXX XXX 
        Prevents threads accessing to the same resource at the same time, eliminating race conditions
        mutex = Lock()
        mutex.acquire()
        mutex.release()
        # XXX XXX
        
        from threading import Thread, Lock
        
        class Worker:                   
            money = 100
            mutex = Lock() # mutex lock
            
            def WorkerAdder(self):
                for _ in range(10000000):
                    self.mutex.acquire() # if lock can't be acquired, sleep. If not, acquire it and lock it for other threads.
                    self.money += 10
                    self.mutex.release() # release the lock so other threads can acquire it.
                print("Stingy done")
                
            def WorkerSubtractor(self):
                for _ in range(10000000):
                    self.mutex.acquire()
                    self.money -= 10
                    self.mutex.release()
                print("Spendy done")     
            
        ss = Worker()
        Thread(target=ss.WorkerAdder, args=()).start()
        Thread(target=ss.WorkerSubtractor, args=()).start()
        time.sleep(10)
        print(ss.money)
        
    """
    Thread Synchronisation with Condition Variable
    """
        # XXX XXX 
        It is a lock but we additionally we can stop threads with wait() and then we can wake them with notify()
        depending on the condition
        cv = Condition()
        cv.acquire()
        cv.release()
        cv.notify()
        cv.wait() -> waits until notified, releases the lock
        # XXX XXX
        
        import time
        from threading import Thread, Condition
        
        class StingySpendy:
            money = 100
            cv = Condition()

            def stingy(self):
                for i in range(1000000):
                    self.cv.acquire()
                    self.money += 10
                    self.cv.notify()
                    self.cv.release()
                print("Stingy Done")

            def spendy(self):
                for i in range(500000):
                    self.cv.acquire()
                    while self.money < 20:
                        self.cv.wait()
                    self.money -= 20
                    self.cv.release()
                print("Spendy Done")
                
        ss = StingySpendy()
        Thread(target=ss.stingy, args=()).start()
        Thread(target=ss.spendy, args=()).start()
        time.sleep(5)
        print("Money in the end", ss.money)
        
    
    """
    Thread Synchronisation with join
    """
    
        def child():
            print("Child thread is doing work...")
            sleep(5)
            print("Child thread done...")

        def parent():
            t = Thread(target=child)
            t.start()
            print("Parent thread is waiting...")
            t.join()
            print("Parent thread is unblocked...")
            
        parent()
    
    """
    Better join - Wait Group
    """
        # XXX XXX 
        With join, we call join for each thread
        # XXX XXX
        
        import os
        from os.path import isdir, join
        from threading import Lock, Thread

        mutex = Lock()
        matches = []

        def file_search(root, filename):
            print("Searching in:", root)
            child_threads = []
            for file in os.listdir(root):
                full_path = join(root, file)
                if filename in file:
                    mutex.acquire()
                    matches.append(full_path)
                    mutex.release()
                if isdir(full_path):
                    t = Thread(target=file_search, args=([full_path, filename]))
                    t.start()
                    child_threads.append(t)
            for t in child_threads:
                t.join()

        def main():
            t = Thread(target=file_search, args=(["c:/tools", "README.md"]))
            t.start()
            t.join()
            for m in matches:
                print("Matched:", m)
                
        main()
        
        # XXX XXX 
        With Wait Group. Each thread signals done after they finish and main thread waits until all finished.
        cv = Condition()
        cv.notify_all()
        # XXX XXX
    
        # main file
        import os
        from os.path import isdir, join
        from threading import Lock, Thread

        from wait_group import WaitGroup

        mutex = Lock()
        matches = []


        def file_search(root, filename, wait_group):
            print("Searching in:", root)
            for file in os.listdir(root):
                full_path = join(root, file)
                if filename in file:
                    mutex.acquire()
                    matches.append(full_path)
                    mutex.release()
                if isdir(full_path):
                    wait_group.add(1)
                    t = Thread(target=file_search, args=([full_path, filename, wait_group]))
                    t.start()
            wait_group.done()

        def main():
            wait_group = WaitGroup()
            wait_group.add(1)
            t = Thread(target=file_search, args=(["c:/tools", "README.md", wait_group]))
            t.start()
            wait_group.wait()
            for m in matches:
                print("Matched:", m)

        main()
    
        # wait_group.py

        from threading import Condition

        class WaitGroup:
            wait_count = 0
            cv = Condition()
            
            def add(self, count):
                self.cv.acquire()
                self.wait_count += count
                self.cv.release()
                
            def done(self):
                self.cv.acquire()
                if self.wait_count > 0:
                    self.wait_count -= 1
                if self.wait_count == 0:
                    self.cv.notify_all()
                self.cv.release()
                
            def wait(self):
                self.cv.acquire()
                while self.wait_count > 0:
                    self.cv.wait()
                self.cv.release()
    """
    Thread Synchronisation with Barrier
    """
    # XXX XXX 
    When a thread calls barrier.wait(), it is blocked until another thread calls barrier.wait(), 
    then they both continue.
    barrier.wait()
    barrier.abort() -> Place the barrier into a 'broken' state. Useful in case of error.
    Any currently waiting threads and threads attempting to 'wait()' will have BrokenBarrierError raised.
    # XXX XXX
    
    barrier = Barrier(2) # 2 threads

    def wait_on_barrier(name, time_to_sleep):
        for i in range(10):
            print(name, "running")
            time.sleep(time_to_sleep)
            print(name, "is waiting on barrier")
            barrier.wait()
        print(name, "is finished")
        
        
    red = Thread(target=wait_on_barrier, args=("red", 4))
    blue = Thread(target=wait_on_barrier, args=("blue", 10))
    red.start()
    blue.start()
    
"""
PROCESSES
"""
# XXX XXX 
Each process executes the code outside of the target function as well so,
make sure that only the first runner executes the code. 
# XXX XXX

import multiprocessing
from multiprocessing import Process

def do_work():
    print("Starting work")
    i = 0
    for _ in range(20000000):
        i += 1
    print("Finished work")
    
if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    for _ in range(0, 5):
        p = Process(target=do_work) # call do_work 5 times simultaneously
        p.start()

    """
    Memory sharing between Processes
    """
        # XXX XXX 
        if you use standard lists, each process will copy it and we cannot change
        the contents of it in a different process. multiprocessing.Array lets us
        share it between different processes so the code below works as intended.
        # XXX XXX
    
        import multiprocessing
        from multiprocessing.context import Process

        import time


        def print_array_contents(array):
            while True:
                print(*array, sep = ", ")
                time.sleep(1)
                
        if __name__ == "__main__":
            arr = multiprocessing.Array('i', [-1]*10, lock=True)
            p = Process(target=print_array_contents, args=(arr,))
            p.start()
            for j in range(10):
                time.sleep(2)
                for i in range(10):
                    arr[i] = j
    
"""
Events
"""

# XXX XXX
We can stop a program until an event is True
# XXX XXX

main.py                                 other.py
def main(event):
    while not event.is_set():           from threading import Event
        pass                            event = Event()
# program will stop until func() is called and it sets the event                            
                                        def func():
                                            event.set()

                                        main(event)


""""""""""""""""""""""""
""""""""""""""""""""""""
# XXX GUI XXX
""""""""""""""""""""""""
""""""""""""""""""""""""
"""
PySimpleGUI
"""
import PySimpleGUI

label = PySimpleGUI.Text("Press Start")

window = PySimpleGUI.Window("Modem Config Engine", layout=[""])
window.read()
window.close()
"""
tkinter
"""
    """
    Simple GUI program
    """
        import tkinter

        root = tkinter.Tk()
        root.title("Modem Master Program")

        root.mainloop()

    """
    Label and Entry
    """
        hotel_label = ttk.Label(root, text="Otel Adi Girin ------>")
        hotel_label.grid(row=0, column=0, padx=10, pady=10)

        hotel_name_input = ttk.Entry(root)
        hotel_name_input.grid(row=0, column=1, padx=10, pady=10)
    
    """
    Buttons
    """
        button = ttk.Button(root, text="Simdi Ag Taramasi Yap", command=lambda: button_function(output, ip_input.get()))
        button.grid(row=0, column=2, columnspan=2, padx=10, pady=10)
        
        """
        Enable/Disable Button
        """
            button.config(state="disable")
    
    """
    Console
    """
        output = tkinter.Text(root)
        output.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        
        """
        Updating the console
        """
            output.update()
        
    """
    Handling X button
    """
        root.protocol("WM_DELETE_WINDOW", on_closing)
        
        def on_closing():
            """Called when you press the X button to close the program
            """
            sleep(0.5)
            root.destroy()
    
    """
    Timer
    """
        root.after(5000, lambda: button.config(state="enable")) # 5 seconds

"""
#///////////////////////////////
#///////////////////////////////
#///////////////////////////////
"""



