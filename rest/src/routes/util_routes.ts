import {oak} from "../../deps.ts";


// No route prefix for basics
// Root route acts as a health check


function basic_routes(router: oak.Router): oak.Router{
    router
        .get("/", (context) => {
            context.response.body = "Ok"
        })
    return router;
}

export {
    basic_routes,
}