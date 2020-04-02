FROM nginx:latest
WORKDIR /ect/nginx/
RUN rm ./conf.d/default.conf
COPY ./reverse_proxy.conf ./conf.d/