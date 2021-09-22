// For manual testing in this project

#[macro_use]
extern crate lazy_static;

mod entities;
mod utils;

use entities::student::student_client::StudentClient;
use entities::student::{CreateStudentRequest, ReadStudentListRequest};
use tonic::transport::Channel;
use utils::config::{is_production_mode, CONFIG};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut client = match is_production_mode() {
        true => {
            StudentClient::connect(format!("http://[::1]:{}", CONFIG.production.server.port))
                .await?
        }
        false => {
            StudentClient::connect(format!("http://[::1]:{}", 13000))
                .await?
        }
    };

    //let request = tonic::Request::new(ReadStudentListRequest {});
//
    //let response = client.read_student_list(request).await?;
//
    //println!("RESPONSE={:?}", response);
    //create_student(client).await;
    let request = tonic::Request::new(CreateStudentRequest {
        first_name: "firstnamefromtonic".to_owned(),
        last_name: "lastnamefromtonic".to_owned(),
        phone_number: "phonenumberfromtonic".to_owned(),
        email: "emailfromtonic".to_owned(),
    });

    let response = client
        .create_student(request)
        .await
        .expect("create_student failed in client");
    println!("RESPONSE={:?}", response);

    Ok(())
}

async fn create_student(mut client: StudentClient<Channel>) {
    let request = tonic::Request::new(CreateStudentRequest {
        first_name: "first_name_from_tonic".to_owned(),
        last_name: "last_name_from_tonic".to_owned(),
        phone_number: "phone_number_from_tonic".to_owned(),
        email: "email_from_tonic".to_owned(),
    });

    let response = client
        .create_student(request)
        .await
        .expect("create_student failed in client");
    println!("RESPONSE={:?}", response);
}
