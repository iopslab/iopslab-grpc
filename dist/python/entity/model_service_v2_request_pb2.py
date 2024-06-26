# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: entity/model_service_v2_request.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%entity/model_service_v2_request.proto\x12\x04grpc\"P\n\x1cModelServiceV2GetByIdRequest\x12\x10\n\x08node_key\x18\x01 \x01(\t\x12\x12\n\nmodel_type\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\"h\n\x1bModelServiceV2GetOneRequest\x12\x10\n\x08node_key\x18\x01 \x01(\t\x12\x12\n\nmodel_type\x18\x02 \x01(\t\x12\r\n\x05query\x18\x03 \x01(\x0c\x12\x14\n\x0c\x66ind_options\x18\x04 \x01(\x0c\"i\n\x1cModelServiceV2GetManyRequest\x12\x10\n\x08node_key\x18\x01 \x01(\t\x12\x12\n\nmodel_type\x18\x02 \x01(\t\x12\r\n\x05query\x18\x03 \x01(\x0c\x12\x14\n\x0c\x66ind_options\x18\x04 \x01(\x0c\"S\n\x1fModelServiceV2DeleteByIdRequest\x12\x10\n\x08node_key\x18\x01 \x01(\t\x12\x12\n\nmodel_type\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\"U\n\x1eModelServiceV2DeleteOneRequest\x12\x10\n\x08node_key\x18\x01 \x01(\t\x12\x12\n\nmodel_type\x18\x02 \x01(\t\x12\r\n\x05query\x18\x03 \x01(\x0c\"V\n\x1fModelServiceV2DeleteManyRequest\x12\x10\n\x08node_key\x18\x01 \x01(\t\x12\x12\n\nmodel_type\x18\x02 \x01(\t\x12\r\n\x05query\x18\x03 \x01(\x0c\"c\n\x1fModelServiceV2UpdateByIdRequest\x12\x10\n\x08node_key\x18\x01 \x01(\t\x12\x12\n\nmodel_type\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0e\n\x06update\x18\x04 \x01(\x0c\"e\n\x1eModelServiceV2UpdateOneRequest\x12\x10\n\x08node_key\x18\x01 \x01(\t\x12\x12\n\nmodel_type\x18\x02 \x01(\t\x12\r\n\x05query\x18\x03 \x01(\x0c\x12\x0e\n\x06update\x18\x04 \x01(\x0c\"f\n\x1fModelServiceV2UpdateManyRequest\x12\x10\n\x08node_key\x18\x01 \x01(\t\x12\x12\n\nmodel_type\x18\x02 \x01(\t\x12\r\n\x05query\x18\x03 \x01(\x0c\x12\x0e\n\x06update\x18\x04 \x01(\x0c\"c\n ModelServiceV2ReplaceByIdRequest\x12\x10\n\x08node_key\x18\x01 \x01(\t\x12\x12\n\nmodel_type\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\r\n\x05model\x18\x04 \x01(\x0c\"e\n\x1fModelServiceV2ReplaceOneRequest\x12\x10\n\x08node_key\x18\x01 \x01(\t\x12\x12\n\nmodel_type\x18\x02 \x01(\t\x12\r\n\x05query\x18\x03 \x01(\x0c\x12\r\n\x05model\x18\x04 \x01(\x0c\"U\n\x1eModelServiceV2InsertOneRequest\x12\x10\n\x08node_key\x18\x01 \x01(\t\x12\x12\n\nmodel_type\x18\x02 \x01(\t\x12\r\n\x05model\x18\x03 \x01(\x0c\"W\n\x1fModelServiceV2InsertManyRequest\x12\x10\n\x08node_key\x18\x01 \x01(\t\x12\x12\n\nmodel_type\x18\x02 \x01(\t\x12\x0e\n\x06models\x18\x03 \x01(\x0c\"Q\n\x1aModelServiceV2CountRequest\x12\x10\n\x08node_key\x18\x01 \x01(\t\x12\x12\n\nmodel_type\x18\x02 \x01(\t\x12\r\n\x05query\x18\x03 \x01(\x0c\x42\x08Z\x06.;grpcb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'entity.model_service_v2_request_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\006.;grpc'
  _MODELSERVICEV2GETBYIDREQUEST._serialized_start=47
  _MODELSERVICEV2GETBYIDREQUEST._serialized_end=127
  _MODELSERVICEV2GETONEREQUEST._serialized_start=129
  _MODELSERVICEV2GETONEREQUEST._serialized_end=233
  _MODELSERVICEV2GETMANYREQUEST._serialized_start=235
  _MODELSERVICEV2GETMANYREQUEST._serialized_end=340
  _MODELSERVICEV2DELETEBYIDREQUEST._serialized_start=342
  _MODELSERVICEV2DELETEBYIDREQUEST._serialized_end=425
  _MODELSERVICEV2DELETEONEREQUEST._serialized_start=427
  _MODELSERVICEV2DELETEONEREQUEST._serialized_end=512
  _MODELSERVICEV2DELETEMANYREQUEST._serialized_start=514
  _MODELSERVICEV2DELETEMANYREQUEST._serialized_end=600
  _MODELSERVICEV2UPDATEBYIDREQUEST._serialized_start=602
  _MODELSERVICEV2UPDATEBYIDREQUEST._serialized_end=701
  _MODELSERVICEV2UPDATEONEREQUEST._serialized_start=703
  _MODELSERVICEV2UPDATEONEREQUEST._serialized_end=804
  _MODELSERVICEV2UPDATEMANYREQUEST._serialized_start=806
  _MODELSERVICEV2UPDATEMANYREQUEST._serialized_end=908
  _MODELSERVICEV2REPLACEBYIDREQUEST._serialized_start=910
  _MODELSERVICEV2REPLACEBYIDREQUEST._serialized_end=1009
  _MODELSERVICEV2REPLACEONEREQUEST._serialized_start=1011
  _MODELSERVICEV2REPLACEONEREQUEST._serialized_end=1112
  _MODELSERVICEV2INSERTONEREQUEST._serialized_start=1114
  _MODELSERVICEV2INSERTONEREQUEST._serialized_end=1199
  _MODELSERVICEV2INSERTMANYREQUEST._serialized_start=1201
  _MODELSERVICEV2INSERTMANYREQUEST._serialized_end=1288
  _MODELSERVICEV2COUNTREQUEST._serialized_start=1290
  _MODELSERVICEV2COUNTREQUEST._serialized_end=1371
# @@protoc_insertion_point(module_scope)
