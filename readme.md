# PDF Conversation AI

This program creates an AI assistant that can answer questions based on the content of multiple PDF files. It uses LangChain and OpenAI to process PDFs, create embeddings, and generate responses in a conversational manner.

## Features

- Loads multiple PDF files from a specified directory
- Creates embeddings for PDF content using OpenAI
- Stores embeddings in a FAISS vector database for efficient retrieval
- Provides a conversational interface to ask questions about the PDF content
- Maintains conversation history for context-aware responses
- Displays the sources (PDF files and page numbers) used for each answer

## Setup and Usage

1. Clone this repository to your local machine.

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

6. Place your PDF files in a folder named `files` in the project directory.

7. Run the program:
   ```
   python run.py
   ```

8. Start asking questions about the content of your PDFs. Type 'quit' to exit the program.

## Requirements

- Python 3.7+
- OpenAI API key
- PDF files to analyze

## Note

This program uses the OpenAI API, which may incur costs based on your usage. Please be aware of the OpenAI pricing model and your account's usage limits.