FROM node:12.7-alpine as reactbuild

WORKDIR /app

COPY package*.json /app/
RUN npm install
COPY . /app/
RUN npm run build

From nginx
COPY --from=reactbuild /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
