import {oak} from "../../deps.ts";
import {Student} from "../entities/student.ts";
import {create} from "../logic/student_handler.ts"

const routePrefix = "/student"

function studentRoutes(router: oak.Router): oak.Router { 
    router
        .get(routePrefix, (context) => {
            create();
            context.response.body = "Hello World";
        }) 
    return router;
}


export {
    studentRoutes,
}