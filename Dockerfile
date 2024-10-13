# Use an official Python Alpine runtime as a parent image
FROM python:3.12-alpine

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apk add --no-cache \
    git \
    wget \
    build-base \
    libffi-dev \
    openssl-dev

# Install Poetry
RUN pip install poetry

# Copy the pyproject.toml and poetry.lock* files (if it exists)
COPY pyproject.toml poetry.lock* ./

# Install project dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy the rest of the application's code
COPY . .

# Install PyInstaller
RUN pip install pyinstaller

# Build the executable
RUN poetry run python build.py

# The executable will be in /app/package_installer.exe

# Set the default command to run when the container starts
CMD ["./package_installer.exe"]