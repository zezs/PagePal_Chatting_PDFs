# MultiPDF Chat App

The MultiPDF Chat App is a Python application designed for conversing with multiple PDF documents simultaneously. By leveraging natural language processing, users can inquire about the contents of the PDFs and receive relevant responses. It utilizes a language model to ensure accuracy in answering queries, restricting responses to information within the loaded PDFs.

## How It Operates

### PDF Loading
The app begins by extracting text content from multiple PDF documents.

### Text Chunking
Extracted text undergoes segmentation into smaller, manageable portions.

### Language Model
Employing a language model, the application creates vector representations (embeddings) of the text chunks.

### Similarity Matching
Upon receiving a query, the app compares it with text chunks to identify the most semantically similar ones.

### Response Generation
Selected chunks are passed to the language model, which generates responses based on relevant PDF content.

## Dependencies and Installation

To install the MultiPDF Chat App, follow these steps:

1. Clone the repository to your local machine.
2. Install the necessary dependencies by executing the following command:
   ```bash
   pip install -r requirements.txt
