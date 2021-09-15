import { Student, NewStudent, StudentResponse } from "../entities/student.ts";
import { runQuery } from "../connection/pg_connection.ts"
import {oak} from "../../deps.ts"

async function insertObject(newObject: Object, tableName: string) {

    const objectKeys = Object.keys(newObject);
    const objectEntries = Object.entries(newObject);

    let query = `INSERT INTO ${tableName}(`
    for (const key of objectKeys) {
        if (objectKeys.indexOf(key) !== objectKeys.length - 1) {
            query += `${key},`
        }
        else {
            query += `${key}`
        }
    }
    query += ") VALUES("
    for (const [key, value] of objectEntries) {
        if (objectKeys.indexOf(key) !== objectKeys.length - 1) {
            query += `${value},`
        }
        else {
            query += `${value}`
        }
    }
    await runQuery(query);
}

function bodyGuard(context: oak.RouterContext){
    if (!context.request.hasBody){
        context.throw(oak.Status.BadRequest, "Bad Request");
    }
    if (context.request.body().type !== "json"){
        context.throw(oak.Status.BadRequest, "Bad Request");
    }
}



export{
    insertObject, bodyGuard
}