# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: laserscan_raw.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='laserscan_raw.proto',
  package='make87_messages.lidar.laserscan',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13laserscan_raw.proto\x12\x1fmake87_messages.lidar.laserscan\x1a\x1fgoogle/protobuf/timestamp.proto\"\xd9\x01\n\x0cLaserScanRaw\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x11\n\tangle_min\x18\x02 \x01(\x02\x12\x11\n\tangle_max\x18\x03 \x01(\x02\x12\x17\n\x0f\x61ngle_increment\x18\x04 \x01(\x02\x12\x11\n\trange_min\x18\x05 \x01(\x02\x12\x11\n\trange_max\x18\x06 \x01(\x02\x12\x0e\n\x06ranges\x18\x07 \x03(\x02\x12\x13\n\x0bintensities\x18\x08 \x03(\x02\x12\x10\n\x08\x63hecksum\x18\t \x01(\rb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_LASERSCANRAW = _descriptor.Descriptor(
  name='LaserScanRaw',
  full_name='make87_messages.lidar.laserscan.LaserScanRaw',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='make87_messages.lidar.laserscan.LaserScanRaw.timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='angle_min', full_name='make87_messages.lidar.laserscan.LaserScanRaw.angle_min', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='angle_max', full_name='make87_messages.lidar.laserscan.LaserScanRaw.angle_max', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='angle_increment', full_name='make87_messages.lidar.laserscan.LaserScanRaw.angle_increment', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='range_min', full_name='make87_messages.lidar.laserscan.LaserScanRaw.range_min', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='range_max', full_name='make87_messages.lidar.laserscan.LaserScanRaw.range_max', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ranges', full_name='make87_messages.lidar.laserscan.LaserScanRaw.ranges', index=6,
      number=7, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='intensities', full_name='make87_messages.lidar.laserscan.LaserScanRaw.intensities', index=7,
      number=8, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='checksum', full_name='make87_messages.lidar.laserscan.LaserScanRaw.checksum', index=8,
      number=9, type=13, cpp_type=3, label=1,
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
  serialized_start=90,
  serialized_end=307,
)

_LASERSCANRAW.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['LaserScanRaw'] = _LASERSCANRAW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LaserScanRaw = _reflection.GeneratedProtocolMessageType('LaserScanRaw', (_message.Message,), {
  'DESCRIPTOR' : _LASERSCANRAW,
  '__module__' : 'laserscan_raw_pb2'
  # @@protoc_insertion_point(class_scope:make87_messages.lidar.laserscan.LaserScanRaw)
  })
_sym_db.RegisterMessage(LaserScanRaw)


# @@protoc_insertion_point(module_scope)
