
import { Student, NewStudent, StudentResponse } from "../entities/student.ts";
import { queryInsertObject, queryBodyGuard, queryReadObject, queryDeleteObject, queryUpdateObject, queryReadObjectList } from "./shared_behaviour.ts";
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
async function read(id: string) {
    return await queryReadObject("students", id)
}

// Expected input = id, newStudent
async function update(context: oak.RouterContext<{id: string}, Record<string, any>>) {
    queryBodyGuard(context);
    let id = "";
    if (context.params.id){
        id = context.params.id
    }

    const updateStudent = await context
        .request
        .body()
        .value as NewStudent
    await queryUpdateObject(updateStudent, "students", id);
}

// Expected input = id
async function _delete(id: string) {
    await queryDeleteObject("students",id);
}

// Expected input = None
async function readList() {
    return await queryReadObjectList("students")
}

export {
    create, read, update, _delete, readList
}
