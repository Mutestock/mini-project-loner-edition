#![allow(dead_code, unused_imports)]

use crate::connection::pg_connection::get_pg_pool;

pub mod student {
    tonic::include_proto!("student");
}

pub fn create(create_student_request: student::CreateStudentRequest) -> student::CreateStudentResponse{
    todo!();
}

pub fn read(read_student_request: student::ReadStudentRequest) -> student::ReadStudentResponse{
    todo!();    
}

pub fn update(update_student_request: student::UpdateStudentRequest) -> student::UpdateStudentResponse{
    todo!();
}

pub fn delete(delete_student_request: student::DeleteStudentRequest) -> student::DeleteStudentResponse{
    todo!();
}

pub fn read_list(_read_student_list_request: student::ReadStudentListRequest) -> student::ReadStudentListResponse{
    todo!();
}

