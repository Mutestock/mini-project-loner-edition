from logic.protogen.out import grade_out_pb2_grpc
from logic.protogen.out import grade_out_pb2
from clients.rest import rest_grade
from entities.grade import Grade


class GradeServicer(grade_out_pb2_grpc.GradeOutServicer):

    def CreateGrade(self, request, context):
        return grade_out_pb2.CreateGradeResponse(rest_grade.create_grade(Grade.from_request(request)))

    def ReadGrade(self, request, context):
        return grade_out_pb2.ReadGradeResponse(rest_grade.read_grade(request.id))

    def UpdateGrade(self, request, context):
        return grade_out_pb2.UpdateGradeResponse(rest_grade.update_grade(request.id, Grade.from_request(request)))

    def DeleteGrade(self, request, context):
        return grade_out_pb2.DeleteGradeResponse(rest_grade.delete_grade(request.id))

    def ReadGradeList(self, request, context):
        return grade_out_pb2.ReadGradeListResponse(rest_grade.read_list_grade())
