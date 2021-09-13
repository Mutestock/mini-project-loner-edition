import {asserts} from "../deps.ts"
import {config} from "../src/utils/config.ts";


Deno.test('Test file works', () => {
    asserts.assert(2===2);
});

Deno.test('Config file works',() => {
    asserts.assert(typeof config.database.pg_port ==="number");
    asserts.assert(typeof config.database.pg_user ==="string");
    asserts.assert(config.database !== undefined);
});






