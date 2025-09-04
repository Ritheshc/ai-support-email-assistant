# 📘 AI Support Email Assistant - Documentation

## 🏗 Architecture
The solution follows a modular design:

1. **Data Source**
   - Current version: CSV dataset (`Sample_Support_Emails_Dataset.csv`)
   - Future scope: Integration with Gmail/Outlook/IMAP APIs for real-time email retrieval

2. **Backend Processing (Flask + Python)**
   - **Preprocessing:** Loads dataset using Pandas
   - **Sentiment Analysis:** Uses TextBlob to classify sentiment (Positive, Negative, Neutral)
   - **Priority Detection:** Keyword-based rules (e.g., "immediately", "urgent", "cannot access")
   - **Information Extraction:** Regex-based extraction of phone numbers, email IDs, and customer metadata
   - **Response Drafting (extendable):** Placeholder for LLM integration (OpenAI/Hugging Face with RAG)

3. **Dashboard / Frontend**
   - Flask template rendering (HTML + CSS)
   - Displays support emails with:
     - Sender
     - Subject
     - Email Body Snippet
     - Sentiment
     - Priority
     - Extracted Contacts
   - Demo screenshot included in repo

4. **Storage**
   - CSV-based for hackathon demo
   - Extendable to SQLite, PostgreSQL, or MongoDB

---

## ⚙️ Approach
1. **Filtering Emails**
   - Emails containing keywords like *Support, Query, Help, Request* are filtered.
   - Dataset is processed for analysis.

2. **Categorization & Prioritization**
   - Sentiment analysis performed using TextBlob.
   - Priority detection uses keyword-based rule engine.
   - Urgent emails appear on top for faster response.

3. **Information Extraction**
   - Regex applied to extract:
     - Phone numbers (10-digit)
     - Email addresses
     - Other metadata

4. **Context-Aware Auto-Response (Planned)**
   - LLM-based draft generation.
   - Empathetic tone for negative/frustrated users.
   - Contextual answers using Retrieval-Augmented Generation (RAG).

5. **Dashboard**
   - Simple web interface with a table.
   - Provides structured view of emails with analytics-ready metadata.

---

## 📌 Impact
- **Efficiency:** Reduces manual workload in reading and categorizing support emails.
- **Quality:** Ensures faster, empathetic responses.
- **Scalability:** Easily extendable to real-world email APIs and databases.
- **Customer Satisfaction:** Improves support turnaround time and customer trust.

---
