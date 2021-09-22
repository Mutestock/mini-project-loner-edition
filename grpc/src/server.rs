use student::student_server::{Student, StudentServer};
use student::{CreationResponse, NewStudentObject, StudentReply};
use tonic::{transport::Server, Request, Response, Status};

#[macro_use]
extern crate lazy_static;

mod connection;
mod logic;
mod utils;

use utils::config::{is_containerized_development_mode, is_production_mode, CONFIG};

pub mod student {
    tonic::include_proto!("student");
}

#[derive(Default)]
pub struct StudentCon {}

#[tonic::async_trait]
impl Student for StudentCon {
    async fn create_student(
        &self,
        request: Request<NewStudentObject>,
    ) -> Result<Response<CreationResponse>, Status> {
        println!("Got a request from {:?}", request.remote_addr());

        let reply = student::CreationResponse {
            message: format!("Hello {}!", request.into_inner().firstname),
        };
        Ok(Response::new(reply))
    }

    async fn read_student(
        &self,
        request: tonic::Request<student::Id>,
    ) -> Result<tonic::Response<student::StudentReply>, tonic::Status> {
        println!("Got a request from {:?}", request.remote_addr());

        //let reply = student::StudentReply {
        //    message: format!("Hello {}!", request.into_inner().firstname),
        //};

        let reply = StudentReply {
            firstname: "stuff".to_owned(),
            lastname: "thing".to_owned(),
            phone_number: "phone".to_owned(),
            email: "email".to_owned(),
        };
        Ok(Response::new(reply))
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let addr = match is_production_mode() {
        true => {
            let formatted_addr_string: &str = &format!(
                "{}:{}",
                CONFIG.production.server.host, CONFIG.production.server.port
            );
            formatted_addr_string
                .parse()
                .expect("Tonic ain't working =|")
        }
        false => match is_containerized_development_mode() {
            true => {
                let formatted_addr_string: &str = &format!(
                    "{}:{}",
                    CONFIG.containerized.server.host, CONFIG.containerized.server.port
                );
                formatted_addr_string
                    .parse()
                    .expect("Tonic ain't working =|")
            }
            false => {
                let formatted_addr_string: &str = &format!(
                    "{}:{}",
                    CONFIG.development.server.host, CONFIG.development.server.port
                );
                formatted_addr_string
                    .parse()
                    .expect("Tonic ain't working =|")
            }
        },
    };

    let student_ = StudentCon::default();

    println!("gRPC server listening on {}", addr);

    Server::builder()
        .add_service(StudentServer::new(student_))
        .serve(addr)
        .await?;

    Ok(())
}
