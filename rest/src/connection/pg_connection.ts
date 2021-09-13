import { config } from "../utils/config.ts";
import { postgres } from "../../deps.ts";

// https://deno.land/x/postgres@v0.12.0

const client = new postgres.Client({
    user: config.database.pg_user,
    database: config.database.pg_db,
    hostname: config.database.pg_host,
    port: config.database.pg_port,
    password: config.database.pg_pass,
});

export {
    client
}

