import { toml, dotenv } from "../../deps.ts";


const env = dotenv.config();
// Run from root of program
const CONFIG_PATH = "./config.toml";
const CONFIG = await Deno.readTextFile(CONFIG_PATH);
let config: any;

try {
    if(env.production == "1"){
        config = toml.parse(CONFIG).production;
    }
    else{
        config = toml.parse(CONFIG).development;
    }
    
} catch (e) {
    console.error("Parsing error on line " + e.line + ", column " + e.column +
        ": " + e.message);
}


export {
    config,
}

