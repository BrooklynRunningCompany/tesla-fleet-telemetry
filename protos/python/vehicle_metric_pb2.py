# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: vehicle_metric.proto
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
    'vehicle_metric.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14vehicle_metric.proto\x12\x19telemetry.vehicle_metrics\x1a\x1fgoogle/protobuf/timestamp.proto\"\x81\x01\n\x0eVehicleMetrics\x12\x32\n\x07metrics\x18\x01 \x03(\x0b\x32!.telemetry.vehicle_metrics.Metric\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0b\n\x03vin\x18\x03 \x01(\t\"\x8d\x01\n\x06Metric\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x39\n\x04tags\x18\x02 \x03(\x0b\x32+.telemetry.vehicle_metrics.Metric.TagsEntry\x12\r\n\x05value\x18\x03 \x01(\x01\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42/Z-github.com/teslamotors/fleet-telemetry/protosb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vehicle_metric_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z-github.com/teslamotors/fleet-telemetry/protos'
  _globals['_METRIC_TAGSENTRY']._loaded_options = None
  _globals['_METRIC_TAGSENTRY']._serialized_options = b'8\001'
  _globals['_VEHICLEMETRICS']._serialized_start=85
  _globals['_VEHICLEMETRICS']._serialized_end=214
  _globals['_METRIC']._serialized_start=217
  _globals['_METRIC']._serialized_end=358
  _globals['_METRIC_TAGSENTRY']._serialized_start=315
  _globals['_METRIC_TAGSENTRY']._serialized_end=358
# @@protoc_insertion_point(module_scope)
