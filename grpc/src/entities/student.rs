tonic::include_proto!("student");

use serde_derive::{Deserialize, Serialize};

// Sqlx => Tonic
#[derive(Serialize, Deserialize, sqlx::FromRow)]
pub struct StudentConverter {
    id: i32,
    first_name: String,
    last_name: String,
    phone_number: String,
    email: String,
}

impl StudentConverter {
    pub fn to_read_response(&self) -> ReadStudentResponse {
        ReadStudentResponse {
            first_name: self.first_name.clone(),
            last_name: self.last_name.clone(),
            phone_number: self.phone_number.clone(),
            email: self.email.clone(),
        }
    }
    pub fn to_list_response(stud_vec: Vec<StudentConverter>) -> ReadStudentListResponse{
        let mut read_list: Vec<ReadStudentResponse> = vec![];
        for student in stud_vec{
            read_list.push(student.to_read_response())
        };
        ReadStudentListResponse{
            student_list: read_list,
        }
    } 
}



