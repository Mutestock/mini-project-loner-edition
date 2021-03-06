# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from logic.protogen.outgoing import teacher_out_pb2 as outgoing_dot_teacher__out__pb2


class TeacherOutStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateTeacher = channel.unary_unary(
                '/teacher_out.TeacherOut/CreateTeacher',
                request_serializer=outgoing_dot_teacher__out__pb2.CreateTeacherRequest.SerializeToString,
                response_deserializer=outgoing_dot_teacher__out__pb2.CreateTeacherResponse.FromString,
                )
        self.ReadTeacher = channel.unary_unary(
                '/teacher_out.TeacherOut/ReadTeacher',
                request_serializer=outgoing_dot_teacher__out__pb2.ReadTeacherRequest.SerializeToString,
                response_deserializer=outgoing_dot_teacher__out__pb2.ReadTeacherResponse.FromString,
                )
        self.ReadTeacherList = channel.unary_unary(
                '/teacher_out.TeacherOut/ReadTeacherList',
                request_serializer=outgoing_dot_teacher__out__pb2.ReadListTeacherRequest.SerializeToString,
                response_deserializer=outgoing_dot_teacher__out__pb2.ReadListTeacherResponse.FromString,
                )
        self.UpdateTeacher = channel.unary_unary(
                '/teacher_out.TeacherOut/UpdateTeacher',
                request_serializer=outgoing_dot_teacher__out__pb2.UpdateTeacherRequest.SerializeToString,
                response_deserializer=outgoing_dot_teacher__out__pb2.UpdateTeacherResponse.FromString,
                )
        self.DeleteTeacher = channel.unary_unary(
                '/teacher_out.TeacherOut/DeleteTeacher',
                request_serializer=outgoing_dot_teacher__out__pb2.DeleteTeacherRequest.SerializeToString,
                response_deserializer=outgoing_dot_teacher__out__pb2.DeleteTeacherResponse.FromString,
                )


class TeacherOutServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateTeacher(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadTeacher(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadTeacherList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTeacher(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTeacher(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TeacherOutServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateTeacher': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateTeacher,
                    request_deserializer=outgoing_dot_teacher__out__pb2.CreateTeacherRequest.FromString,
                    response_serializer=outgoing_dot_teacher__out__pb2.CreateTeacherResponse.SerializeToString,
            ),
            'ReadTeacher': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadTeacher,
                    request_deserializer=outgoing_dot_teacher__out__pb2.ReadTeacherRequest.FromString,
                    response_serializer=outgoing_dot_teacher__out__pb2.ReadTeacherResponse.SerializeToString,
            ),
            'ReadTeacherList': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadTeacherList,
                    request_deserializer=outgoing_dot_teacher__out__pb2.ReadListTeacherRequest.FromString,
                    response_serializer=outgoing_dot_teacher__out__pb2.ReadListTeacherResponse.SerializeToString,
            ),
            'UpdateTeacher': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateTeacher,
                    request_deserializer=outgoing_dot_teacher__out__pb2.UpdateTeacherRequest.FromString,
                    response_serializer=outgoing_dot_teacher__out__pb2.UpdateTeacherResponse.SerializeToString,
            ),
            'DeleteTeacher': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteTeacher,
                    request_deserializer=outgoing_dot_teacher__out__pb2.DeleteTeacherRequest.FromString,
                    response_serializer=outgoing_dot_teacher__out__pb2.DeleteTeacherResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'teacher_out.TeacherOut', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TeacherOut(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateTeacher(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/teacher_out.TeacherOut/CreateTeacher',
            outgoing_dot_teacher__out__pb2.CreateTeacherRequest.SerializeToString,
            outgoing_dot_teacher__out__pb2.CreateTeacherResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadTeacher(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/teacher_out.TeacherOut/ReadTeacher',
            outgoing_dot_teacher__out__pb2.ReadTeacherRequest.SerializeToString,
            outgoing_dot_teacher__out__pb2.ReadTeacherResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadTeacherList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/teacher_out.TeacherOut/ReadTeacherList',
            outgoing_dot_teacher__out__pb2.ReadListTeacherRequest.SerializeToString,
            outgoing_dot_teacher__out__pb2.ReadListTeacherResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateTeacher(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/teacher_out.TeacherOut/UpdateTeacher',
            outgoing_dot_teacher__out__pb2.UpdateTeacherRequest.SerializeToString,
            outgoing_dot_teacher__out__pb2.UpdateTeacherResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteTeacher(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/teacher_out.TeacherOut/DeleteTeacher',
            outgoing_dot_teacher__out__pb2.DeleteTeacherRequest.SerializeToString,
            outgoing_dot_teacher__out__pb2.DeleteTeacherResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
