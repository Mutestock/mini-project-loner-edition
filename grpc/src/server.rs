use tonic::{transport::Server, Request, Response, Status};

use student::student_constructor_server::{StudentConstructor, StudentConstructorServer};
use student::{CreationResponse, Student};

#[macro_use]
extern crate lazy_static;

mod utils;
mod connection;
mod logic;

use utils::config::{is_production_mode, CONFIG};

pub mod student {
    tonic::include_proto!("student");
}

#[derive(Default)]
pub struct StudentCon {}

#[tonic::async_trait]
impl StudentConstructor for StudentCon {
    async fn create_student(
        &self,
        request: Request<Student>,
    ) -> Result<Response<CreationResponse>, Status> {
        println!("Got a request from {:?}", request.remote_addr());

        let reply = student::CreationResponse {
            message: format!("Hello {}!", request.into_inner().firstname),
        };
        Ok(Response::new(reply))
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    //let mut addr = "[::1]:50051".parse().unwrap();

    let addr = match is_production_mode() {
        true => {
            let formatted_addr_string: &str = &format!("[::1]:{}", CONFIG.production.server.port);
            let stuff = formatted_addr_string.parse().expect("Shit ain't working");
            stuff
        }
        false => {
            let formatted_addr_string: &str = &format!("[::1]:{}", CONFIG.development.server.port);
            println!("{}", formatted_addr_string);
            let stuff = formatted_addr_string.parse().expect("Shit ain't working");
            stuff
        }
    };

    let student_constructor = StudentCon::default();

    println!("gRPC server listening on {}", addr);

    Server::builder()
        .add_service(StudentConstructorServer::new(student_constructor))
        .serve(addr)
        .await?;

    Ok(())
}
