# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: entity/response.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from entity import response_code_pb2 as entity_dot_response__code__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x65ntity/response.proto\x12\x04grpc\x1a\x1a\x65ntity/response_code.proto\"d\n\x08Response\x12\x1b\n\x04\x63ode\x18\x01 \x01(\x0e\x32\r.ResponseCode\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x12\r\n\x05\x65rror\x18\x04 \x01(\t\x12\r\n\x05total\x18\x05 \x01(\x03\x42\x08Z\x06.;grpcb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'entity.response_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\006.;grpc'
  _RESPONSE._serialized_start=59
  _RESPONSE._serialized_end=159
# @@protoc_insertion_point(module_scope)