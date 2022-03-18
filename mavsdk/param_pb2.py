# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: param/param.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11param/param.proto\x12\x10mavsdk.rpc.param\x1a\x14mavsdk_options.proto\"\"\n\x12GetParamIntRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"Y\n\x13GetParamIntResponse\x12\x33\n\x0cparam_result\x18\x01 \x01(\x0b\x32\x1d.mavsdk.rpc.param.ParamResult\x12\r\n\x05value\x18\x02 \x01(\x05\"1\n\x12SetParamIntRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05\"J\n\x13SetParamIntResponse\x12\x33\n\x0cparam_result\x18\x01 \x01(\x0b\x32\x1d.mavsdk.rpc.param.ParamResult\"$\n\x14GetParamFloatRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"[\n\x15GetParamFloatResponse\x12\x33\n\x0cparam_result\x18\x01 \x01(\x0b\x32\x1d.mavsdk.rpc.param.ParamResult\x12\r\n\x05value\x18\x02 \x01(\x02\"3\n\x14SetParamFloatRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02\"L\n\x15SetParamFloatResponse\x12\x33\n\x0cparam_result\x18\x01 \x01(\x0b\x32\x1d.mavsdk.rpc.param.ParamResult\"\x15\n\x13GetAllParamsRequest\"C\n\x14GetAllParamsResponse\x12+\n\x06params\x18\x01 \x01(\x0b\x32\x1b.mavsdk.rpc.param.AllParams\"\'\n\x08IntParam\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05\")\n\nFloatParam\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02\"o\n\tAllParams\x12.\n\nint_params\x18\x01 \x03(\x0b\x32\x1a.mavsdk.rpc.param.IntParam\x12\x32\n\x0c\x66loat_params\x18\x02 \x03(\x0b\x32\x1c.mavsdk.rpc.param.FloatParam\"\x88\x02\n\x0bParamResult\x12\x34\n\x06result\x18\x01 \x01(\x0e\x32$.mavsdk.rpc.param.ParamResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"\xae\x01\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x12\n\x0eRESULT_TIMEOUT\x10\x02\x12\x1b\n\x17RESULT_CONNECTION_ERROR\x10\x03\x12\x15\n\x11RESULT_WRONG_TYPE\x10\x04\x12\x1e\n\x1aRESULT_PARAM_NAME_TOO_LONG\x10\x05\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x06\x32\x87\x04\n\x0cParamService\x12`\n\x0bGetParamInt\x12$.mavsdk.rpc.param.GetParamIntRequest\x1a%.mavsdk.rpc.param.GetParamIntResponse\"\x04\x80\xb5\x18\x01\x12`\n\x0bSetParamInt\x12$.mavsdk.rpc.param.SetParamIntRequest\x1a%.mavsdk.rpc.param.SetParamIntResponse\"\x04\x80\xb5\x18\x01\x12\x66\n\rGetParamFloat\x12&.mavsdk.rpc.param.GetParamFloatRequest\x1a\'.mavsdk.rpc.param.GetParamFloatResponse\"\x04\x80\xb5\x18\x01\x12\x66\n\rSetParamFloat\x12&.mavsdk.rpc.param.SetParamFloatRequest\x1a\'.mavsdk.rpc.param.SetParamFloatResponse\"\x04\x80\xb5\x18\x01\x12\x63\n\x0cGetAllParams\x12%.mavsdk.rpc.param.GetAllParamsRequest\x1a&.mavsdk.rpc.param.GetAllParamsResponse\"\x04\x80\xb5\x18\x01\x42\x1d\n\x0fio.mavsdk.paramB\nParamProtob\x06proto3')



