# MultiPDF Chat App
The MultiPDF Chat App is a Python application that allows you to chat with multiple PDF documents. You can ask questions about the PDFs using natural language, and the application will provide relevant responses based on the content of the documents. This app utilizes a language model to generate accurate answers to your queries. Please note that the app will only respond to questions related to the loaded PDFs.
Response Generation: The selected chunks are passed to the language model, which generates a response based on the relevant content of the PDFs.

## Project Workflow
![MultiPDF Chat App](project_workflow.png)

## The application follows these steps to provide responses to your questions:

1. PDF Loading: The app reads multiple PDF documents and extracts their text content.

2. Text Chunking: The extracted text is divided into smaller chunks that can be processed effectively.

3. Language Model: The application utilizes a language model to generate vector representations (embeddings) of the text chunks.

4. Similarity Matching: When you ask a question, the app compares it with the text chunks and identifies the most semantically similar ones.

5. Response Generation: The selected chunks are passed to the language model, which generates a response based on the relevant content of the PDFs.

## Dependencies and Installation

To install the MultiPDF Chat App, follow these steps:

1. Clone the repository to your local machine.
2. Install the necessary dependencies by executing the following command:
   ```bash
   - pip install -r requirements.txt
4. Obtain an API key from OpenAI and add it to the .env file in the project directory.
   ```bash
   - OPENAI_API_KEY=your_secrit_api_key
