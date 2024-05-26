from datetime import datetime
from blacksheep import Application, get


app = Application()

@get("/")
def home():
    return f"Hello, World! {datetime.now().isoformat()}"
