
import { Student, NewStudent, StudentResponse } from "../entities/student.ts";
import { queryInsertObject, queryBodyGuard } from "./shared_behaviour.ts";
import { oak } from "../../deps.ts";


async function create(context: oak.RouterContext) {
    queryBodyGuard(context);
    const newStudent = await context.request.body().value as NewStudent;
    await queryInsertObject(newStudent, "students");
}


async function read() {

}

async function update(context: oak.RouterContext) {
    await queryBodyGuard(context);
}

async function _delete() {

}

async function readList() {

}

export {
    create, read, update, _delete, readList
}

