// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: models/task.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace Grpc {

  /// <summary>Holder for reflection information generated from models/task.proto</summary>
  public static partial class TaskReflection {

    #region Descriptor
    /// <summary>File descriptor for models/task.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static TaskReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "ChFtb2RlbHMvdGFzay5wcm90bxIEZ3JwYyK0AQoEVGFzaxILCgNfaWQYASAB",
            "KAkSEQoJc3BpZGVyX2lkGAIgASgJEg4KBnN0YXR1cxgFIAEoCRIPCgdub2Rl",
            "X2lkGAYgASgJEgsKA2NtZBgIIAEoCRINCgVwYXJhbRgJIAEoCRINCgVlcnJv",
            "chgKIAEoCRILCgNwaWQYECABKAUSEAoIcnVuX3R5cGUYESABKAkSEwoLc2No",
            "ZWR1bGVfaWQYEiABKAkSDAoEdHlwZRgTIAEoCUIIWgYuO2dycGNiBnByb3Rv",
            "Mw=="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { },
          new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::Grpc.Task), global::Grpc.Task.Parser, new[]{ "Id", "SpiderId", "Status", "NodeId", "Cmd", "Param", "Error", "Pid", "RunType", "ScheduleId", "Type" }, null, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class Task : pb::IMessage<Task>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<Task> _parser = new pb::MessageParser<Task>(() => new Task());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pb::MessageParser<Task> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Grpc.TaskReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public Task() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public Task(Task other) : this() {
      Id_ = other.Id_;
      spiderId_ = other.spiderId_;
      status_ = other.status_;
      nodeId_ = other.nodeId_;
      cmd_ = other.cmd_;
      param_ = other.param_;
      error_ = other.error_;
      pid_ = other.pid_;
      runType_ = other.runType_;
      scheduleId_ = other.scheduleId_;
      type_ = other.type_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public Task Clone() {
      return new Task(this);
    }

    /// <summary>Field number for the "_id" field.</summary>
    public const int IdFieldNumber = 1;
    private string Id_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Id {
      get { return Id_; }
      set {
        Id_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "spider_id" field.</summary>
    public const int SpiderIdFieldNumber = 2;
    private string spiderId_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string SpiderId {
      get { return spiderId_; }
      set {
        spiderId_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "status" field.</summary>
    public const int StatusFieldNumber = 5;
    private string status_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Status {
      get { return status_; }
      set {
        status_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "node_id" field.</summary>
    public const int NodeIdFieldNumber = 6;
    private string nodeId_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string NodeId {
      get { return nodeId_; }
      set {
        nodeId_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "cmd" field.</summary>
    public const int CmdFieldNumber = 8;
    private string cmd_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Cmd {
      get { return cmd_; }
      set {
        cmd_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "param" field.</summary>
    public const int ParamFieldNumber = 9;
    private string param_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Param {
      get { return param_; }
      set {
        param_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "error" field.</summary>
    public const int ErrorFieldNumber = 10;
    private string error_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Error {
      get { return error_; }
      set {
        error_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "pid" field.</summary>
    public const int PidFieldNumber = 16;
    private int pid_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public int Pid {
      get { return pid_; }
      set {
        pid_ = value;
      }
    }

    /// <summary>Field number for the "run_type" field.</summary>
    public const int RunTypeFieldNumber = 17;
    private string runType_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string RunType {
      get { return runType_; }
      set {
        runType_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "schedule_id" field.</summary>
    public const int ScheduleIdFieldNumber = 18;
    private string scheduleId_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string ScheduleId {
      get { return scheduleId_; }
      set {
        scheduleId_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "type" field.</summary>
    public const int TypeFieldNumber = 19;
    private string type_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Type {
      get { return type_; }
      set {
        type_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override bool Equals(object other) {
      return Equals(other as Task);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public bool Equals(Task other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (Id != other.Id) return false;
      if (SpiderId != other.SpiderId) return false;
      if (Status != other.Status) return false;
      if (NodeId != other.NodeId) return false;
      if (Cmd != other.Cmd) return false;
      if (Param != other.Param) return false;
      if (Error != other.Error) return false;
      if (Pid != other.Pid) return false;
      if (RunType != other.RunType) return false;
      if (ScheduleId != other.ScheduleId) return false;
      if (Type != other.Type) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override int GetHashCode() {
      int hash = 1;
      if (Id.Length != 0) hash ^= Id.GetHashCode();
      if (SpiderId.Length != 0) hash ^= SpiderId.GetHashCode();
      if (Status.Length != 0) hash ^= Status.GetHashCode();
      if (NodeId.Length != 0) hash ^= NodeId.GetHashCode();
      if (Cmd.Length != 0) hash ^= Cmd.GetHashCode();
      if (Param.Length != 0) hash ^= Param.GetHashCode();
      if (Error.Length != 0) hash ^= Error.GetHashCode();
      if (Pid != 0) hash ^= Pid.GetHashCode();
      if (RunType.Length != 0) hash ^= RunType.GetHashCode();
      if (ScheduleId.Length != 0) hash ^= ScheduleId.GetHashCode();
      if (Type.Length != 0) hash ^= Type.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void WriteTo(pb::CodedOutputStream output) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      output.WriteRawMessage(this);
    #else
      if (Id.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(Id);
      }
      if (SpiderId.Length != 0) {
        output.WriteRawTag(18);
        output.WriteString(SpiderId);
      }
      if (Status.Length != 0) {
        output.WriteRawTag(42);
        output.WriteString(Status);
      }
      if (NodeId.Length != 0) {
        output.WriteRawTag(50);
        output.WriteString(NodeId);
      }
      if (Cmd.Length != 0) {
        output.WriteRawTag(66);
        output.WriteString(Cmd);
      }
      if (Param.Length != 0) {
        output.WriteRawTag(74);
        output.WriteString(Param);
      }
      if (Error.Length != 0) {
        output.WriteRawTag(82);
        output.WriteString(Error);
      }
      if (Pid != 0) {
        output.WriteRawTag(128, 1);
        output.WriteInt32(Pid);
      }
      if (RunType.Length != 0) {
        output.WriteRawTag(138, 1);
        output.WriteString(RunType);
      }
      if (ScheduleId.Length != 0) {
        output.WriteRawTag(146, 1);
        output.WriteString(ScheduleId);
      }
      if (Type.Length != 0) {
        output.WriteRawTag(154, 1);
        output.WriteString(Type);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
      if (Id.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(Id);
      }
      if (SpiderId.Length != 0) {
        output.WriteRawTag(18);
        output.WriteString(SpiderId);
      }
      if (Status.Length != 0) {
        output.WriteRawTag(42);
        output.WriteString(Status);
      }
      if (NodeId.Length != 0) {
        output.WriteRawTag(50);
        output.WriteString(NodeId);
      }
      if (Cmd.Length != 0) {
        output.WriteRawTag(66);
        output.WriteString(Cmd);
      }
      if (Param.Length != 0) {
        output.WriteRawTag(74);
        output.WriteString(Param);
      }
      if (Error.Length != 0) {
        output.WriteRawTag(82);
        output.WriteString(Error);
      }
      if (Pid != 0) {
        output.WriteRawTag(128, 1);
        output.WriteInt32(Pid);
      }
      if (RunType.Length != 0) {
        output.WriteRawTag(138, 1);
        output.WriteString(RunType);
      }
      if (ScheduleId.Length != 0) {
        output.WriteRawTag(146, 1);
        output.WriteString(ScheduleId);
      }
      if (Type.Length != 0) {
        output.WriteRawTag(154, 1);
        output.WriteString(Type);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(ref output);
      }
    }
    #endif

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public int CalculateSize() {
      int size = 0;
      if (Id.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Id);
      }
      if (SpiderId.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(SpiderId);
      }
      if (Status.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Status);
      }
      if (NodeId.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(NodeId);
      }
      if (Cmd.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Cmd);
      }
      if (Param.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Param);
      }
      if (Error.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Error);
      }
      if (Pid != 0) {
        size += 2 + pb::CodedOutputStream.ComputeInt32Size(Pid);
      }
      if (RunType.Length != 0) {
        size += 2 + pb::CodedOutputStream.ComputeStringSize(RunType);
      }
      if (ScheduleId.Length != 0) {
        size += 2 + pb::CodedOutputStream.ComputeStringSize(ScheduleId);
      }
      if (Type.Length != 0) {
        size += 2 + pb::CodedOutputStream.ComputeStringSize(Type);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(Task other) {
      if (other == null) {
        return;
      }
      if (other.Id.Length != 0) {
        Id = other.Id;
      }
      if (other.SpiderId.Length != 0) {
        SpiderId = other.SpiderId;
      }
      if (other.Status.Length != 0) {
        Status = other.Status;
      }
      if (other.NodeId.Length != 0) {
        NodeId = other.NodeId;
      }
      if (other.Cmd.Length != 0) {
        Cmd = other.Cmd;
      }
      if (other.Param.Length != 0) {
        Param = other.Param;
      }
      if (other.Error.Length != 0) {
        Error = other.Error;
      }
      if (other.Pid != 0) {
        Pid = other.Pid;
      }
      if (other.RunType.Length != 0) {
        RunType = other.RunType;
      }
      if (other.ScheduleId.Length != 0) {
        ScheduleId = other.ScheduleId;
      }
      if (other.Type.Length != 0) {
        Type = other.Type;
      }
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(pb::CodedInputStream input) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      input.ReadRawMessage(this);
    #else
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 10: {
            Id = input.ReadString();
            break;
          }
          case 18: {
            SpiderId = input.ReadString();
            break;
          }
          case 42: {
            Status = input.ReadString();
            break;
          }
          case 50: {
            NodeId = input.ReadString();
            break;
          }
          case 66: {
            Cmd = input.ReadString();
            break;
          }
          case 74: {
            Param = input.ReadString();
            break;
          }
          case 82: {
            Error = input.ReadString();
            break;
          }
          case 128: {
            Pid = input.ReadInt32();
            break;
          }
          case 138: {
            RunType = input.ReadString();
            break;
          }
          case 146: {
            ScheduleId = input.ReadString();
            break;
          }
          case 154: {
            Type = input.ReadString();
            break;
          }
        }
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalMergeFrom(ref pb::ParseContext input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, ref input);
            break;
          case 10: {
            Id = input.ReadString();
            break;
          }
          case 18: {
            SpiderId = input.ReadString();
            break;
          }
          case 42: {
            Status = input.ReadString();
            break;
          }
          case 50: {
            NodeId = input.ReadString();
            break;
          }
          case 66: {
            Cmd = input.ReadString();
            break;
          }
          case 74: {
            Param = input.ReadString();
            break;
          }
          case 82: {
            Error = input.ReadString();
            break;
          }
          case 128: {
            Pid = input.ReadInt32();
            break;
          }
          case 138: {
            RunType = input.ReadString();
            break;
          }
          case 146: {
            ScheduleId = input.ReadString();
            break;
          }
          case 154: {
            Type = input.ReadString();
            break;
          }
        }
      }
    }
    #endif

  }

  #endregion

}

#endregion Designer generated code