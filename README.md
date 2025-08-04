# 📊 AI-Powered Business Insights

Welcome to the **AI-Powered Business Insights** app — a sleek, intelligent, and ready-to-use Streamlit dashboard that transforms your business CSV datasets into **visualizations**, **statistical summaries**, and **AI-generated recommendations** using the power of **LLMs (via Groq API)**.

<br>

## 🚀 Demo Preview

<img width="1263" height="367" alt="image" src="https://github.com/user-attachments/assets/c2ecd582-590c-4769-9db3-4cf80581fd4b" />
<img width="1305" height="528" alt="image" src="https://github.com/user-attachments/assets/b04cb790-0b2f-40b7-ad9d-472153667b9b" />
<img width="1252" height="535" alt="image" src="https://github.com/user-attachments/assets/33f67663-0135-4205-8320-a585e393c34a" />
<img width="1226" height="540" alt="image" src="https://github.com/user-attachments/assets/57dfbb3b-7947-4d4a-96ae-076818d766a3" />
<img width="1272" height="498" alt="image" src="https://github.com/user-attachments/assets/fde32fb8-12a8-4c97-9b16-d8d1b6021670" />
<img width="1263" height="480" alt="image" src="https://github.com/user-attachments/assets/f5356275-7f9c-404d-b089-2df5c4524c58" />





---

## 🧠 What This App Does

- ✅ Upload your business CSV data (sales, marketing, financials, etc.)
- 📈 Select column to generates key visuals (histograms, boxplots, trends, value counts)
- 📊 Summarizes data stats and structure
- 🧠 Uses LLMs to provide smart **insights**, **recommendations**, and **actionable takeaways**
- 🖨️ Exports full AI-generated report as a **PDF**

---


## 🛠️ Tech Stack

| Technology     | Purpose                             |
|----------------|--------------------------------------|
| `Streamlit`    | Web app framework (v1.12.0)          |
| `Pandas`       | Data wrangling                       |
| `Seaborn`      | Visualizations                       |
| `Matplotlib`   | Plot rendering                       |
| `FPDF`         | Exporting AI insights to PDF         |
| `Groq (LLaMA3)`| LLM-based business recommendations   |
| `.env`         | Secure API key storage               |

---

## ⚙️ Setup Instructions

> 📦 **Prerequisites**: Python 3.9+ and Git installed on your system

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai_business_insights.git
cd ai_business_insights
```
### 2. Create and activate a virtual environment
```bash
python -m venv .venv
```
Windows:

```bash
.venv\Scripts\activate
```
Mac/Linux:

```bash

source .venv/bin/activate
```
### 3. Install dependencies
```bash

pip install -r requirements.txt
```
### 4. Add your Groq API key
Create a .env file in the project root and add your key:

```env

GROQ_API_KEY=your_groq_api_key_here
```
### 5. Launch the app
```bash

streamlit run app.py
```
## 📤 How to Use
1. Run the app in your browser

2. Upload a CSV file (you can start with one from the data/ folder)

3. Preview the data and generate charts

4. Get intelligent business recommendations

5. Export insights as a polished PDF report

## 🔐 Environment Variables
Do not push your .env file to GitHub. Your .gitignore handles this automatically.

Your .env should include:

```env

GROQ_API_KEY=your_real_api_key
```
## 📄 PDF Export
Click the 🖨 Export Full Report as PDF button to generate a downloadable file summarizing the AI’s recommendations — perfect for clients or stakeholders.

## 🐳 Docker (Optional)
You can easily dockerize this app for production. Ask and we'll help you generate a Dockerfile.



## 🙋 FAQ
Q: Does it support Excel or JSON?

No. Only .csv is supported for now.

Q: Is it using OpenAI?

No. It uses Groq’s LLaMA 3 API for free LLM access.

Q: Can I customize the visuals?

Yes. You can modify the chart section inside app.py.



## ⭐ Like This Project?
Give it a ⭐ on GitHub and share with others — especially if you're a freelancer or data analyst looking to impress clients.
