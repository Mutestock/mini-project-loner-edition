import {config} from "../utils/config.ts";
import {runQuery} from "../connection/pg_connection.ts";

async function up(path: string) {
    const sql = await Deno.readTextFile(config.misc.migrations_directory+`/${path}/up.sql`);
    runQuery(sql);
}

async function down(path: string) {
    const sql = await Deno.readTextFile(config.misc.migrations_directory+`/${path}/down.sql`);
    runQuery(sql);
}

export {
    up, down
}


