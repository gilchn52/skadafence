FROM nginx:1.22-alpine

COPY index.html /usr/share/nginx/html
COPY changeme.sh /home
RUN /home/changeme.sh
RUN     chown -R nginx:nginx /var/cache/nginx && \
        chown -R nginx:nginx /var/log/nginx && \
        chown -R nginx:nginx /etc/nginx/conf.d
RUN touch /var/run/nginx.pid && \
        chown -R nginx:nginx /var/run/nginx.pid

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
EXPOSE 8080
USER nginx

CMD ["nginx", "-c", "/etc/nginx/nginx.conf"]









