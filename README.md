# DeepSeekChatBot  

DeepSeekChatBot is a locally hosted chatbot powered by [Ollama models](https://ollama.com/). This project enables users to run an AI chatbot entirely offline, ensuring privacy and control over conversations. It supports multiple LLMs, customizable prompts, and local storage for responses.  

### Features  
- Runs locally using Ollama models (e.g., Mistral, Llama, DeepSeek)  
- No internet required for chatbot interactions  
- Easy setup with minimal dependencies  
- Customizable chatbot behavior through prompt engineering  
- Efficient and lightweight for local machines  

### Installation  
1. Install Ollama:  
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ```
2. Clone this repository:  
   ```bash
   git clone https://github.com/yourusername/DeepSeekChatBot.git
   cd DeepSeekChatBot
   ```
3. Run the chatbot:  
   ```bash
   python app.py
   ```

### Requirements  
- Python 3.8+  
- Ollama installed  
- Required Python libraries (`pip install -r requirements.txt`)  

### Usage  
Simply run the script and start chatting with your locally hosted AI assistant. Modify the prompt and model settings in `config.json` to tweak chatbot behavior.  

---
