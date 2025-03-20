# Audio-to-Text LLM Test

This project is designed to leverage local language models and artificial intelligence technologies to optimize human resources processes. It includes tools for audio transcription and generating structured summaries or proposals based on the transcribed content.

## Features

- **Audio Transcription**: Converts audio files into text using the Groq API.
- **Text Summarization**: Generates professional summaries in Turkish, including short summaries, detailed summaries, and action items.
- **Project Proposal Generation**: Creates structured project proposals in Turkish using extracted text and AI models.
- **Customizable Prompts**: Allows users to define specific prompts for generating tailored outputs.
- **LLM Monitoring Tool**: Test and monitor the performance of language models using Portkey AI's monitoring tool.

## Requirements

- Python 3.8 or higher
- API keys for:
  - Groq
  - Portkey AI

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/tahsinsoyak/audio-to-text-llm-test.git
   cd audio-to-text-llm-test
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project directory and add your API keys:
   ```
   GROQ_API_KEY="your_groq_api_key"
   Portkey_API_KEY="your_portkey_api_key"
   Portkey_Virtual_KEY="your_portkey_virtual_key"
   ```

4. Place your audio file (`3.mp3`) in the project directory for transcription.

## Usage

### Audio Transcription and Summarization
Run the `convert.py` script to transcribe an audio file and generate structured summaries:
```bash
python convert.py
```

### Project Proposal Generation
Prepare a text file (`text.txt`) with the content you want to use for the proposal. Then, run the `app.py` script:
```bash
python app.py
```

## File Structure

- `convert.py`: Handles audio transcription and generates structured summaries.
- `app.py`: Generates project proposals based on text input.
- `.env`: Stores API keys (not included in version control).
- `README.md`: Documentation for the project.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [Groq API](https://groq.com) for audio transcription.
- [Portkey AI](https://portkey.ai) for advanced language model capabilities.
