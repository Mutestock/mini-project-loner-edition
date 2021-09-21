#[macro_use]
extern crate lazy_static;

use student::student_constructor_client::StudentConstructorClient;
use student::Student;

mod utils;

use utils::config::{CONFIG,is_production_mode};

pub mod student {
    tonic::include_proto!("student");
}


#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {

    let mut client = StudentConstructorClient::connect("http://[::1]:50051").await?;
    match is_production_mode(){
        true => client = StudentConstructorClient::connect(format!("http://[::1]:{}", CONFIG.production.server.port)).await?,
        false => client = StudentConstructorClient::connect(format!("http://[::1]:{}", CONFIG.development.server.port)).await?,
    }


    let request = tonic::Request::new(Student {
        firstname:  "John".to_owned(),
        lastname: "Doe".to_owned(),
        id: 0,
        phone_number: "+45 12 12 12 12".to_owned(),
        email: "herp@derp.com".to_owned(),
    });

    let response = client.create_student(request).await?;

    println!("RESPONSE={:?}", response);

    Ok(())
}
