# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sylvain_eric_python/auth.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1esylvain_eric_python/auth.proto\x12\tmypackage\"2\n\x0cLoginRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"9\n\rLoginResponse\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0b\n\x03jwt\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\"5\n\x0fRegisterRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"/\n\x10RegisterResponse\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\r\n\x05\x65rror\x18\x02 \x01(\t2\x92\x01\n\x0b\x41uthService\x12<\n\x05Login\x12\x17.mypackage.LoginRequest\x1a\x18.mypackage.LoginResponse\"\x00\x12\x45\n\x08Register\x12\x1a.mypackage.RegisterRequest\x1a\x1b.mypackage.RegisterResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sylvain_eric_python.auth_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LOGINREQUEST._serialized_start=45
  _LOGINREQUEST._serialized_end=95
  _LOGINRESPONSE._serialized_start=97
  _LOGINRESPONSE._serialized_end=154
  _REGISTERREQUEST._serialized_start=156
  _REGISTERREQUEST._serialized_end=209
  _REGISTERRESPONSE._serialized_start=211
  _REGISTERRESPONSE._serialized_end=258
  _AUTHSERVICE._serialized_start=261
  _AUTHSERVICE._serialized_end=407
# @@protoc_insertion_point(module_scope)
