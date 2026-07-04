# Use an official Node.js image
FROM node:22

# Working directory inside the container
WORKDIR /app

# Copy dependency files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the frontend
COPY . .

# Vite development server port
EXPOSE 5173

# Start Vite and allow external connections
CMD ["npm", "run", "dev", "--", "--host"]