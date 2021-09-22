use sqlx::postgres::PgPool;

use crate::utils::config::{is_production_mode, CONFIG};

lazy_static! {
    static ref DATABASE_URL: String = {
        match is_production_mode() {
            true => format!(
                "postgres://{}:{}@{}:{}/{}",
                CONFIG.production.database.pg_user,
                CONFIG.production.database.pg_pass,
                CONFIG.production.database.pg_host,
                CONFIG.production.database.pg_port,
                CONFIG.production.database.pg_db,
            ),
            false => format!(
                "postgres://{}:{}@{}:{}/{}",
                CONFIG.development.database.pg_user,
                CONFIG.development.database.pg_pass,
                CONFIG.development.database.pg_host,
                CONFIG.development.database.pg_port,
                CONFIG.development.database.pg_db,
            ),
        }
    };
}

pub async fn get_pg_pool() -> anyhow::Result<PgPool> {
    Ok(PgPool::connect(&DATABASE_URL).await?)
}
