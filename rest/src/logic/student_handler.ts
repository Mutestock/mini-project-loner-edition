
import { Student, NewStudent, StudentResponse } from "../entities/student.ts";
import { insertObject } from "./handler_utils.ts";


async function create(newStudent: NewStudent) {
    await insertObject(newStudent, "students");
}


async function read() {

}

async function update() {

}

async function _delete() {

}

async function readList() {

}

export {
    create, read, update, _delete, readList
}

