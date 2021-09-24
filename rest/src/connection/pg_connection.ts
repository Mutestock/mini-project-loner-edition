import { config } from "../utils/config.ts";
import { postgres } from "../../deps.ts";

// https://deno.land/x/postgres@v0.12.0

const dbParams = {
    user: config.database.pg_user,
    database: config.database.pg_db,
    hostname: config.database.pg_host,
    port: config.database.pg_port,
    password: config.database.pg_pass,
};

const pool = new postgres.Pool(dbParams, config.database.max_pool_connections, true);

async function runQuery(query: string, _pool: postgres.Pool = pool) {
    const client = await _pool.connect();
    let result: any;
    try {
        result = await client.queryObject(query);
    } finally {
        client.release();
    }
    return result;
}

export {
    runQuery
}
