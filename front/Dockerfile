
FROM node:16.14.2

WORKDIR /app
RUN npm install -g @vue/cli
ADD ./test-project/package.json /app/package.json
RUN npm install
ADD ./start.sh /app/start.sh
