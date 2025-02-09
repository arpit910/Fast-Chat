# FastAPI Chat App

FastAPI Chat App is a real-time chatting application using FastAPI, WebSockets, and MongoDB with a user-friendly UI.

## Tech Stack

**Client:** HTML, CSS, JavaScript  
**Server:** FastAPI, WebSockets  
**Database:** MongoDB  


## Run Locally

### Clone the project
```bash
git clone https://github.com/arpit910/fastapi-chat-app.git
```

### Go to the project directory
```bash
cd fastapi-chat-app
```

### Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Set Up Environment Variables
Create a `.env` file and add the following:
```bash
MONGO_URI=mongodb://localhost:27017/chatdb
SECRET_KEY=your_secret_key
```

### Run the Application
```bash
uvicorn main:app --reload
```

### Access the App
Open [`http://127.0.0.1:8000`](http://127.0.0.1:8000) in your browser.

## Features

### User Authentication
![](#) *(Add image link here)*

### Real-Time Chatting with WebSockets
![](#)

### One-to-One and Group Chats
![](#)

### Message Persistence
![](#)

### User Search and Profile View
![](#)

## Deployment

### Using Docker
```bash
docker build -t fastapi-chat-app .
docker run -p 8000:8000 fastapi-chat-app
```

### Deploy on Cloud (e.g., Heroku, AWS, Railway)
- Use **MongoDB Atlas** for cloud database.
- Deploy using **Gunicorn** and **Uvicorn**.

## Contributing

1. Fork the repo and create a new branch.
2. Make changes and submit a pull request.

## License

This project is licensed under the **MIT License**.

## Made By

- [@Arpit910](https://github.com/arpit910) 

