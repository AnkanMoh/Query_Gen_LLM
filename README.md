# **QueryGen LLM: Natural Language to SQL Query Generator**
[![QueryGen LLM](https://img.shields.io/badge/Live%20App-Streamlit-brightgreen)](https://querygenllm.streamlit.app/)  
**Generate SQL queries seamlessly from natural language inputs.**  

---

## 🌟 **Overview**
QueryGen LLM is a web application that simplifies SQL query generation. Using an intuitive interface, users can upload their SQLite database and input plain English queries. The app leverages cutting-edge LLM (Large Language Models) to generate SQL code dynamically and execute it on the provided database.

**🔗 Live Application:** [https://querygenllm.streamlit.app/](https://querygenllm.streamlit.app/)

---

## ✨ **Features**
- **Natural Language to SQL**: Converts plain English descriptions into valid SQL queries.
- **Schema Detection**: Automatically extracts and displays the schema of the uploaded SQLite database.
- **Query Execution**: Executes the generated SQL query and displays the results.
- **Interactive Interface**: User-friendly, minimalistic design powered by Streamlit.
- **Secure Integration**: API key integration ensures data privacy and secure query generation.

---

## 🚀 **How It Works**
1. **Upload Database**: Upload your SQLite `.db` file.
2. **Enter Query**: Provide a natural language query, such as:
   ```
   "Show the total sales by month."
   ```
3. **Generate SQL**: The app generates a compatible SQL query.
4. **Execute and View Results**: The SQL query is executed, and the results are displayed in an easy-to-read format.

---

## 🛠️ **Technologies Used**
- **Python**: Core programming language.
- **Streamlit**: For building the interactive web application.
- **SQLAlchemy**: For database interactions.
- **Groq API**: LLM-powered query generation.
- **SQLite**: Database format for input files.

---

## 🎨 **Screenshots**

### **Home Page**
![Home Page Screenshot](https://via.placeholder.com/800x400?text=Add+Screenshot+Here)

### **Database Schema Display**
![Schema Display Screenshot](https://via.placeholder.com/800x400?text=Add+Screenshot+Here)

---

## 📝 **Setup Instructions**
### **Prerequisites**
- Python 3.8+
- Pip (Python package manager)
- SQLite database file (`.db`)

### **1. Clone the Repository**
```bash
git clone https://github.com/your-repository/querygen-llm.git
cd querygen-llm
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Run Locally**
```bash
streamlit run app.py
```
Open your browser and navigate to `http://localhost:8501`.

---

## 🌐 **Deployment**
### **Streamlit Cloud**
The application is deployed on [Streamlit Cloud](https://querygenllm.streamlit.app/). To deploy your version:
1. Push the code to your GitHub repository.
2. Link your repository to Streamlit Cloud.
3. Set the necessary environment variables (e.g., API keys).

---

## 🔐 **Environment Variables**
- **`GROQ_API_KEY`**: API key for LLM-powered query generation.
  ```bash
  heroku config:set GROQ_API_KEY=your_api_key
  ```

---

## 🙌 **Contributing**
Contributions are welcome! Feel free to open issues or submit pull requests.

---

## ⭐ **Acknowledgments**
- **Streamlit**: For providing a seamless framework for interactive applications.
- **Groq**: For powering natural language query generation.
- **SQLAlchemy**: For database integration.

---

**Made with ❤️ by [Ankan_Moh](https://github.com/AnkanMoh).**

---
