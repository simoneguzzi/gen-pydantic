# Pydantic

## Run locally

1. Install requirements:

   ```shell
   pip install -r requirements.txt
   ```

2. Run the application:

   ```shell
   fastapi dev main.py
   ```

Getting Started Locally with Dockerized Container 
=================================================
Prerequisite
--------
- Docker
  
Pull the repository
-------------------
```
git clone https://github.com/iamkashifyousuf/gen-pydantic.git
cd gen-pydantic
```
Building Image
--------------
```
docker build -t gen-pydantic:latest .
```
Run the Docker Container with Compose File
----------------------------------------------------
```
docker compose up
```
Access the Web-App
------------------
The app is accessable on localhost:8001
