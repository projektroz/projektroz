FROM node:alpine

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

RUN npm install react-router-dom history sass
RUN npm run build

RUN npm install styled-components
RUN npm install @mantine/core

EXPOSE 3000 3010

CMD ["npm", "run", "dev"]
