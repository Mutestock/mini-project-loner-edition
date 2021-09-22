// Irrelevant in this project

#[macro_use]
extern crate lazy_static;

use student::student_client::StudentClient;
use student::{NewStudentObject,Id};

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

    //let request = tonic::Request::new(NewStudentObject {
    //    firstname: "John".to_owned(),
    //    lastname: "Doe".to_owned(),
    //    phone_number: "+45 12 12 12 12".to_owned(),
    //    email: "herp@derp.com".to_owned(),
    //});

    let request = tonic::Request::new(Id {
        id:19
    });

    let response = client.read_student(request).await?;

    println!("RESPONSE={:?}", response);

    Ok(())
}
