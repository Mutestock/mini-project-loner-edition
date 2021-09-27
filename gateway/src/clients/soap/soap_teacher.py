import zeep
from utils.config import CONFIG

_CLIENT_CONFIG = f"{CONFIG['client']['soap']['mini-proj']}"
_WSDL_URL = f"{_CLIENT_CONFIG['host']}:{_CLIENT_CONFIG['port']}/Service.svc?WSDL"

def _create_client():
    return zeep.Client(wsdl=_WSDL_URL)

def create_teacher(teacher):
    _create_client().service.AddTeacher()

def read_teacher(id):
    _create_client().service.GetTeacher()

def update_teacher(id, teacher):
    _create_client().service.UpdateTeacher()

def delete_teacher(id):
    _create_client().service.DeleteTeacher()

def read_list_teacher():
    _create_client().service.GetAllTeachers()



