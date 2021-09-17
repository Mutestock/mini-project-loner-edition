
import { Student, NewStudent, StudentResponse } from "../entities/student.ts";
import { queryInsertObject, queryBodyGuard } from "./shared_behaviour.ts";
import { oak } from "../../deps.ts";


// Expected input = newStudent
async function create(context: oak.RouterContext) {
    queryBodyGuard(context);
    const newStudent = await context
        .request
        .body()
        .value as NewStudent;
    await queryInsertObject(newStudent, "students");
}

// Expected input = id
async function read(context: oak.RouterContext) {
    await queryBodyGuard(context);
}

// Expected input = id, newStudent
async function update(context: oak.RouterContext) {
    await queryBodyGuard(context);
}

// Expected input = id
async function _delete() {

}

// Expected input = None
async function readList() {

}

export {
    create, read, update, _delete, readList
}

