FROM node:alpine

WORKDIR /app

COPY package*.json .

RUN npm install

COPY . .

RUN npm install react-router-dom


#  Kompilacja aplikacji w trybie produkcyjnym
#  CMD ["npm", "run", "build"]

EXPOSE 3000

# Change CMD to start the development server
CMD ["npm", "start"]
