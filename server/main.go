package main

import (
    "context"
    "log"
    "math/rand"
    "net"
    "net/http"

    "github.com/gin-gonic/gin"
    "google.golang.org/grpc"
    "google.golang.org/grpc/credentials/insecure"
    "matrix-api/proto"  // Import the generated gRPC code as matrix
)

// Implement the MatrixServiceServer interface
type server struct {
    matrix.UnimplementedMatrixServiceServer
}

// MultiplyMatrices multiplies a 500x500 matrix with random numbers
func (s *server) MultiplyMatrices(ctx context.Context, req *matrix.MatrixRequest) (*matrix.MatrixResponse, error) {
    size := req.GetSize()
    result := make([]int32, size*size)

    // Multiply matrix with random numbers
    for i := 0; i < int(size)*int(size); i++ {
        result[i] = rand.Int31n(100)  // Random number between 0 and 99
    }

    return &matrix.MatrixResponse{Result: result}, nil
}

// Create a simple Gin API that hits the gRPC service
func apiHandler(c *gin.Context) {
    // Create gRPC client connection
    conn, err := grpc.Dial("localhost:50051", grpc.WithTransportCredentials(insecure.NewCredentials()))
    if err != nil {
        c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to connect to gRPC server"})
        return
    }
    defer conn.Close()

    client := matrix.NewMatrixServiceClient(conn)

    req := &matrix.MatrixRequest{
        Size: 5000, // Request a 500x500 matrix multiplication
    }

    resp, err := client.MultiplyMatrices(context.Background(), req)
    if err != nil {
        c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to multiply matrices"})
        return
    }

    c.JSON(http.StatusOK, gin.H{"result": resp.GetResult()})
}

func main() {
    // Set up the gRPC server
    grpcServer := grpc.NewServer()
    matrix.RegisterMatrixServiceServer(grpcServer, &server{})

    // Listen for incoming gRPC requests on port 50051
    go func() {
        lis, err := net.Listen("tcp", ":50051")
        if err != nil {
            log.Fatalf("Failed to listen: %v", err)
        }
        log.Println("gRPC server listening on port 50051")
        if err := grpcServer.Serve(lis); err != nil {
            log.Fatalf("Failed to serve gRPC: %v", err)
        }
    }()

    // Set up the Gin HTTP server
    r := gin.Default()

    // Define a route to call the gRPC service
    r.GET("/matrix", apiHandler)

    // Start the Gin server
    log.Println("HTTP server listening on port 8080")
    r.Run(":8080")
}
