# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chat.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nchat.proto\x12\x04grpc\"\x07\n\x05\x45mpty\"b\n\x04Note\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x16\n\x0eoperation_code\x18\x02 \x01(\x05\x12\x0e\n\x06sender\x18\x03 \x01(\t\x12\x10\n\x08receiver\x18\x04 \x01(\t\x12\x0f\n\x07message\x18\x05 \x01(\t2Z\n\nChatServer\x12\'\n\nChatStream\x12\x0b.grpc.Empty\x1a\n.grpc.Note0\x01\x12#\n\x08SendNote\x12\n.grpc.Note\x1a\x0b.grpc.Emptyb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chat_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMPTY._serialized_start=20
  _EMPTY._serialized_end=27
  _NOTE._serialized_start=29
  _NOTE._serialized_end=127
  _CHATSERVER._serialized_start=129
  _CHATSERVER._serialized_end=219
# @@protoc_insertion_point(module_scope)
