from logic.protogen.out import student_out_pb2


class Student():
    def __init__(self, first_name, last_name, phone_number, email) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    @staticmethod
    def to_grpc_read_response(student) -> ReadStudentResponse:
        return ReadStudentResponse(
            first_name=student.first_name,
            last_name=student.last_name,
            phone_number=student.phone_number,
            email=student.email
        )

    @staticmethod
    def to_grpc_read_list_response(student_list) -> ReadStudentListResponse:
        read_student_list_response = []
        for student in student_list:
            read_student_list_response.append(
                Student.to_grpc_read_response(student))
        return read_student_list_response
