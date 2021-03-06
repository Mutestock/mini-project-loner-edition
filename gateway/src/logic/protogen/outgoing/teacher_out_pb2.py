# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: outgoing/teacher_out.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='outgoing/teacher_out.proto',
  package='teacher_out',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1aoutgoing/teacher_out.proto\x12\x0bteacher_out\"b\n\x14\x43reateTeacherRequest\x12\x12\n\nfirst_name\x18\x01 \x01(\t\x12\x11\n\tlast_name\x18\x02 \x01(\t\x12\x14\n\x0cphone_number\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\"$\n\x15\x43reateTeacherResponse\x12\x0b\n\x03msg\x18\x01 \x01(\t\" \n\x12ReadTeacherRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"a\n\x13ReadTeacherResponse\x12\x12\n\nfirst_name\x18\x01 \x01(\t\x12\x11\n\tlast_name\x18\x02 \x01(\t\x12\x14\n\x0cphone_number\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\"n\n\x14UpdateTeacherRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\x14\n\x0cphone_number\x18\x04 \x01(\t\x12\r\n\x05\x65mail\x18\x05 \x01(\t\"$\n\x15UpdateTeacherResponse\x12\x0b\n\x03msg\x18\x01 \x01(\t\"\"\n\x14\x44\x65leteTeacherRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"$\n\x15\x44\x65leteTeacherResponse\x12\x0b\n\x03msg\x18\x01 \x01(\t\"\x18\n\x16ReadListTeacherRequest\"M\n\x17ReadListTeacherResponse\x12\x32\n\x08teachers\x18\x01 \x03(\x0b\x32 .teacher_out.ReadTeacherResponse2\xce\x03\n\nTeacherOut\x12X\n\rCreateTeacher\x12!.teacher_out.CreateTeacherRequest\x1a\".teacher_out.CreateTeacherResponse\"\x00\x12R\n\x0bReadTeacher\x12\x1f.teacher_out.ReadTeacherRequest\x1a .teacher_out.ReadTeacherResponse\"\x00\x12^\n\x0fReadTeacherList\x12#.teacher_out.ReadListTeacherRequest\x1a$.teacher_out.ReadListTeacherResponse\"\x00\x12X\n\rUpdateTeacher\x12!.teacher_out.UpdateTeacherRequest\x1a\".teacher_out.UpdateTeacherResponse\"\x00\x12X\n\rDeleteTeacher\x12!.teacher_out.DeleteTeacherRequest\x1a\".teacher_out.DeleteTeacherResponse\"\x00\x62\x06proto3'
)




_CREATETEACHERREQUEST = _descriptor.Descriptor(
  name='CreateTeacherRequest',
  full_name='teacher_out.CreateTeacherRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='first_name', full_name='teacher_out.CreateTeacherRequest.first_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='teacher_out.CreateTeacherRequest.last_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phone_number', full_name='teacher_out.CreateTeacherRequest.phone_number', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='teacher_out.CreateTeacherRequest.email', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=141,
)


_CREATETEACHERRESPONSE = _descriptor.Descriptor(
  name='CreateTeacherResponse',
  full_name='teacher_out.CreateTeacherResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='teacher_out.CreateTeacherResponse.msg', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=143,
  serialized_end=179,
)


_READTEACHERREQUEST = _descriptor.Descriptor(
  name='ReadTeacherRequest',
  full_name='teacher_out.ReadTeacherRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='teacher_out.ReadTeacherRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=181,
  serialized_end=213,
)


_READTEACHERRESPONSE = _descriptor.Descriptor(
  name='ReadTeacherResponse',
  full_name='teacher_out.ReadTeacherResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='first_name', full_name='teacher_out.ReadTeacherResponse.first_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='teacher_out.ReadTeacherResponse.last_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phone_number', full_name='teacher_out.ReadTeacherResponse.phone_number', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='teacher_out.ReadTeacherResponse.email', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=215,
  serialized_end=312,
)


_UPDATETEACHERREQUEST = _descriptor.Descriptor(
  name='UpdateTeacherRequest',
  full_name='teacher_out.UpdateTeacherRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='teacher_out.UpdateTeacherRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='first_name', full_name='teacher_out.UpdateTeacherRequest.first_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='teacher_out.UpdateTeacherRequest.last_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phone_number', full_name='teacher_out.UpdateTeacherRequest.phone_number', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='teacher_out.UpdateTeacherRequest.email', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=314,
  serialized_end=424,
)


_UPDATETEACHERRESPONSE = _descriptor.Descriptor(
  name='UpdateTeacherResponse',
  full_name='teacher_out.UpdateTeacherResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='teacher_out.UpdateTeacherResponse.msg', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=426,
  serialized_end=462,
)


_DELETETEACHERREQUEST = _descriptor.Descriptor(
  name='DeleteTeacherRequest',
  full_name='teacher_out.DeleteTeacherRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='teacher_out.DeleteTeacherRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=464,
  serialized_end=498,
)


_DELETETEACHERRESPONSE = _descriptor.Descriptor(
  name='DeleteTeacherResponse',
  full_name='teacher_out.DeleteTeacherResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='teacher_out.DeleteTeacherResponse.msg', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=500,
  serialized_end=536,
)


_READLISTTEACHERREQUEST = _descriptor.Descriptor(
  name='ReadListTeacherRequest',
  full_name='teacher_out.ReadListTeacherRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=538,
  serialized_end=562,
)


_READLISTTEACHERRESPONSE = _descriptor.Descriptor(
  name='ReadListTeacherResponse',
  full_name='teacher_out.ReadListTeacherResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='teachers', full_name='teacher_out.ReadListTeacherResponse.teachers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=564,
  serialized_end=641,
)

_READLISTTEACHERRESPONSE.fields_by_name['teachers'].message_type = _READTEACHERRESPONSE
DESCRIPTOR.message_types_by_name['CreateTeacherRequest'] = _CREATETEACHERREQUEST
DESCRIPTOR.message_types_by_name['CreateTeacherResponse'] = _CREATETEACHERRESPONSE
DESCRIPTOR.message_types_by_name['ReadTeacherRequest'] = _READTEACHERREQUEST
DESCRIPTOR.message_types_by_name['ReadTeacherResponse'] = _READTEACHERRESPONSE
DESCRIPTOR.message_types_by_name['UpdateTeacherRequest'] = _UPDATETEACHERREQUEST
DESCRIPTOR.message_types_by_name['UpdateTeacherResponse'] = _UPDATETEACHERRESPONSE
DESCRIPTOR.message_types_by_name['DeleteTeacherRequest'] = _DELETETEACHERREQUEST
DESCRIPTOR.message_types_by_name['DeleteTeacherResponse'] = _DELETETEACHERRESPONSE
DESCRIPTOR.message_types_by_name['ReadListTeacherRequest'] = _READLISTTEACHERREQUEST
DESCRIPTOR.message_types_by_name['ReadListTeacherResponse'] = _READLISTTEACHERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateTeacherRequest = _reflection.GeneratedProtocolMessageType('CreateTeacherRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATETEACHERREQUEST,
  '__module__' : 'outgoing.teacher_out_pb2'
  # @@protoc_insertion_point(class_scope:teacher_out.CreateTeacherRequest)
  })
_sym_db.RegisterMessage(CreateTeacherRequest)

CreateTeacherResponse = _reflection.GeneratedProtocolMessageType('CreateTeacherResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATETEACHERRESPONSE,
  '__module__' : 'outgoing.teacher_out_pb2'
  # @@protoc_insertion_point(class_scope:teacher_out.CreateTeacherResponse)
  })
