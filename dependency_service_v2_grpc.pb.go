// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.2.0
// - protoc             v3.20.1
// source: services/dependency_service_v2.proto

package grpc

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

// DependencyServiceV2Client is the client API for DependencyServiceV2 service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type DependencyServiceV2Client interface {
	Connect(ctx context.Context, opts ...grpc.CallOption) (DependencyServiceV2_ConnectClient, error)
	Sync(ctx context.Context, in *DependenciesServiceV2SyncRequest, opts ...grpc.CallOption) (*Response, error)
	Install(ctx context.Context, opts ...grpc.CallOption) (DependencyServiceV2_InstallClient, error)
	UninstallDependencies(ctx context.Context, opts ...grpc.CallOption) (DependencyServiceV2_UninstallDependenciesClient, error)
}

type dependencyServiceV2Client struct {
	cc grpc.ClientConnInterface
}

func NewDependencyServiceV2Client(cc grpc.ClientConnInterface) DependencyServiceV2Client {
	return &dependencyServiceV2Client{cc}
}

func (c *dependencyServiceV2Client) Connect(ctx context.Context, opts ...grpc.CallOption) (DependencyServiceV2_ConnectClient, error) {
	stream, err := c.cc.NewStream(ctx, &DependencyServiceV2_ServiceDesc.Streams[0], "/grpc.DependencyServiceV2/Connect", opts...)
	if err != nil {
		return nil, err
	}
	x := &dependencyServiceV2ConnectClient{stream}
	return x, nil
}

type DependencyServiceV2_ConnectClient interface {
	Send(*DependenciesServiceV2ConnectRequest) error
	CloseAndRecv() (*Response, error)
	grpc.ClientStream
}

type dependencyServiceV2ConnectClient struct {
	grpc.ClientStream
}

func (x *dependencyServiceV2ConnectClient) Send(m *DependenciesServiceV2ConnectRequest) error {
	return x.ClientStream.SendMsg(m)
}

