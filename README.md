# RAG-Based Smart Search System for Analytics Vidhya Courses

This project is a **RAG (Retrieval-Augmented Generation)** based smart search system designed to assist users in finding and querying information related to the free courses available on **Analytics Vidhya**. The system provides relevant course recommendations and answers user queries based on natural language inputs.

## 🌟 Key Features
- **AI-Powered Search**: Utilizes a combination of semantic search and generative AI to deliver precise results.
- **LLAMA 3.3 70B by Groq**: The system uses the powerful **Llama 3.3 70B model** provided by **Groq** for natural language understanding and response generation.
- **Course Content Scraper**: Automated web scraping to collect course content and metadata.
- **RAG Implementation**: Combines traditional information retrieval with a language model to improve search relevance.
- **Vector Search with Pinecone**: Efficient vector storage and similarity search using **Pinecone**.
- **Streamlit Web App**: Interactive, user-friendly interface built with **Streamlit**.

## 📊 Tech Stack
- **Python**: Core programming language
- **BeautifulSoup4 & Requests**: Web scraping
- **Streamlit**: Web app framework
- **Llama 3.3 70B by Groq**: Large language model
- **Pinecone**: Vector database for storing embeddings
- **LangChain**: For integrating RAG components

## 📈 Workflow
1. **Data Collection**:
   - Scraped course content from Analytics Vidhya using `BeautifulSoup4` and `requests`.
   - Stored all course links in a text file for batch processing.
2. **Data Cleaning**:
   - Removed redundant content (e.g., common descriptions across all courses).
   - Split the content into smaller chunks suitable for the model's context window.
3. **Embedding & Storage**:
   - Generated vector embeddings for the cleaned content using **Llama 3.3 70B**.
   - Stored vectors in **Pinecone** for efficient retrieval.
4. **RAG Implementation**:
   - Used a retrieval-augmented generation approach where relevant course sections are retrieved and passed to the model for generating answers.
5. **Streamlit Web App**:
   - Developed a visually appealing **Streamlit** app to allow users to search and get course recommendations.

## 📦 Project Structure
```plaintext
📂 CourseLens
├── 📂 data
│   └── courses.csv
├── 📂 scraping
│   └── scraper.py
|──indexing.py
├── app.py
├── query.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🎯 How to Run the Project
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/devroopsaha744/CourseLens
   cd CourseLens
   ```
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Streamlit App:**
   ```bash
   streamlit run webapp/app.py
   ```

## 🚀 Deployed Version
[Deployed Link](https://huggingface.co/spaces/datafreak/CoureLens)

## 📸 Screenshots
*Include relevant screenshots of the app interface.*

## 🤖 Future Improvements
- Integration with additional LLMs.
- Fine-tuning the **Llama 3.3 70B** model for domain-specific tasks.
- Multi-language support.

## 📧 Contact
Feel free to reach out if you have any questions or suggestions!

**Created by datafreak aka Devroop Saha**

