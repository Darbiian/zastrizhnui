FROM nginx:1.25-alpine

# Create necessary directories with proper permissions
RUN mkdir -p /var/run/nginx && \
    chmod 755 /var/run/nginx && \
    mkdir -p /var/log/nginx && \
    chmod 755 /var/log/nginx && \
    mkdir -p /usr/share/nginx/html && \
    chmod 755 /usr/share/nginx/html

# Remove default configuration
RUN rm -f /etc/nginx/conf.d/default.conf

# Copy custom configuration files
COPY nginx.conf /etc/nginx/nginx.conf
COPY app.conf /etc/nginx/conf.d/app.conf

# Copy error pages
COPY error_pages/404.html /usr/share/nginx/html/404.html
COPY error_pages/50x.html /usr/share/nginx/html/50x.html

# Expose ports
EXPOSE 80 443

# Use default nginx entrypoint
CMD ["nginx", "-g", "daemon off;"] 