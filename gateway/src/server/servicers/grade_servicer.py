from logic.protogen.out import grade_out_pb2_grpc
from logic.protogen.out import grade_out_pb2


class GradeServicer(grade_out_pb2_grpc.GradeOutServicer):

    def CreateGrade(self, request, context):
        return grade_out_pb2.CreateGradeResponse("Placeholder")
    
    def ReadGrade(self, request, context):
        return grade_out_pb2.ReadGradeResponse("Placeholder")
    
    def UpdateGrade(self, request, context):
        return grade_out_pb2.UpdateGradeResponse("Placeholder")
    
    def DeleteGrade(self, request, context):
        return grade_out_pb2.DeleteGradeResponse("Placeholder")
    
    def ReadGradeList(self, request, context):
        return grade_out_pb2.ReadGradeListResponse("Placeholder")
    
    
    
    

