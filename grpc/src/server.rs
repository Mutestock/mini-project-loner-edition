use student::student_server::{Student, StudentServer};
use student::{CreateStudentRequest, CreateStudentResponse, ReadStudentResponse};
use tonic::{transport::Server, Request, Response, Status};

#[macro_use]
extern crate lazy_static;

mod connection;
mod entities;
mod logic;
mod utils;

use entities::student;

use logic::student_handler;
use utils::config::{is_containerized_development_mode, is_production_mode, CONFIG};

//pub mod student {
//    tonic::include_proto!("student");
//}

#[derive(Default)]
pub struct StudentCon {}

#[tonic::async_trait]
impl Student for StudentCon {
    async fn create_student(
        &self,
        request: Request<CreateStudentRequest>,
    ) -> Result<Response<CreateStudentResponse>, Status> {
        println!("Got a request from {:?}", request.remote_addr());
        
        Ok(Response::new(
            student_handler::create(request.into_inner())
                .await
                .expect("Student Creation failed"),
        ))
    }

    async fn read_student(
        &self,
        request: tonic::Request<student::ReadStudentRequest>,
    ) -> Result<tonic::Response<student::ReadStudentResponse>, tonic::Status> {
        println!("Got a request from {:?}", request.remote_addr());

        let reply = ReadStudentResponse {
            firstname: "stuff".to_owned(),
            lastname: "thing".to_owned(),
            phone_number: "phone".to_owned(),
            email: "email".to_owned(),
        };
        Ok(Response::new(reply))
    }

    async fn update_student(
        &self,
        request: tonic::Request<student::UpdateStudentRequest>,
    ) -> Result<tonic::Response<student::UpdateStudentResponse>, tonic::Status> {
        println!("Got a request from {:?}", request.remote_addr());
        let reply = student::UpdateStudentResponse {
            message: "Update student placeholder".to_owned(),
        };
        Ok(Response::new(reply))
    }

    async fn delete_student(
        &self,
        request: tonic::Request<student::DeleteStudentRequest>,
    ) -> Result<tonic::Response<student::DeleteStudentResponse>, tonic::Status> {
        println!("Got a request from {:?}", request.remote_addr());
        let reply = student::DeleteStudentResponse {
            message: "Update student placeholder".to_owned(),
        };
        Ok(Response::new(reply))
    }

    async fn read_student_list(
        &self,
        request: tonic::Request<student::ReadStudentListRequest>,
    ) -> Result<tonic::Response<student::ReadStudentListResponse>, tonic::Status> {
        println!("Got a request from {:?}", request.remote_addr());
        let student_response = ReadStudentResponse {
            firstname: "stuff".to_owned(),
            lastname: "thing".to_owned(),
            phone_number: "phone".to_owned(),
            email: "email".to_owned(),
        };

        let reply = student::ReadStudentListResponse {
            student_list: vec![student_response],
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
