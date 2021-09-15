
import { Student, NewStudent, StudentResponse } from "../entities/student.ts";
import { insertObject } from "./handler_utils.ts";
import {oak} from "../../deps.ts";


async function create(context: oak.RouterContext) {
    let body = context.request.body();
    let newStudent = await body.value;
    newStudent = newStudent as NewStudent;
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

