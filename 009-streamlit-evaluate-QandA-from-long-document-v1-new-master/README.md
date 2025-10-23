# Streamlit Evaluate Q&A from Long Document - Modern Version

A modernized version of the Streamlit RAG (Retrieval-Augmented Generation) evaluation application using the latest versions of Python 3.13.3, Poetry 2.1.4, Streamlit 1.49+, and LangChain 0.3+ modular architecture.

## Features

- **RAG App Evaluation**: Test the quality of retrieval-augmented generation systems
- **Document Upload**: Process .txt files for knowledge base creation
- **Vector Database**: FAISS-based document embeddings and similarity search
- **Question-Answer Evaluation**: Compare AI-generated answers against known correct answers
- **Hallucination Detection**: Identify when AI produces incorrect or fabricated information
- **Evaluation Chain**: Automated grading of answer quality and accuracy
- **Modern dependency stack** with the most comprehensive LangChain integration

## Requirements

- Python 3.13.3 or higher
- Poetry 2.1.4 or higher

## Installation

1. Navigate to the project directory:
```bash
cd 009-streamlit-evaluate-QandA-from-long-document-v1-new
```

2. Install dependencies:
```bash
poetry-2.1.4 install
```

## Usage

1. Start the Streamlit application:
```bash
poetry-2.1.4 run streamlit run main.py
```

2. Open your browser to the displayed URL (typically http://localhost:8501)

3. **Upload Document**: Upload a .txt file containing your knowledge base

4. **Enter Question**: Provide a question you've already fact-checked

5. **Provide Real Answer**: Enter the known correct answer to the question

6. **Enter API Key**: Provide your OpenAI API key in the form

7. **Submit**: Click Submit to evaluate the RAG system

8. **View Results**: See the comparison between AI answer and real answer with evaluation grade

## How RAG Evaluation Works

### 1. Document Processing
- **Text Splitting**: Document is chunked into manageable pieces (1000 characters)
- **Embeddings**: Each chunk is converted to vector embeddings using OpenAI
- **Vector Store**: FAISS creates a searchable database of document embeddings

### 2. Question Answering
- **Retrieval**: System finds most relevant document chunks for the question
- **Generation**: OpenAI generates an answer based on retrieved context
- **Prediction**: System produces its best answer to the question

### 3. Answer Evaluation
- **Comparison**: AI answer is compared against the known correct answer
- **Evaluation Chain**: LangChain evaluation determines if the AI answer is correct
- **Grading**: System provides assessment of answer quality and accuracy

## Example Workflow

1. **Upload**: A document about company policies
2. **Question**: "What is the vacation policy for new employees?"
3. **Real Answer**: "New employees get 15 days of vacation after 6 months"
4. **AI Processing**: System retrieves relevant sections and generates answer
5. **Evaluation**: Compare AI answer vs real answer and grade accuracy
6. **Results**: Show question, real answer, AI answer, and evaluation grade

## Technical Details

### RAG Pipeline Architecture
- **Document Loader**: Processes uploaded .txt files
- **Text Splitter**: CharacterTextSplitter with 1000 character chunks
- **Embeddings**: OpenAI embeddings for semantic search
- **Vector Store**: FAISS for efficient similarity search
- **Retriever**: Retrieval interface for finding relevant contexts
- **QA Chain**: RetrievalQA with "stuff" chain type for answer generation
- **Evaluation Chain**: QAEvalChain for automated answer grading

### Advanced Interface
- **File Upload**: Drag-and-drop .txt document processing
- **Conditional Fields**: Question and answer inputs enabled only after file upload
- **Form Validation**: API key and input validation before processing
- **Processing Indicator**: Spinner during RAG evaluation
- **Results Display**: Structured output showing all evaluation components

### Most Complex Migration

This represents the **most complex migration** of all 6 apps:
- **6 LangChain packages**: Highest dependency count requiring specialized components
- **Vector Database Integration**: FAISS for document embeddings and retrieval
- **Multi-step Processing**: Document → Chunks → Embeddings → Vector Store → Retrieval → Generation → Evaluation
- **Evaluation Chains**: Specialized chains for answer quality assessment
- **Form-based Submission**: Complex conditional field enabling and validation

## Key Modernizations

- **Python 3.13.3**: Latest Python version with performance improvements
- **Poetry 2.1.4**: Modern dependency management with PEP 621 compliance
- **Comprehensive LangChain**: 6 specialized packages for complete RAG functionality:
  - `langchain-core`: Core functionality and base classes
  - `langchain-text-splitters`: Document chunking utilities  
  - `langchain-community`: FAISS integration and embeddings
  - `langchain-openai`: OpenAI model integration
  - `langchain`: Complex chains (RetrievalQA, QAEvalChain)
  - `faiss-cpu`: Vector database for similarity search
  - `tiktoken`: Token counting for optimization
- **Streamlit 1.49+**: Latest Streamlit features available

## Code Changes Summary

Only **2 lines** of code changed from the original version:
1. Import: `from langchain.text_splitter import CharacterTextSplitter` → `from langchain_text_splitters import CharacterTextSplitter`
2. Chain method: `predictions = qachain.apply(real_qa)` → `predictions = qachain.batch(real_qa)`

## RAG Evaluation Categories

The app evaluates these aspects:

### 1. Retrieval Quality
- Does the system find the most relevant document sections?
- Are the retrieved contexts sufficient to answer the question?

### 2. Generation Accuracy
- Is the AI-generated answer factually correct?
- Does it align with the information in the document?

### 3. Answer Completeness
- Does the answer address all aspects of the question?
- Is important information missing or hallucinated?

### 4. Evaluation Reliability
- How accurately does the evaluation chain assess answer quality?
- Are the evaluation criteria appropriate for the question type?

## Use Cases

- **Content Quality Assurance**: Test RAG systems before production deployment
- **Knowledge Base Validation**: Verify that document-based QA systems work correctly
- **Hallucination Detection**: Identify when AI systems generate incorrect information
- **RAG System Comparison**: Compare different retrieval and generation approaches
- **Training Data Quality**: Assess whether knowledge bases support accurate answers

## Dependencies

Comprehensive modern dependency stack with 6 LangChain packages:
- `langchain>=0.3.0` - Complex chains and orchestration
- `langchain-core>=0.3.0` - Fundamental LangChain components
- `langchain-text-splitters>=0.3.0` - Document processing utilities
- `langchain-community>=0.3.0` - FAISS and community integrations
- `langchain-openai>=0.2.0` - OpenAI model integration
- `faiss-cpu>=1.9.0` - Vector database for similarity search
- `tiktoken>=0.8.0` - Token counting functionality
- `streamlit>=1.49.0` - Modern web interface framework

## Migration Complexity Comparison

| App | Lines Changed | LangChain Packages | Complexity |
|-----|---------------|-------------------|------------|
| Extract JSON | 3 | 2 | Simplest |
| Blog generator | 3 | 2 | Simple |
| Text redaction | 4 | 2 | Simple |
| Text summarization | 3 | 4 | Medium |
| Split & summarize | 4 | 5 | Complex |
| **RAG Evaluation** | **2** | **6** | **Most Complex** |
