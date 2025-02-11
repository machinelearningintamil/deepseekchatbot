Here's the updated GitHub repository description with the Windows installation guide for Ollama:  

---

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
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
3. Run the chatbot:  
   ```bash
   python chatbot.py
   ```  

### Requirements  
- Python 3.8+  
- Ollama installed  
- Required Python libraries (`pip install -r requirements.txt`)  
