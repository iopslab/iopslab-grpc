// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: services/node_service.proto

package grpc;

public final class NodeServiceOuterClass {
  private NodeServiceOuterClass() {}
  public static void registerAllExtensions(
      com.google.protobuf.ExtensionRegistryLite registry) {
  }

  public static void registerAllExtensions(
      com.google.protobuf.ExtensionRegistry registry) {
    registerAllExtensions(
        (com.google.protobuf.ExtensionRegistryLite) registry);
  }

  public static com.google.protobuf.Descriptors.FileDescriptor
      getDescriptor() {
    return descriptor;
  }
  private static  com.google.protobuf.Descriptors.FileDescriptor
      descriptor;
  static {
    java.lang.String[] descriptorData = {
      "\n\033services/node_service.proto\022\004grpc\032\024ent" +
      "ity/request.proto\032\025entity/response.proto" +
      "\032\033entity/stream_message.proto2\372\001\n\013NodeSe" +
      "rvice\022+\n\010Register\022\r.grpc.Request\032\016.grpc." +
      "Response\"\000\0220\n\rSendHeartbeat\022\r.grpc.Reque" +
      "st\032\016.grpc.Response\"\000\022\'\n\004Ping\022\r.grpc.Requ" +
      "est\032\016.grpc.Response\"\000\0223\n\tSubscribe\022\r.grp" +
      "c.Request\032\023.grpc.StreamMessage\"\0000\001\022.\n\013Un" +
      "subscribe\022\r.grpc.Request\032\016.grpc.Response" +
      "\"\000B\010Z\006.;grpcb\006proto3"
    };
    descriptor = com.google.protobuf.Descriptors.FileDescriptor
      .internalBuildGeneratedFileFrom(descriptorData,
        new com.google.protobuf.Descriptors.FileDescriptor[] {
          grpc.RequestOuterClass.getDescriptor(),
          grpc.ResponseOuterClass.getDescriptor(),
          grpc.StreamMessageOuterClass.getDescriptor(),
        });
    grpc.RequestOuterClass.getDescriptor();
    grpc.ResponseOuterClass.getDescriptor();
    grpc.StreamMessageOuterClass.getDescriptor();
  }

  // @@protoc_insertion_point(outer_class_scope)
}
