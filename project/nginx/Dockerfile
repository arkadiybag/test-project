FROM nginx:stable
COPY nginx.conf /etc/nginx/nginx.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
WORKDIR /etc/nginx
EXPOSE 80
CMD service nginx start
