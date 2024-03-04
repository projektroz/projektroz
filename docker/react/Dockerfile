FROM node:14

WORKDIR /app

COPY package*.json ./

RUN npm install
COPY . .
RUN npm run build

FROM ngnix:alpine

COPY --from=0 /app/build /usr/share/ngnix/html
EXPOSE 80

CMD ["ngnix", "-g", "daemon off;"]