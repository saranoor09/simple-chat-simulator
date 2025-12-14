# 💬 Simple Chat / Messaging Simulator

SCD Lab Project - Implementation of 5 Design Patterns

## 📋 Project Overview
A desktop-based messaging application demonstrating software design patterns from Software Construction & Development (SCD) course.

## 🎯 Implemented Design Patterns
1. **Factory Method** - `MessageFactory` creates different message types
2. **Builder** - `ChatSessionBuilder` constructs chat sessions step-by-step
3. **Decorator** - `TimestampDecorator`, `BoldDecorator` for message styling
4. **Observer** - `NotificationObserver` for event notifications
5. **Singleton** - `ChatEngine` single global instance

## 🚀 How to Run
```bash
# Clone repository
git clone https://github.com/saramoor09/simple-chat-simulator.git

# Navigate to project
cd simple-chat-simulator

# Run application
python main.py
📁 Project Structure
text
simple-chat-simulator/
├── patterns/              # Design patterns implementations
│   ├── __init__.py       # Package initialization
│   ├── builder.py        # Builder Pattern
│   └── decorator.py      # Decorator Pattern
├── main.py               # Main application + other patterns
└── README.md             # This file
🔧 Requirements
Python 3.8 or higher

Tkinter (included with Python)

🖼️ Features
Discord-like GUI with dark theme

Real-time chat with bot responses

Message styling (bold, timestamps)

Typing indicators

Console logging of all messages
