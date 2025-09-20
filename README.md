# Chatbot FastAPI Project

This project is a simple chatbot web application built with FastAPI and OpenAI's GPT-4 model. It supports both text chat and image generation using OpenAI's API. The frontend uses Jinja2 templates and Bootstrap for styling.

## Features

- Chat with an AI assistant (text-based, jokes by default)
- Image generation from prompts
- WebSocket support for real-time chat streaming
- Responsive UI with Bootstrap

## Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd <repo-folder>
   ```

2. **Create and activate a Python virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install fastapi openai uvicorn python-dotenv jinja2
   ```

4. **Set your OpenAI API key:**
   - Create a `.env` file in the project root:
     ```
     openai_api_key=your_openai_api_key_here
     ```

5. **Run the server:**
   ```bash
   uvicorn main:app --reload
   ```

6. **Access the app:**
   - Open [http://localhost:8000](http://localhost:8000) in your browser.

## File Structure

```
├── main.py
├── templates/
│   ├── home.html
│   ├── layout.html
│   └── image.html
├── .env
└── README.md
```

## Usage

- **Chat:**  
  Go to `/` and start chatting with the bot.
- **Image Generation:**  
  Go to `/image`, enter a prompt, and generate an image.

## Customization

- Change the system prompt in `main.py` (`chat_log`) to modify the bot's behavior.
- Edit the HTML templates in `templates/` for UI changes.

## License

MIT License

---

**Note:**  
You need an OpenAI API key to use this app.  
For production, consider securing your API key and handling
