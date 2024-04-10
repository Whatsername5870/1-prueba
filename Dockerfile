FROM python:3.11

ENV MONGODB_USER='root'
ENV MONGODB_PASSWORD='rootpassword'

ENV POSTGRES_USER='postgres'
ENV POSTGRES_PASSWORD='postgres'
ENV POSTGRES_DB='postgres'

ENV REDIS_USER='redis'
ENV REDIS_PASSWORD='redis'

# Set the working directory
WORKDIR /opt/app

COPY . .

# Install Poetry
RUN pip install poetry
# Install dependencies
RUN poetry install

# Expose the port
EXPOSE 5000

# Run the application
CMD ["poetry", "run", "python3", "-m", "flask", "run", "--host=0.0.0.0"]