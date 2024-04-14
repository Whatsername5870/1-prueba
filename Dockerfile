FROM python:3.11

ENV MONGODB_USER='root'
ENV MONGODB_PASSWORD='rootpassword'

ENV POSTGRES_DB_USER='postgres'
ENV POSTGRES_DB_PASSWORD='postgres'
ENV POSTGRES_DB_NAME='postgres'
ENV POSTGRES_DB_HOST='localhost'
ENV POSTGRES_DB_PORT=5432

ENV REDIS_USER='redis'
ENV REDIS_PASSWORD='redis'

# Set the working directory
WORKDIR /opt/app

COPY . .

# Install Poetry
RUN pip install poetry
# Install dependencies
RUN poetry install

# Create a volume
VOLUME /data_store

# Expose the port
EXPOSE 5000

# Run the application
CMD ["poetry", "run", "python3", "-m", "flask", "run", "--host=0.0.0.0"]