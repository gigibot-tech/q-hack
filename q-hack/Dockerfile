FROM node:16-buster-slim as builder

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

FROM node:16-buster-slim

WORKDIR /app

RUN npm install -g serve

COPY --from=builder /app/dist /app/dist

EXPOSE 8080

CMD ["serve", "-s", "dist", "-l", "8080"]
