# Frontend Dockerfile
FROM node:16-alpine

# Set working directory
WORKDIR /app

# Install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy application code
COPY . .

# Expose Vue dev server port
EXPOSE 5173

# Run Vue development server
CMD ["npm", "run", "dev"]