import {oak} from "../../deps.ts";
import {Student} from "../entities/student.ts";
import {create} from "../logic/student_handler.ts"

const routePrefix = "/student"

function studentRoutes(router: oak.Router): oak.Router { 
    router
        .get(routePrefix, (context) => {
            context.response.body = "Read list placeholder";
        })
        .get<{id: string}>(routePrefix+"/:id", (context) => {
            context.response.body = "Read placeholder";
        })
        .post(routePrefix, async (context: oak.RouterContext) => {
            await create(context);
        })
        .put(routePrefix, (context) => {
            context.response.body = "Read list placeholder";
        })
        .delete(routePrefix, (context) => {
            context.response.body = "Read list placeholder";
        })
    return router;
}


export {
    studentRoutes,
}