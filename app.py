# app.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from insights_engine import generate_insights
from fpdf import FPDF
import os
import tempfile

st.set_page_config(page_title="AI Business Insights", layout="wide")

# Custom CSS
st.markdown("""
    <style>
        .container {
            max-width: 75%;
            margin: auto;
        }
        .main-title {
            background: linear-gradient(90deg, #2b5876, #4e4376);
            padding: 1.2rem;
            border-radius: 15px;
            text-align: center;
            color: white;
            font-size: 2.2rem;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            font-weight: bold;
            margin-bottom: 1.5rem;
        }
        .section-title {
            background: linear-gradient(90deg, #2b5876, #4e4376);
            padding: 0.7rem 1rem;
            border-radius: 10px;
            color: white;
            font-size: 1.2rem;
            margin: 0.2rem 0 0.2rem 0;
        }
        .data-box, .insights-box {
            background: #1e222d;
            padding: 1rem;
            border-radius: 10px;
            border: 1px solid #333;
            box-shadow: 0 2px 10px rgba(0,0,0,0.3);
        }
        .insights-box {
            border-left: 6px solid #4e4376;
            margin-top: 0.5rem;
        }
        .stButton>button, .stDownloadButton>button {
            background-color: #4e4376;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 0.5rem 1.2rem;
        }
        .stSelectbox>div {
            background-color: #0e1117 !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="container">', unsafe_allow_html=True)
st.markdown('<div class="main-title">📊 AI-Powered Business Insights</div>', unsafe_allow_html=True)

# Upload CSV
st.markdown('<div class="section-title">📁 Upload Your Business Dataset</div>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Quick Overview
    st.markdown('<div class="section-title">🔍 Quick Overview</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📌 Data Preview")
        st.dataframe(df.head(20), height=450)

    with col2:
        st.subheader("📈 Basic Statistics")
        st.dataframe(df.describe(), height=450)

    # Auto Visual Summary (2x2 layout using one selected column)
    st.markdown('<div class="section-title">📊 Auto Visual Summary</div>', unsafe_allow_html=True)
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()

    if numeric_cols:
        selected_col = st.selectbox("Select a column for all charts", numeric_cols)

        vcol1, vcol2 = st.columns(2)
        with vcol1:
            fig1, ax1 = plt.subplots()
            sns.histplot(df[selected_col], kde=True, ax=ax1, color="skyblue")
            ax1.set_title(f"Histogram of {selected_col}")
            ax1.set_xlabel(selected_col)
            ax1.set_ylabel("Frequency")
            ax1.grid(True, linestyle="--", alpha=0.4)
            st.pyplot(fig1)

        with vcol2:
            fig2, ax2 = plt.subplots()
            sns.boxplot(x=df[selected_col], ax=ax2, color="orchid")
            ax2.set_title(f"Boxplot of {selected_col}")
            ax2.set_xlabel(selected_col)
            ax2.grid(True, linestyle="--", alpha=0.4)
            st.pyplot(fig2)

        vcol3, vcol4 = st.columns(2)
        with vcol3:
            fig3, ax3 = plt.subplots()
            sns.lineplot(data=df[selected_col], ax=ax3, color="lime")
            ax3.set_title(f"Line Trend of {selected_col} (by index)")
            ax3.set_xlabel("Index")
            ax3.set_ylabel(selected_col)
            ax3.grid(True, linestyle="--", alpha=0.4)
            st.pyplot(fig3)

        with vcol4:
            fig4, ax4 = plt.subplots()
            sns.barplot(x=df[selected_col].value_counts().index[:10], 
                        y=df[selected_col].value_counts().values[:10], ax=ax4, color="orange")
            ax4.set_title(f"Top 10 Frequent Values of {selected_col}")
            ax4.set_xlabel(selected_col)
            ax4.set_ylabel("Count")
            ax4.tick_params(axis='x', rotation=45)
            ax4.grid(True, linestyle="--", alpha=0.4)
            st.pyplot(fig4)

    # AI Insights
    st.markdown('<div class="section-title">🧠 AI Insights & Recommendations</div>', unsafe_allow_html=True)

    try:
        summary_text = f"""
        Data Head (first 5 rows):
        {df.head(5).to_string(index=False)}

        Column Types:
        {df.dtypes.astype(str).to_string()}

        Unique Values per Column:
        {df.nunique().to_string()}

        Statistical Summary:
        {df.describe().to_string()}
        """

        with st.spinner("Generating intelligent recommendations..."):
            insights = generate_insights(summary_text)
            insights_clean = insights.replace("**", "").strip()
            st.markdown(f"<div class='insights-box'>{insights_clean}</div>", unsafe_allow_html=True)

        # PDF Export
        def export_full_pdf(text, filename="AI_Report.pdf"):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                pdf.multi_cell(0, 10, "AI Business Insights Report\n\n")
                pdf.multi_cell(0, 10, text)
                pdf.output(tmp.name)
                return tmp.name

        bcol1, bcol2 = st.columns([1, 2])
        with bcol1:
            if st.button("🖨️ Export Full Report as PDF"):
                pdf_path = export_full_pdf(insights_clean)
                with open(pdf_path, "rb") as f:
                    st.download_button("⬇️ Download PDF", f, file_name="AI_Report.pdf", mime="application/pdf")

    except Exception as e:
        st.error("⚠️ Could not generate insights due to a data formatting issue.")
        st.exception(e)

else:
    st.info("Upload a CSV file to get started.")

st.markdown('</div>', unsafe_allow_html=True)