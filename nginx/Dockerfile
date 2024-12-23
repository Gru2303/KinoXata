# Use the official Nginx image from Docker Hub
FROM nginx:alpine

# Remove the default nginx configuration
RUN rm /etc/nginx/conf.d/default.conf

# Copy the custom Nginx configuration file to the container
COPY default.conf /etc/nginx/conf.d/

# Copy the built frontend files into the Nginx container
COPY ../frontend/dist /usr/share/nginx/html

# Expose port 80 for Nginx
EXPOSE 80

# Start Nginx when the container runs
CMD ["nginx", "-g", "daemon off;"]