FROM debian:latest
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --no-install-recommends -y curl dirmngr gnupg apt-transport-https ca-certificates nodejs npm

# App
ADD . /web
WORKDIR /web
# Install app dependencies
RUN npm install
RUN npm install supervisor body-parser

EXPOSE  8080
ENTRYPOINT ["nodejs", "./index.js"]
