use tonic::{transport::Server, Request, Response, Status};

use student::student_server::{StudentConstructor, StudentServer};
use student::{Student, CreationResponse};

pub mod student {
    tonic::include_proto!("student");
}

#[derive(Default)]
pub struct StudentCon {}

#[tonic::async_trait]
impl StudentConstructor for StudentCon {
    async fn say_hello(
        &self,
        request: Request<Student>,
    ) -> Result<Response<CreationResponse>, Status> {
        println!("Got a request from {:?}", request.remote_addr());

        let reply = student::CreationResponse {
            message: format!("Hello {}!", request.into_inner().name),
        };
        Ok(Response::new(reply))
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let addr = "[::1]:50051".parse().unwrap();
    let greeter = StudentCon::default();

    println!("GreeterServer listening on {}", addr);

    Server::builder()
        .add_service(StudentServer::new(greeter))
        .serve(addr)
        .await?;

    Ok(())
}
