# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Authentication.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x41uthentication.proto\x12\x0e\x41uthentication\"D\n\x0fRegisterRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\"#\n\x10RegisterResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"/\n\x0cLoginRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\x1e\n\rLoginResponse\x12\r\n\x05token\x18\x01 \x01(\t\"2\n\x1f\x41\x63\x63\x65ssProtectedResourceResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x07\n\x05\x45mpty2\xc0\x02\n\x0b\x41uthService\x12M\n\x08Register\x12\x1f.Authentication.RegisterRequest\x1a .Authentication.RegisterResponse\x12\x44\n\x05Login\x12\x1c.Authentication.LoginRequest\x1a\x1d.Authentication.LoginResponse\x12\x61\n\x17\x41\x63\x63\x65ssProtectedResource\x12\x15.Authentication.Empty\x1a/.Authentication.AccessProtectedResourceResponse\x12\x39\n\tCleanupDb\x12\x15.Authentication.Empty\x1a\x15.Authentication.Emptyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Authentication_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_REGISTERREQUEST']._serialized_start=40
  _globals['_REGISTERREQUEST']._serialized_end=108
  _globals['_REGISTERRESPONSE']._serialized_start=110
  _globals['_REGISTERRESPONSE']._serialized_end=145
  _globals['_LOGINREQUEST']._serialized_start=147
  _globals['_LOGINREQUEST']._serialized_end=194
  _globals['_LOGINRESPONSE']._serialized_start=196
  _globals['_LOGINRESPONSE']._serialized_end=226
  _globals['_ACCESSPROTECTEDRESOURCERESPONSE']._serialized_start=228
  _globals['_ACCESSPROTECTEDRESOURCERESPONSE']._serialized_end=278
  _globals['_EMPTY']._serialized_start=280
  _globals['_EMPTY']._serialized_end=287
  _globals['_AUTHSERVICE']._serialized_start=290
  _globals['_AUTHSERVICE']._serialized_end=610
# @@protoc_insertion_point(module_scope)
