#![allow(dead_code, unused_imports)]

use crate::connection::pg_connection::get_pg_pool;
use crate::entities::student;

pub async fn create(
    create_student_request: student::CreateStudentRequest,
) -> anyhow::Result<student::CreateStudentResponse> {
    sqlx::query(
        r#"
        INSERT INTO students (first_name, last_name, phone_number, email)
        VALUES( $1, $2, $3, $4 )
        "#,
    )
    .bind(create_student_request.first_name)
    .bind(create_student_request.last_name)
    .bind(create_student_request.phone_number)
    .bind(create_student_request.email)
    .execute(
        &get_pg_pool()
            .await
            .expect("Create student connection issues"),
    )
    .await
    .expect("Could not create student");

    Ok(student::CreateStudentResponse {
        message: "201".to_owned(),
    })
}

pub async fn read(
    read_student_request: student::ReadStudentRequest,
) -> student::ReadStudentResponse {
    todo!();
}

pub async fn update(
    update_student_request: student::UpdateStudentRequest,
) -> student::UpdateStudentResponse {
    todo!();
}

pub async fn delete(
    delete_student_request: student::DeleteStudentRequest,
) -> student::DeleteStudentResponse {
    todo!();
}

pub async fn read_list(
    _read_student_list_request: student::ReadStudentListRequest,
) -> student::ReadStudentListResponse {
    todo!();
}
