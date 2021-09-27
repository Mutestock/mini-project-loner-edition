from logic.protogen.in import student_pb2_grpc
from utils.config import CONFIG

_CLIENT_CONFIG = CONFIG["clients"]["rest"]["mini-proj"]

def _create_stub():
    channel = grpc.insecure_channel(f"{_CLIENT_CONFIG['host']}:{_CLIENT_CONFIG['port']}")
    return student_pb2_grpc.StudentStub(channel)

def create_student(student):
    response = _create_stub().CreateStudentRequest(student)
    return response

def read_student(id):
    response = _create_stub().ReadStudentRequest(id)
    return response

def update_student(id, student):
    response = _create_stub().UpdateStudentRequest(id, student)
    return response

def delete_student(id):
    response = _create_stub().DeleteStudentRequest(id)
    return response

def read_student_list():
    response = _create_stub().ReadStudentListRequest()
    return response
