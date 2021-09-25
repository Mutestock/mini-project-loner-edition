FROM node:14-alpine AS build

WORKDIR /app
COPY ./src/package.json ./src/package-lock.json ./
RUN npm ci
COPY ./src .
RUN npm run build

FROM nginx:1.21-alpine
COPY nginx.conf /etc/nginx/nginx.conf
COPY --from=build /app/dist/frontend /usr/share/nginx/html
