use student::student_client::StudentClient;
use student::Student;

pub mod student {
    tonic::include_proto!("student");
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut client = StudentClient::connect("http://[::1]:50051").await?;

    let request = tonic::Request::new(Student {
        name: "Tonic".into(),
    });

    let response = client.say_hello(request).await?;

    println!("RESPONSE={:?}", response);

    Ok(())
}
