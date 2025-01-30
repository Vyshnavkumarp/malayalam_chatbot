# Malayalam PDF Chatbot - Document Q&A Assistant

A multilingual chatbot that understands Malayalam and answers questions from PDF documents or web articles. Combines AI-powered text analysis with translation capabilities.

![Chatbot Interface Preview](https://github.com/user-attachments/assets/1e8824e5-caba-4688-9c41-d2cd29875ed7)

## Features

- **Multilingual Support**  
  🗣️ Malayalam speech-to-text input  
  🔄 English↔Malayalam bidirectional translation

- **Document Processing**  
  📄 PDF text extraction  
  🌐 Web article scraping & summarization

- **AI Capabilities**  
  ❓ Contextual question answering using T5-large model  
  📝 Text summarization using LSA algorithm

- **User-Friendly Interface**  
  🎙️ Voice input support  
  📱 Responsive web interface  
  📁 File upload capability

## Technology Stack

- **Backend**: Python Flask
- **ML/NLP**: Transformers, Sumy, Newspaper3k
- **Translation**: Googletrans
- **Frontend**: Vanilla JS + PDF.js
- **Speech Recognition**: Web Speech API

## Installation Guide

### Prerequisites
- Python 3.8+
- Node.js (for PDF.js)
- Chrome/Firefox browser

### Step 1: Backend Setup
1. Clone the repository
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download NLTK data:
   ```python
   import nltk
   nltk.download('punkt')
   ```

### Step 2: Frontend Setup
1. Install PDF.js:
   ```bash
   npm install pdfjs-dist
   ```
2. Place compiled PDF.js files in `static/` directory

### Step 3: Run Application
```bash
python main.py
```
Access at: `http://localhost:5000`

## Usage Guide

1. **Input Sources**:
   - Upload PDF files (📁 button)
   - Enter website URLs
   - Direct text input

2. **Ask Questions**:
   1. Type/Speak question in Malayalam
   2. Click "Ask" button
   3. View translated answer in chat window

3. **Voice Commands**:
   - Click microphone icon to start recording
   - Speak in Malayalam
   - Click stop to process audio

4. **Translation**:
   - Automatic translation between English/Malayalam
   - Answers preserved in original context

## File Structure

```
project-root/
├── main.py            # Flask backend
├── requirements.txt   # Python dependencies
├── static/
│   └── chatbot.js     # Frontend logic
├── templates/
│   └── index.html     # Main interface
└── README.md          # Documentation
```

## Configuration Tips

- **Model Optimization**:
  ```python
  # main.py
  qa_pipeline = pipeline("text2text-generation", 
                       model="t5-large",
                       device=0)  # Use GPU if available
  ```
- **Browser Requirements**:
  - Chrome recommended for speech recognition
  - Enable microphone access

## Limitations & Notes

- First run may take time to download T5-large model (~3GB)
- Internet connection required for:
  - Translation services
  - Web article scraping
  - Model downloads
- PDF parsing works best with text-based PDFs (not scanned)
