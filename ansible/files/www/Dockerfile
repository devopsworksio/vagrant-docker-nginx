
FROM nginx:alpine


# Install Flask app dependencies.apl
ADD html/index.html /usr/share/nginx/html/index.html
EXPOSE 80
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]
