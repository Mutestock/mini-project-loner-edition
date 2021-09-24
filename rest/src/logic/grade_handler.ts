
import { NewGrade } from "../entities/grade.ts";
import { queryInsertObject, queryBodyGuard, queryReadObject, queryDeleteObject, queryUpdateObject, queryReadObjectList } from "./shared_behaviour.ts";
import { oak } from "../../deps.ts";


// Expected input = newGrade
async function create(context: oak.RouterContext) {
    queryBodyGuard(context);
    const newGrade = await context
        .request
        .body()
        .value as NewGrade;
    await queryInsertObject(newGrade, "grades");
}

// Expected input = id
async function read(id: string) {
    return await queryReadObject("grades", id)
}

// Expected input = id, newGrade
async function update(context: oak.RouterContext<{id: string}, Record<string, any>>) {
    //console.log(await context.request.body);
    queryBodyGuard(context);
    let id = "";
    if (context.params.id){
        id = context.params.id
    }
    

    const updateGrade = await context
        .request
        .body()
        .value as NewGrade
    await queryUpdateObject(updateGrade, "grades", id);
}

// Expected input = id
async function _delete(id: string) {
    await queryDeleteObject("grades",id);
}

// Expected input = None
async function readList() {
    return await queryReadObjectList("grades")
}

export {
    create, read, update, _delete, readList
}
