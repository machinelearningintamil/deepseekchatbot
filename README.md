# DeepSeekChatBot  

DeepSeekChatBot is a locally hosted chatbot powered by [Ollama models](https://ollama.com/). This project enables users to run an AI chatbot entirely offline, ensuring privacy and control over conversations. It supports multiple LLMs, customizable prompts, and local storage for responses.  

### Features  
- Runs locally using Ollama models (e.g., Mistral, Llama, DeepSeek)  
- No internet required for chatbot interactions  
- Easy setup with minimal dependencies  
- Customizable chatbot behavior through prompt engineering  
- Efficient and lightweight for local machines  

### Installation  

#### Install Ollama  
- **For Linux/macOS:**  
  ```bash
  curl -fsSL https://ollama.com/install.sh | sh
  ```  
- **For Windows:**  
  Follow this video tutorial: [Install Ollama on Windows](https://youtu.be/npKenRQkkGU?si=tTV9AwUQjW8Qr7qH)  

#### Set Up DeepSeekChatBot  
1. Clone this repository:  
   ```bash
   git clone https://github.com/yourusername/DeepSeekChatBot.git
   cd DeepSeekChatBot
   ```  
2. Install dependencies/Python 3.10.6:  
   ```bash
   pip install -r requirements.txt
   ```  
3. Run the chatbot:  
   ```bash
   python app.py
   ```  

### Usage  
Once you run the code, you can access the chatbot UI in your browser at:  

👉 [http://127.0.0.1:7860](http://127.0.0.1:7860)  

**How to Use:**  
1. Enter the model name (e.g., `mistral`, `llama3`, `deepseek`) to download it from Ollama.  
2. After downloading, initialize the model.  
3. Once initialized, start chatting! You can:  
   - Ask the AI assistant to generate code snippets.  
   - Get grammar corrections for text.  
   - Engage in general conversations.
  
![Screenshot 2025-02-11 181137](https://github.com/user-attachments/assets/8cd80743-bd6e-492c-b85a-732bfe05225b)
