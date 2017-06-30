
FROM library/alpine:latest


# Install Flask app dependencies.
RUN apk add --no-cache nginx
RUN mkdir www /run/nginx
ADD etc/nginx.conf /etc/nginx/nginx.conf
ADD html/index.html /html/index.html

EXPOSE 8080

CMD ["/usr/sbin/nginx"]
