import grpc
import matrix_pb2
import matrix_pb2_grpc
import time
def run():
    start_time = time.time()
    # Establish a connection to the gRPC server
    channel = grpc.insecure_channel('localhost:50051')
    stub = matrix_pb2_grpc.MatrixServiceStub(channel)

    # Create a request message
    request = matrix_pb2.MatrixRequest(size=500)

    # Make the gRPC call
    try:
        response = stub.MultiplyMatrices(request)
        print("Matrix multiplication result:")
        print(response.result)  # This will print the result of the matrix multiplication
    except grpc.RpcError as e:
        print(f"Error occurred: {e.details()}")

    end_time = time.time()
    print(f"Time taken for the operation: {end_time - start_time} seconds")
if __name__ == '__main__':
    run()
