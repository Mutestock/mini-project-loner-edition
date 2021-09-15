import {oak} from "../../deps.ts";
import {Student} from "../entities/student.ts";

const routePrefix = "/student"

function studentRoutes(router: oak.Router): oak.Router { 
    router
        .get(routePrefix, (context) => {
            context.response.body = "Hello World";
        }) 
    return router;
}


export {
    studentRoutes,
}