_GETPARAMINTREQUEST = DESCRIPTOR.message_types_by_name['GetParamIntRequest']
_GETPARAMINTRESPONSE = DESCRIPTOR.message_types_by_name['GetParamIntResponse']
_SETPARAMINTREQUEST = DESCRIPTOR.message_types_by_name['SetParamIntRequest']
_SETPARAMINTRESPONSE = DESCRIPTOR.message_types_by_name['SetParamIntResponse']
_GETPARAMFLOATREQUEST = DESCRIPTOR.message_types_by_name['GetParamFloatRequest']
_GETPARAMFLOATRESPONSE = DESCRIPTOR.message_types_by_name['GetParamFloatResponse']
_SETPARAMFLOATREQUEST = DESCRIPTOR.message_types_by_name['SetParamFloatRequest']
_SETPARAMFLOATRESPONSE = DESCRIPTOR.message_types_by_name['SetParamFloatResponse']
_GETALLPARAMSREQUEST = DESCRIPTOR.message_types_by_name['GetAllParamsRequest']
_GETALLPARAMSRESPONSE = DESCRIPTOR.message_types_by_name['GetAllParamsResponse']
_INTPARAM = DESCRIPTOR.message_types_by_name['IntParam']
_FLOATPARAM = DESCRIPTOR.message_types_by_name['FloatParam']
_ALLPARAMS = DESCRIPTOR.message_types_by_name['AllParams']
_PARAMRESULT = DESCRIPTOR.message_types_by_name['ParamResult']
_PARAMRESULT_RESULT = _PARAMRESULT.enum_types_by_name['Result']
GetParamIntRequest = _reflection.GeneratedProtocolMessageType('GetParamIntRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPARAMINTREQUEST,
  '__module__' : 'param.param_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param.GetParamIntRequest)
  })
_sym_db.RegisterMessage(GetParamIntRequest)

GetParamIntResponse = _reflection.GeneratedProtocolMessageType('GetParamIntResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPARAMINTRESPONSE,
  '__module__' : 'param.param_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param.GetParamIntResponse)
  })
_sym_db.RegisterMessage(GetParamIntResponse)

SetParamIntRequest = _reflection.GeneratedProtocolMessageType('SetParamIntRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETPARAMINTREQUEST,
  '__module__' : 'param.param_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param.SetParamIntRequest)
  })
_sym_db.RegisterMessage(SetParamIntRequest)

SetParamIntResponse = _reflection.GeneratedProtocolMessageType('SetParamIntResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETPARAMINTRESPONSE,
  '__module__' : 'param.param_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param.SetParamIntResponse)
  })
_sym_db.RegisterMessage(SetParamIntResponse)

GetParamFloatRequest = _reflection.GeneratedProtocolMessageType('GetParamFloatRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPARAMFLOATREQUEST,
  '__module__' : 'param.param_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param.GetParamFloatRequest)
  })
_sym_db.RegisterMessage(GetParamFloatRequest)

GetParamFloatResponse = _reflection.GeneratedProtocolMessageType('GetParamFloatResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPARAMFLOATRESPONSE,
  '__module__' : 'param.param_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param.GetParamFloatResponse)
  })
_sym_db.RegisterMessage(GetParamFloatResponse)

SetParamFloatRequest = _reflection.GeneratedProtocolMessageType('SetParamFloatRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETPARAMFLOATREQUEST,
  '__module__' : 'param.param_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param.SetParamFloatRequest)
  })
_sym_db.RegisterMessage(SetParamFloatRequest)

SetParamFloatResponse = _reflection.GeneratedProtocolMessageType('SetParamFloatResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETPARAMFLOATRESPONSE,
  '__module__' : 'param.param_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param.SetParamFloatResponse)
  })
_sym_db.RegisterMessage(SetParamFloatResponse)

GetAllParamsRequest = _reflection.GeneratedProtocolMessageType('GetAllParamsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETALLPARAMSREQUEST,
  '__module__' : 'param.param_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param.GetAllParamsRequest)
  })
_sym_db.RegisterMessage(GetAllParamsRequest)

GetAllParamsResponse = _reflection.GeneratedProtocolMessageType('GetAllParamsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETALLPARAMSRESPONSE,
  '__module__' : 'param.param_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param.GetAllParamsResponse)
  })
_sym_db.RegisterMessage(GetAllParamsResponse)

