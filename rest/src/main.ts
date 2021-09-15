import { oak, colors } from "../deps.ts";
import { router } from "./routes/router.ts";
import {config} from "./utils/config.ts";



let app = new oak.Application();
app.use(router.routes());
app.use(router.allowedMethods());

app.addEventListener("listen", ({ hostname, port, serverType }) => {
    console.log(
        colors.bold("Start listening on ") + colors.yellow(`${hostname}:${port}`),
    );
    console.log(colors.bold("  using HTTP server: " + colors.yellow(serverType)));
});

await app.listen({hostname: config.server.hostname, port: config.server.port});


