FROM node:alpine

WORKDIR /app

COPY package*.json .

RUN npm install

COPY . .

EXPOSE 3000

# CMD ["npm", "run", "build"]

# Change CMD to start the development server
CMD ["npm", "start"]
