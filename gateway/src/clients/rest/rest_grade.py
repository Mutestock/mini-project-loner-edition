import requests
from utils.config import CONFIG

_CLIENT_CONFIG: str = CONFIG["clients"]["rest"]["mini-proj"]
_PREFIX: str = f"{_CLIENT_CONFIG['host']}:{_CLIENT_CONFIG['port']}/grade"

 
def request_create_grade(grade):
    return requests.post(_PREFIX, data=grade)

def request_read_grade(id):
    return requests.get(f"{_PREFIX}/{id}")

def request_update_grade(grade, id):
    return requests.put(f"{_PREFIX}/{id}", data=grade)

def request_delete_grade(id):
    return requests.delete(f"{_PREFIX}/{id}")
   
def request_read_list_grade():
    return requests.delete(_PREFIX)
   
