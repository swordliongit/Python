

try:
    if True:
        raise Exception("bla")
except Exception as e:
    print(e.__class__.__name__)