_sym_db.RegisterMessage(CreateTeacherResponse)

ReadTeacherRequest = _reflection.GeneratedProtocolMessageType('ReadTeacherRequest', (_message.Message,), {
  'DESCRIPTOR' : _READTEACHERREQUEST,
  '__module__' : 'outgoing.teacher_out_pb2'
  # @@protoc_insertion_point(class_scope:teacher_out.ReadTeacherRequest)
  })
_sym_db.RegisterMessage(ReadTeacherRequest)

ReadTeacherResponse = _reflection.GeneratedProtocolMessageType('ReadTeacherResponse', (_message.Message,), {
  'DESCRIPTOR' : _READTEACHERRESPONSE,
  '__module__' : 'outgoing.teacher_out_pb2'
  # @@protoc_insertion_point(class_scope:teacher_out.ReadTeacherResponse)
  })
_sym_db.RegisterMessage(ReadTeacherResponse)

UpdateTeacherRequest = _reflection.GeneratedProtocolMessageType('UpdateTeacherRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATETEACHERREQUEST,
  '__module__' : 'outgoing.teacher_out_pb2'
  # @@protoc_insertion_point(class_scope:teacher_out.UpdateTeacherRequest)
  })
_sym_db.RegisterMessage(UpdateTeacherRequest)

