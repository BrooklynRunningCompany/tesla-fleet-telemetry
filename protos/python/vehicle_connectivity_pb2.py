# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: vehicle_connectivity.proto
# Protobuf Python Version: 5.29.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    3,
    '',
    'vehicle_connectivity.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1avehicle_connectivity.proto\x12\x1etelemetry.vehicle_connectivity\x1a\x1fgoogle/protobuf/timestamp.proto\"\xc7\x01\n\x13VehicleConnectivity\x12\x0b\n\x03vin\x18\x01 \x01(\t\x12\x15\n\rconnection_id\x18\x02 \x01(\t\x12\x41\n\x06status\x18\x03 \x01(\x0e\x32\x31.telemetry.vehicle_connectivity.ConnectivityEvent\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x19\n\x11network_interface\x18\x05 \x01(\t*A\n\x11\x43onnectivityEvent\x12\x0b\n\x07UNKNOWN\x10\x00\x12\r\n\tCONNECTED\x10\x01\x12\x10\n\x0c\x44ISCONNECTED\x10\x02\x42/Z-github.com/teslamotors/fleet-telemetry/protosb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vehicle_connectivity_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z-github.com/teslamotors/fleet-telemetry/protos'
  _globals['_CONNECTIVITYEVENT']._serialized_start=297
  _globals['_CONNECTIVITYEVENT']._serialized_end=362
  _globals['_VEHICLECONNECTIVITY']._serialized_start=96
  _globals['_VEHICLECONNECTIVITY']._serialized_end=295
# @@protoc_insertion_point(module_scope)
