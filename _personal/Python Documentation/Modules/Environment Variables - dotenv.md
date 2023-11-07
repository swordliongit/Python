```python
from dotenv import load_dotenv

load_dotenv()

def create_app():
    ...
    client = MongoClient(os.getenv("MONGODB_URI"))
	...
```

*.env*
```
MONGODB_URI=mongodb+srv://sword:xhunter50@flask-test-application.nnvocjl.mongodb.net/
```