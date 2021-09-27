from logic.protogen.outgoing.grade_out_pb2 import ReadGradeListResponse, ReadGradeResponse


class Grade():
    def __init__(self, name) -> None:
        self.name = name

    @staticmethod
    def to_grpc_read_response(grade) -> ReadGradeResponse:
        return ReadGradeResponse(
            name=grade.name,
        )

    @staticmethod
    def to_grpc_read_list_response(grade_list) -> ReadGradeListResponse:
        read_grade_list_response = []
        for grade in grade_list:
            read_grade_list_response.append(Grade.to_grpc_read_response(grade))
        return read_grade_list_response
