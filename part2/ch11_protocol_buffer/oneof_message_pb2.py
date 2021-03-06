# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: oneof_message.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='oneof_message.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13oneof_message.proto\"*\n\x05Login\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"$\n\x07Product\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\x03\"9\n\x05Order\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x1a\n\x08products\x18\x02 \x03(\x0b\x32\x08.Product\"L\n\x06Refund\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x10\n\x08order_id\x18\x02 \x01(\t\x12\x1a\n\x08products\x18\x03 \x03(\x0b\x32\x08.Product\"`\n\nRequestMsg\x12\x17\n\x05login\x18\x01 \x01(\x0b\x32\x06.LoginH\x00\x12\x17\n\x05order\x18\x02 \x01(\x0b\x32\x06.OrderH\x00\x12\x19\n\x06refund\x18\x03 \x01(\x0b\x32\x07.RefundH\x00\x42\x05\n\x03msgb\x06proto3'
)




_LOGIN = _descriptor.Descriptor(
  name='Login',
  full_name='Login',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='Login.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='Login.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=23,
  serialized_end=65,
)


_PRODUCT = _descriptor.Descriptor(
  name='Product',
  full_name='Product',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Product.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='count', full_name='Product.count', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=67,
  serialized_end=103,
)


_ORDER = _descriptor.Descriptor(
  name='Order',
  full_name='Order',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='access_token', full_name='Order.access_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='products', full_name='Order.products', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=105,
  serialized_end=162,
)


_REFUND = _descriptor.Descriptor(
  name='Refund',
  full_name='Refund',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='access_token', full_name='Refund.access_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order_id', full_name='Refund.order_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='products', full_name='Refund.products', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=164,
  serialized_end=240,
)


_REQUESTMSG = _descriptor.Descriptor(
  name='RequestMsg',
  full_name='RequestMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='login', full_name='RequestMsg.login', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order', full_name='RequestMsg.order', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='refund', full_name='RequestMsg.refund', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='msg', full_name='RequestMsg.msg',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=242,
  serialized_end=338,
)

_ORDER.fields_by_name['products'].message_type = _PRODUCT
_REFUND.fields_by_name['products'].message_type = _PRODUCT
_REQUESTMSG.fields_by_name['login'].message_type = _LOGIN
_REQUESTMSG.fields_by_name['order'].message_type = _ORDER
_REQUESTMSG.fields_by_name['refund'].message_type = _REFUND
_REQUESTMSG.oneofs_by_name['msg'].fields.append(
  _REQUESTMSG.fields_by_name['login'])
_REQUESTMSG.fields_by_name['login'].containing_oneof = _REQUESTMSG.oneofs_by_name['msg']
_REQUESTMSG.oneofs_by_name['msg'].fields.append(
  _REQUESTMSG.fields_by_name['order'])
_REQUESTMSG.fields_by_name['order'].containing_oneof = _REQUESTMSG.oneofs_by_name['msg']
_REQUESTMSG.oneofs_by_name['msg'].fields.append(
  _REQUESTMSG.fields_by_name['refund'])
_REQUESTMSG.fields_by_name['refund'].containing_oneof = _REQUESTMSG.oneofs_by_name['msg']
DESCRIPTOR.message_types_by_name['Login'] = _LOGIN
DESCRIPTOR.message_types_by_name['Product'] = _PRODUCT
DESCRIPTOR.message_types_by_name['Order'] = _ORDER
DESCRIPTOR.message_types_by_name['Refund'] = _REFUND
DESCRIPTOR.message_types_by_name['RequestMsg'] = _REQUESTMSG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Login = _reflection.GeneratedProtocolMessageType('Login', (_message.Message,), {
  'DESCRIPTOR' : _LOGIN,
  '__module__' : 'oneof_message_pb2'
  # @@protoc_insertion_point(class_scope:Login)
  })
_sym_db.RegisterMessage(Login)

Product = _reflection.GeneratedProtocolMessageType('Product', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCT,
  '__module__' : 'oneof_message_pb2'
  # @@protoc_insertion_point(class_scope:Product)
  })
_sym_db.RegisterMessage(Product)

Order = _reflection.GeneratedProtocolMessageType('Order', (_message.Message,), {
  'DESCRIPTOR' : _ORDER,
  '__module__' : 'oneof_message_pb2'
  # @@protoc_insertion_point(class_scope:Order)
  })
_sym_db.RegisterMessage(Order)

Refund = _reflection.GeneratedProtocolMessageType('Refund', (_message.Message,), {
  'DESCRIPTOR' : _REFUND,
  '__module__' : 'oneof_message_pb2'
  # @@protoc_insertion_point(class_scope:Refund)
  })
_sym_db.RegisterMessage(Refund)

RequestMsg = _reflection.GeneratedProtocolMessageType('RequestMsg', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTMSG,
  '__module__' : 'oneof_message_pb2'
  # @@protoc_insertion_point(class_scope:RequestMsg)
  })
_sym_db.RegisterMessage(RequestMsg)


# @@protoc_insertion_point(module_scope)