func (x *dependencyServiceV2ConnectClient) CloseAndRecv() (*Response, error) {
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	m := new(Response)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

func (c *dependencyServiceV2Client) Sync(ctx context.Context, in *DependenciesServiceV2SyncRequest, opts ...grpc.CallOption) (*Response, error) {
	out := new(Response)
	err := c.cc.Invoke(ctx, "/grpc.DependencyServiceV2/Sync", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *dependencyServiceV2Client) Install(ctx context.Context, opts ...grpc.CallOption) (DependencyServiceV2_InstallClient, error) {
	stream, err := c.cc.NewStream(ctx, &DependencyServiceV2_ServiceDesc.Streams[1], "/grpc.DependencyServiceV2/Install", opts...)
	if err != nil {
		return nil, err
	}
	x := &dependencyServiceV2InstallClient{stream}
	return x, nil
}

type DependencyServiceV2_InstallClient interface {
	Send(*DependenciesServiceV2InstallRequest) error
	Recv() (*Response, error)
	grpc.ClientStream
}

type dependencyServiceV2InstallClient struct {
	grpc.ClientStream
}

func (x *dependencyServiceV2InstallClient) Send(m *DependenciesServiceV2InstallRequest) error {
	return x.ClientStream.SendMsg(m)
}

func (x *dependencyServiceV2InstallClient) Recv() (*Response, error) {
	m := new(Response)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

func (c *dependencyServiceV2Client) UninstallDependencies(ctx context.Context, opts ...grpc.CallOption) (DependencyServiceV2_UninstallDependenciesClient, error) {
	stream, err := c.cc.NewStream(ctx, &DependencyServiceV2_ServiceDesc.Streams[2], "/grpc.DependencyServiceV2/UninstallDependencies", opts...)
	if err != nil {
		return nil, err
	}
	x := &dependencyServiceV2UninstallDependenciesClient{stream}
	return x, nil
}

type DependencyServiceV2_UninstallDependenciesClient interface {
	Send(*DependenciesServiceV2UninstallRequest) error
	Recv() (*Response, error)
	grpc.ClientStream
}

type dependencyServiceV2UninstallDependenciesClient struct {
	grpc.ClientStream
}

func (x *dependencyServiceV2UninstallDependenciesClient) Send(m *DependenciesServiceV2UninstallRequest) error {
	return x.ClientStream.SendMsg(m)
}

func (x *dependencyServiceV2UninstallDependenciesClient) Recv() (*Response, error) {
	m := new(Response)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

// DependencyServiceV2Server is the server API for DependencyServiceV2 service.
// All implementations must embed UnimplementedDependencyServiceV2Server
// for forward compatibility
type DependencyServiceV2Server interface {
	Connect(DependencyServiceV2_ConnectServer) error
	Sync(context.Context, *DependenciesServiceV2SyncRequest) (*Response, error)
	Install(DependencyServiceV2_InstallServer) error
	UninstallDependencies(DependencyServiceV2_UninstallDependenciesServer) error
	mustEmbedUnimplementedDependencyServiceV2Server()
}

// UnimplementedDependencyServiceV2Server must be embedded to have forward compatible implementations.
type UnimplementedDependencyServiceV2Server struct {
}

func (UnimplementedDependencyServiceV2Server) Connect(DependencyServiceV2_ConnectServer) error {
	return status.Errorf(codes.Unimplemented, "method Connect not implemented")
}
func (UnimplementedDependencyServiceV2Server) Sync(context.Context, *DependenciesServiceV2SyncRequest) (*Response, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Sync not implemented")
}
func (UnimplementedDependencyServiceV2Server) Install(DependencyServiceV2_InstallServer) error {
	return status.Errorf(codes.Unimplemented, "method Install not implemented")
}
func (UnimplementedDependencyServiceV2Server) UninstallDependencies(DependencyServiceV2_UninstallDependenciesServer) error {
	return status.Errorf(codes.Unimplemented, "method UninstallDependencies not implemented")
}
func (UnimplementedDependencyServiceV2Server) mustEmbedUnimplementedDependencyServiceV2Server() {}

// UnsafeDependencyServiceV2Server may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to DependencyServiceV2Server will
// result in compilation errors.
type UnsafeDependencyServiceV2Server interface {
	mustEmbedUnimplementedDependencyServiceV2Server()
}

func RegisterDependencyServiceV2Server(s grpc.ServiceRegistrar, srv DependencyServiceV2Server) {
	s.RegisterService(&DependencyServiceV2_ServiceDesc, srv)
}

func _DependencyServiceV2_Connect_Handler(srv interface{}, stream grpc.ServerStream) error {
	return srv.(DependencyServiceV2Server).Connect(&dependencyServiceV2ConnectServer{stream})
}

type DependencyServiceV2_ConnectServer interface {
	SendAndClose(*Response) error
	Recv() (*DependenciesServiceV2ConnectRequest, error)
	grpc.ServerStream
}

type dependencyServiceV2ConnectServer struct {
	grpc.ServerStream
}

func (x *dependencyServiceV2ConnectServer) SendAndClose(m *Response) error {
	return x.ServerStream.SendMsg(m)
}

func (x *dependencyServiceV2ConnectServer) Recv() (*DependenciesServiceV2ConnectRequest, error) {
	m := new(DependenciesServiceV2ConnectRequest)
	if err := x.ServerStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

func _DependencyServiceV2_Sync_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(DependenciesServiceV2SyncRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DependencyServiceV2Server).Sync(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/grpc.DependencyServiceV2/Sync",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DependencyServiceV2Server).Sync(ctx, req.(*DependenciesServiceV2SyncRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _DependencyServiceV2_Install_Handler(srv interface{}, stream grpc.ServerStream) error {
	return srv.(DependencyServiceV2Server).Install(&dependencyServiceV2InstallServer{stream})
}

type DependencyServiceV2_InstallServer interface {
	Send(*Response) error
	Recv() (*DependenciesServiceV2InstallRequest, error)
	grpc.ServerStream
}

type dependencyServiceV2InstallServer struct {
	grpc.ServerStream
}

func (x *dependencyServiceV2InstallServer) Send(m *Response) error {
	return x.ServerStream.SendMsg(m)
}

func (x *dependencyServiceV2InstallServer) Recv() (*DependenciesServiceV2InstallRequest, error) {
	m := new(DependenciesServiceV2InstallRequest)
	if err := x.ServerStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

func _DependencyServiceV2_UninstallDependencies_Handler(srv interface{}, stream grpc.ServerStream) error {
	return srv.(DependencyServiceV2Server).UninstallDependencies(&dependencyServiceV2UninstallDependenciesServer{stream})
}

type DependencyServiceV2_UninstallDependenciesServer interface {
	Send(*Response) error
	Recv() (*DependenciesServiceV2UninstallRequest, error)
	grpc.ServerStream
}

type dependencyServiceV2UninstallDependenciesServer struct {
	grpc.ServerStream
}

func (x *dependencyServiceV2UninstallDependenciesServer) Send(m *Response) error {
	return x.ServerStream.SendMsg(m)
}

func (x *dependencyServiceV2UninstallDependenciesServer) Recv() (*DependenciesServiceV2UninstallRequest, error) {
	m := new(DependenciesServiceV2UninstallRequest)
	if err := x.ServerStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

// DependencyServiceV2_ServiceDesc is the grpc.ServiceDesc for DependencyServiceV2 service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var DependencyServiceV2_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "grpc.DependencyServiceV2",
	HandlerType: (*DependencyServiceV2Server)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Sync",
			Handler:    _DependencyServiceV2_Sync_Handler,
		},
	},
	Streams: []grpc.StreamDesc{
		{
			StreamName:    "Connect",
			Handler:       _DependencyServiceV2_Connect_Handler,
			ClientStreams: true,
		},
		{
			StreamName:    "Install",
			Handler:       _DependencyServiceV2_Install_Handler,
			ServerStreams: true,
			ClientStreams: true,
		},
		{
			StreamName:    "UninstallDependencies",
			Handler:       _DependencyServiceV2_UninstallDependencies_Handler,
			ServerStreams: true,
			ClientStreams: true,
		},
	},
	Metadata: "services/dependency_service_v2.proto",
}
