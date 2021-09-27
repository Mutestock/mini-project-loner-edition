from logic.protogen.out import teacher_out_pb2_grpc
from logic.protogen.out import teacher_out_pb2


class TeacherServicer(teacher_out_pb2_grpc.TeacherOutServicer):

    def CreateTeacher(self, request, context):
        return teacher_out_pb2.CreateTeacherResponse("Placeholder")
    
    def ReadTeacher(self, request, context):
        return teacher_out_pb2.ReadTeacherResponse("Placeholder")
    
    def UpdateTeacher(self, request, context):
        return teacher_out_pb2.UpdateTeacherResponse("Placeholder")
    
    def DeleteTeacher(self, request, context):
        return teacher_out_pb2.DeleteTeacherResponse("Placeholder")
    
    def ReadTeacherList(self, request, context):
        return teacher_out_pb2.ReadTeacherListResponse("Placeholder")
    
    
    
    

