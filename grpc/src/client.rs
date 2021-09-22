// Irrelevant in this project

#[macro_use]
extern crate lazy_static;

use student::student_client::StudentClient;
use student::{CreateStudentRequest, ReadStudentListRequest};

mod utils;

use utils::config::{is_production_mode, CONFIG};

pub mod student {
    tonic::include_proto!("student");
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut client = match is_production_mode() {
        true => {
            StudentClient::connect(format!(
                "http://[::1]:{}",
                CONFIG.production.server.port
            ))
            .await?
        }
        false => {
            StudentClient::connect(format!(
                "http://[::1]:{}",
                CONFIG.development.server.port
            ))
            .await?
        }
    };

    let request = tonic::Request::new(ReadStudentListRequest {
    });

    let response = client.read_student_list(request).await?;

    println!("RESPONSE={:?}", response);

    Ok(())
}
