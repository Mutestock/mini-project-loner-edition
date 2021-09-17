import {oak} from "../../deps.ts"
import {studentRoutes} from "./student_routes.ts";
import {basicRoutes} from "./util_routes.ts";


// Contains configurations for all routes

let router = new oak.Router();
router = studentRoutes(router);
router = basicRoutes(router);


export {
    router
}