UpdateTeacherResponse = _reflection.GeneratedProtocolMessageType('UpdateTeacherResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATETEACHERRESPONSE,
  '__module__' : 'outgoing.teacher_out_pb2'
  # @@protoc_insertion_point(class_scope:teacher_out.UpdateTeacherResponse)
  })
_sym_db.RegisterMessage(UpdateTeacherResponse)

DeleteTeacherRequest = _reflection.GeneratedProtocolMessageType('DeleteTeacherRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETETEACHERREQUEST,
  '__module__' : 'outgoing.teacher_out_pb2'
  # @@protoc_insertion_point(class_scope:teacher_out.DeleteTeacherRequest)
  })
_sym_db.RegisterMessage(DeleteTeacherRequest)

DeleteTeacherResponse = _reflection.GeneratedProtocolMessageType('DeleteTeacherResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETETEACHERRESPONSE,
  '__module__' : 'outgoing.teacher_out_pb2'
  # @@protoc_insertion_point(class_scope:teacher_out.DeleteTeacherResponse)
  })
_sym_db.RegisterMessage(DeleteTeacherResponse)

ReadListTeacherRequest = _reflection.GeneratedProtocolMessageType('ReadListTeacherRequest', (_message.Message,), {
  'DESCRIPTOR' : _READLISTTEACHERREQUEST,
  '__module__' : 'outgoing.teacher_out_pb2'
  # @@protoc_insertion_point(class_scope:teacher_out.ReadListTeacherRequest)
  })
_sym_db.RegisterMessage(ReadListTeacherRequest)

ReadListTeacherResponse = _reflection.GeneratedProtocolMessageType('ReadListTeacherResponse', (_message.Message,), {
  'DESCRIPTOR' : _READLISTTEACHERRESPONSE,
  '__module__' : 'outgoing.teacher_out_pb2'
  # @@protoc_insertion_point(class_scope:teacher_out.ReadListTeacherResponse)
  })
_sym_db.RegisterMessage(ReadListTeacherResponse)



_TEACHEROUT = _descriptor.ServiceDescriptor(
  name='TeacherOut',
  full_name='teacher_out.TeacherOut',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=644,
  serialized_end=1106,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateTeacher',
    full_name='teacher_out.TeacherOut.CreateTeacher',
    index=0,
    containing_service=None,
    input_type=_CREATETEACHERREQUEST,
    output_type=_CREATETEACHERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReadTeacher',
    full_name='teacher_out.TeacherOut.ReadTeacher',
    index=1,
    containing_service=None,
    input_type=_READTEACHERREQUEST,
    output_type=_READTEACHERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReadTeacherList',
    full_name='teacher_out.TeacherOut.ReadTeacherList',
    index=2,
    containing_service=None,
    input_type=_READLISTTEACHERREQUEST,
    output_type=_READLISTTEACHERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateTeacher',
    full_name='teacher_out.TeacherOut.UpdateTeacher',
    index=3,
    containing_service=None,
    input_type=_UPDATETEACHERREQUEST,
    output_type=_UPDATETEACHERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteTeacher',
    full_name='teacher_out.TeacherOut.DeleteTeacher',
    index=4,
    containing_service=None,
    input_type=_DELETETEACHERREQUEST,
    output_type=_DELETETEACHERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TEACHEROUT)

DESCRIPTOR.services_by_name['TeacherOut'] = _TEACHEROUT

# @@protoc_insertion_point(module_scope)
