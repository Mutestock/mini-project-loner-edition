
import { Student, NewStudent, StudentResponse } from "../entities/student.ts";
import { insertObject, bodyGuard} from "./handler_utils.ts";
import {oak} from "../../deps.ts";


async function create(context: oak.RouterContext) {
    bodyGuard(context);
    const newStudent = await context.request.body().value as NewStudent;
    await insertObject(newStudent, "students");
}


async function read() {

}

async function update(context: oak.RouterContext) {
    bodyGuard(context);
}

async function _delete() {

}

async function readList() {

}

export {
    create, read, update, _delete, readList
}

