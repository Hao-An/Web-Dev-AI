# Web-Dev-AI
This project contains **Plenty Plants**, a simple knowledge sharing platform for plant enthusiasts.

### Running with Docker

1. Build the image:
   ```bash
   docker build -t plentyplants .
   ```
2. Run the container (requires a PostgreSQL database):
   ```bash
   docker run -e POSTGRES_HOST=<db_host> -e POSTGRES_DB=<db_name> \
      -e POSTGRES_USER=<user> -e POSTGRES_PASSWORD=<password> \
      -p 8000:8000 plentyplants
   ```