IntParam = _reflection.GeneratedProtocolMessageType('IntParam', (_message.Message,), {
  'DESCRIPTOR' : _INTPARAM,
  '__module__' : 'param.param_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param.IntParam)
  })
_sym_db.RegisterMessage(IntParam)

FloatParam = _reflection.GeneratedProtocolMessageType('FloatParam', (_message.Message,), {
  'DESCRIPTOR' : _FLOATPARAM,
  '__module__' : 'param.param_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param.FloatParam)
  })
_sym_db.RegisterMessage(FloatParam)

AllParams = _reflection.GeneratedProtocolMessageType('AllParams', (_message.Message,), {
  'DESCRIPTOR' : _ALLPARAMS,
  '__module__' : 'param.param_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param.AllParams)
  })
_sym_db.RegisterMessage(AllParams)

ParamResult = _reflection.GeneratedProtocolMessageType('ParamResult', (_message.Message,), {
  'DESCRIPTOR' : _PARAMRESULT,
  '__module__' : 'param.param_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param.ParamResult)
  })
_sym_db.RegisterMessage(ParamResult)

_PARAMSERVICE = DESCRIPTOR.services_by_name['ParamService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\017io.mavsdk.paramB\nParamProto'
  _PARAMSERVICE.methods_by_name['GetParamInt']._options = None
  _PARAMSERVICE.methods_by_name['GetParamInt']._serialized_options = b'\200\265\030\001'
  _PARAMSERVICE.methods_by_name['SetParamInt']._options = None
  _PARAMSERVICE.methods_by_name['SetParamInt']._serialized_options = b'\200\265\030\001'
  _PARAMSERVICE.methods_by_name['GetParamFloat']._options = None
  _PARAMSERVICE.methods_by_name['GetParamFloat']._serialized_options = b'\200\265\030\001'
  _PARAMSERVICE.methods_by_name['SetParamFloat']._options = None
  _PARAMSERVICE.methods_by_name['SetParamFloat']._serialized_options = b'\200\265\030\001'
  _PARAMSERVICE.methods_by_name['GetAllParams']._options = None
  _PARAMSERVICE.methods_by_name['GetAllParams']._serialized_options = b'\200\265\030\001'
  _GETPARAMINTREQUEST._serialized_start=61
  _GETPARAMINTREQUEST._serialized_end=95
  _GETPARAMINTRESPONSE._serialized_start=97
  _GETPARAMINTRESPONSE._serialized_end=186
  _SETPARAMINTREQUEST._serialized_start=188
  _SETPARAMINTREQUEST._serialized_end=237
  _SETPARAMINTRESPONSE._serialized_start=239
  _SETPARAMINTRESPONSE._serialized_end=313
  _GETPARAMFLOATREQUEST._serialized_start=315
  _GETPARAMFLOATREQUEST._serialized_end=351
  _GETPARAMFLOATRESPONSE._serialized_start=353
  _GETPARAMFLOATRESPONSE._serialized_end=444
  _SETPARAMFLOATREQUEST._serialized_start=446
  _SETPARAMFLOATREQUEST._serialized_end=497
  _SETPARAMFLOATRESPONSE._serialized_start=499
  _SETPARAMFLOATRESPONSE._serialized_end=575
  _GETALLPARAMSREQUEST._serialized_start=577
  _GETALLPARAMSREQUEST._serialized_end=598
  _GETALLPARAMSRESPONSE._serialized_start=600
  _GETALLPARAMSRESPONSE._serialized_end=667
  _INTPARAM._serialized_start=669
  _INTPARAM._serialized_end=708
  _FLOATPARAM._serialized_start=710
  _FLOATPARAM._serialized_end=751
  _ALLPARAMS._serialized_start=753
  _ALLPARAMS._serialized_end=864
  _PARAMRESULT._serialized_start=867
  _PARAMRESULT._serialized_end=1131
  _PARAMRESULT_RESULT._serialized_start=957
  _PARAMRESULT_RESULT._serialized_end=1131
  _PARAMSERVICE._serialized_start=1134
  _PARAMSERVICE._serialized_end=1653
# @@protoc_insertion_point(module_scope)
