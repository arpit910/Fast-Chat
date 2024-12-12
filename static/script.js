let socket;
let username = "";

function connectWebSocket() {
    username = document.getElementById("username").value.trim();
    
    if (username === "") {
        alert("Please enter a username!");
        return;
    }

    socket = new WebSocket(`ws://127.0.0.1:8000/ws/${username}`);

    socket.onopen = function () {
        console.log("Connected to WebSocket");
        document.getElementById("username-section").style.display = "none";
        document.getElementById("chat-section").style.display = "block";
        loadMessages();
    };

    socket.onmessage = function (event) {
        let chatBox = document.getElementById("chat-box");
        let newMessage = document.createElement("p");

        if (event.data.includes("joined the chat") || event.data.includes("left the chat")) {
            newMessage.className = "system-message";
        } else if (event.data.startsWith(`💬 ${username}:`)) {
            newMessage.className = "self-message";
        } else {
            newMessage.className = "user-message";
        }

        newMessage.textContent = event.data;
        chatBox.appendChild(newMessage);
        chatBox.scrollTop = chatBox.scrollHeight;
    };

    socket.onerror = function (error) {
        console.error("WebSocket Error:", error);
    };
}

function sendMessage() {
    let messageInput = document.getElementById("message");
    let message = messageInput.value;
    
    if (message.trim() !== "" && socket) {
        socket.send(message);
        messageInput.value = "";
    }
}

// Fetch last 20 messages from MongoDB
function loadMessages() {
    fetch("http://127.0.0.1:8000/messages")
        .then(response => response.json())
        .then(messages => {
            let chatBox = document.getElementById("chat-box");
            chatBox.innerHTML = ""; // Clear old messages
            messages.reverse().forEach(msg => {
                let msgElement = document.createElement("p");
                msgElement.textContent = `💬 ${msg.username}: ${msg.content}`;
                chatBox.appendChild(msgElement);
            });
            chatBox.scrollTop = chatBox.scrollHeight;
        })
        .catch(error => console.error("Error loading messages:", error));
}
