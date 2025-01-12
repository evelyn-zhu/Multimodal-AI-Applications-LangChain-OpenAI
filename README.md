# 📚 Multimodal AI Applications with LangChain & OpenAI API

_A Comprehensive Framework for Building Multimodal AI Applications Using LangChain and OpenAI._

---

## 🌟 **Overview**
This repository provides a framework for building **multimodal AI applications**, utilizing **LangChain** and **OpenAI APIs**. It supports processing video, audio, and text data, generating embeddings, and implementing a **Question-Answering (QA)** system.

---

## 🔧 **Features**
- 🎥 **YouTube Video Processing**: Extract audio and generate transcripts for analysis.
- 📝 **Text Embedding**: Leverage OpenAI models for semantic similarity and embeddings.
- ❓ **Question-Answering System**: Create a retrieval-based QA system with LangChain.
- 📂 **Customizable Framework**: Modular design for real-world adaptability.

## 🚀 **Getting Started**

### **2. Set Up the Environment**
Follow these steps to prepare your development environment:

1. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv .venv_multimodal
   source .venv_multimodal/bin/activate
   ```

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### **3. Configure API Keys**
Replace the placeholder in `main.py` with your OpenAI API key:
```python
openai.api_key = "your-openai-api-key"
```
For secure management, consider using a `.env` file or secrets manager.

## 🏗 **Project Structure**
The project follows a modular design:
```plaintext
Multimodal-AI-Applications-LangChain-OpenAI/
├── src/
│   ├── download_video.py    # YouTube video downloader
│   ├── transcribe_audio.py  # Audio transcription module
│   ├── my_embeddings.py     # Text embeddings processing
│   ├── text_loader.py       # Text loader for documents
│   ├── qa_system.py        # QA system configuration
├── files/
│   ├── transcripts/         # Directory for transcripts
│   └── embeddings/          # Processed embeddings
├── requirements.txt         # Python dependencies
├── README.md               # Project documentation
└── main.py                # Main script
```

## 💡 **Usage**

### **Running the Application**
To process a YouTube video and interact with the QA system, execute the following:
```bash
python main.py
```

### **Example Queries**
Once the QA system is running, you can try queries such as:
* "What is this tutorial about?"
* "What is the difference between training and test datasets?"

## 📖 **Technologies Used**
* **Python 3.11**
* **LangChain** for chaining AI tasks
* **OpenAI API** for embedding generation and transcription
* **yt-dlp** for video processing

## ⚖ **License**
This project is licensed under the MIT License.

## 🤝 **Contributing**
Contributions are welcome! Please fork this repository and submit a pull request.

## 🌐 **Contact**
For questions or feedback, please reach out via GitHub issues or contact the repository owner directly.
