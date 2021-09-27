from logic.protogen.out import student_out_pb2_grpc
from logic.protogen.out import student_out_pb2


class StudentServicer(student_out_pb2_grpc.StudentOutServicer):

    def CreateStudent(self, request, context):
        return student_out_pb2.CreateStudentResponse("Placeholder")
    
    def ReadStudent(self, request, context):
        return student_out_pb2.ReadStudentResponse("Placeholder")
    
    def UpdateStudent(self, request, context):
        return student_out_pb2.UpdateStudentResponse("Placeholder")
    
    def DeleteStudent(self, request, context):
        return student_out_pb2.DeleteStudentResponse("Placeholder")
    
    def ReadStudentList(self, request, context):
        return student_out_pb2.ReadStudentListResponse("Placeholder")
    
    
    
    

