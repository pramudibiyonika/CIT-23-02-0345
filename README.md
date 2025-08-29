#  Task Manager App – Assignment 1
##  Application Description
This project is a **Task Manager Web Application** built using **Flask** (Python) and **MySQL**.  
It allows users to  
- Add new tasks  
- Mark tasks as done  
- Delete tasks  
- Persist tasks even after container restarts (using Docker volumes)
  
  ---


##  Deployment Requirements
To deploy this application, ensure you have the following installed:  
- **Linux environment** (Ubuntu recommended)  
- **Docker** (version 20+ recommended)  
- **Docker Compose** plugin (newer `docker compose` command)  
- **Git** (to clone and submit the project)

  ---

##  Network and Volume Details
- **Network-** `app-network` (created for communication between containers)  
- **Volume-** `db-data` (attached to MySQL container for persistent storage of tasks)
  --- 

##  Container Configuration
### 1. **Web Container (Flask App)**
- **Image:** Built from `./app/Dockerfile`  
- **Port:** 5000 (exposed as `http://localhost:5000`)  
- **Depends on:** `db` container (MySQL)  

### 2. **Database Container (MySQL)**
- **Image:** `mysql:5.7`  
- **Port:** 3306 (internal, not exposed to host)  
- **Environment variables:**  
  - `MYSQL_ROOT_PASSWORD=rootpassword`  
  - `MYSQL_DATABASE=taskdb`  
- **Volume:** `db-data:/var/lib/mysql`
  ---

##  Container List
| Container | Role             | Port |
|-----------|------------------|------|
| `web`     | Flask Task Manager (frontend) | 5000 |
| `db`      | MySQL Database (persistent)   | 3306 |

---


##  Instructions

###  1. Prepare Application
```bash
./prepare-app.sh
```
-Creates network (app-network)
-Creates volume (db-data)
-Builds Flask web app image
---

### 2. Start Application
```bash
./start-app.sh
```
-Starts all containers in detached mode
-Flask app available at:  (http://localhost:5000)
---

### 3. Stop Application
```bash
./stop-app.sh
```
-Stops all containers
-Persistent data in MySQL remains saved








