import {oak} from "../../deps.ts"
import {gradeRoutes} from "./grade_routes.ts";
import {basicRoutes} from "./util_routes.ts";
import {homeRoutes} from "./home_routes.ts";


// Contains configurations for all routes

let router = new oak.Router();
router = gradeRoutes(router);
router = basicRoutes(router);
router = homeRoutes(router);


export {
    router
}