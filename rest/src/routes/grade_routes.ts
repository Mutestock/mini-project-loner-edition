import {oak} from "../../deps.ts";
import {create, read, update, _delete, readList, head} from "../logic/grade_handler.ts"

const routePrefix = "/grade"

function gradeRoutes(router: oak.Router): oak.Router { 
    router
        .get(routePrefix, async (context) => {
            context.response.body = await (await readList()).rows;
        })
        .get<{id: string}>(routePrefix+"/:id", async (context) => {
            context.response.body = await (await read(context.params.id)).rows;
        })
        .post(routePrefix, async (context: oak.RouterContext) => {
            await create(context);
            context.response.body = "201"
        })
        .put<{id: string}>(routePrefix+"/:id", async (context: oak.RouterContext<{id: string}, Record<string, any>>) => {
            await update(context);
            context.response.body ="204";
        })
        .delete<{id: string}>(routePrefix+"/:id", async (context) => {
            await _delete(context.params.id)
            context.response.body ="200"
        })
        .head(routePrefix, (context) => {
            context.response.body =head()
        })
    return router;  
}


export {
    gradeRoutes,
}