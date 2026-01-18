## How It Works

This project demonstrates the internal architecture of a basic Command & Control (C2) model implemented in Python.
It simulates how a control server communicates with a remote client to send commands and receive execution results.

The implementation is intentionally simple and designed strictly for educational and defensive analysis purposes.
It helps students understand how attackers structure C2 communication and how defenders can detect such behavior.

## Architecture

The project is composed of two logical components:

Server  
Acts as the command dispatcher and control interface used by the operator.

Client  
Simulates an infected endpoint that connects back to the server and executes received commands.

Both components communicate using:
- TCP sockets
- JSON serialization for message exchange
- A blocking command/response model

## Communication Flow

1. The client connects to the control server
2. The server sends a command
3. The client processes and executes the command
4. The execution output is returned to the server
5. The server displays the response to the operator

[ Operator ] → Server → Client → Execution → Response → Server

## Features

Remote shell command execution  
Remote directory navigation  
File upload from server to client  
File download from client to server  
Screenshot capture simulation  
JSON-based C2 communication channel  

## Requirements

Python 3.x  
Linux or Windows system  

Required Python libraries:
- pyautogui
- termcolor

## Installation

### Clone the repository
git clone https://github.com/yourusername/basic-c2-simulator.git
cd basic-c2-simulator

### Install dependencies
pip install pyautogui termcolor

## Usage

### Start the server
python server.py

### Start the client
python backdoor.py

Once connected, the server provides an interactive shell interface for issuing commands.

## Implemented Capabilities

Execute system commands remotely  
Change directories on the client system  
Upload files to the client  
Download files from the client  
Capture screenshots from the client  
Structured command exchange using JSON  

## Detection & Defense Notes

From a defensive perspective, behavior like this can be detected through:

Network IDS/IPS monitoring  
EDR telemetry (process execution, screenshot APIs)  
Unusual outbound TCP connections  
Repeated command/response traffic patterns  
Suspicious file transfer activity  

## Use Cases

Blue Team detection training  
Red Team simulation labs  
Malware traffic analysis  
Security research and education  
CTF challenge creation  

## Future Improvements

Encrypted communication (TLS)  
Authentication between client and server  
Non-blocking communication model  
Beaconing and heartbeat simulation  
Traffic obfuscation techniques  
Centralized logging and telemetry  

## Legal Disclaimer

This project is provided strictly for educational purposes only.

### Do NOT:
Use on real networks  
Deploy on systems you do not own  
Use for spying, persistence, unauthorized access, or data theft  

Any misuse of this code is the sole responsibility of the user.

## License

This project is licensed under the MIT License.

