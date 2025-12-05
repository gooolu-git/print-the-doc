
# **Print-the-doc – PDF Report Generator**

A simple, clean, and powerful **Flask web application** for generating **professional PDF reports** from dynamic HTML content. Users can choose report parameters (like month) and instantly download a beautifully styled PDF.

Built with **Flask**, **Flask-WeasyPrint**, **Bootstrap 5**, and **Jinja2**.

---

## **✨ Overview**

This project demonstrates:

- A **Bootstrap-styled landing page** for selecting report parameters.
- **Dynamic PDF generation** using WeasyPrint.
- Clean and responsive design that looks great both in the browser and in the final PDF.
- A minimal yet scalable architecture built with Flask.

---

## **🔥 Features**

- **🗓 Parameter Selection:**  
  A dedicated landing page to select the month for generating a sales report.

- **📄 Dynamic PDF Generation:**  
  Converts HTML templates into a complete PDF on-the-fly.

- **🎨 High-Fidelity Output:**  
  WeasyPrint ensures pixel-perfect PDF styling with full HTML/CSS support.

- **📱 Responsive UI:**  
  Built using Bootstrap 5 for a modern, mobile-friendly design.

---

## **🛠 Technologies Used**

| **Category**        | **Technology**      | **Purpose** |
|---------------------|---------------------|-------------|
| Backend             | **Python 3**        | Core logic & server runtime |
| Web Framework       | **Flask**           | Routing, request handling |
| PDF Generation      | **Flask-WeasyPrint** | Convert HTML/CSS → PDF |
| HTML Templating     | **Jinja2**          | Dynamic HTML rendering |
| Frontend Styling    | **Bootstrap 5**     | Responsive UI |

---

## **⚙ Installation**

### **📌 Prerequisites**

- Python 3 installed

### **📦 System Dependencies (Required for WeasyPrint)**

#### **Ubuntu/Debian**
```bash
sudo apt update
sudo apt install python3-dev libxml2-dev libxslt1-dev libgomp1 libpango1.0-0
```

#### **macOS (Homebrew)**
```bash
brew install cairo pango gdk-pixbuf libffi
```

---

## **📁 Setup Steps**

### **1️⃣ Create Project Structure**
```bash
mkdir pdf_app
cd pdf_app
mkdir templates static
```

Save these files:

- `app.py`
- `templates/landing.html`
- `templates/report.html`
- `static/style.css`

---

### **2️⃣ Create requirements.txt**
```
Flask
Flask-WeasyPrint
```

---

### **3️⃣ Install Python Packages**
```bash
pip install -r requirements.txt
```

---

## **▶ Usage**

### **Run the application**
```bash
python app.py
```

➡ App runs at: **http://127.0.0.1:5000/**

### **Generate PDF Report**
1. Open the landing page  
2. Select a month  
3. Click **"Submit & Generate PDF"**  
4. Your file (e.g., `sales_report_November_2025.pdf`) will download automatically  

---

## **📂 Project Structure**

```
pdf_app/
├── app.py
├── requirements.txt
├── templates/
│   ├── landing.html
│   └── report.html
└── static/
    └── style.css
```

---

## **👤 Author**

**gooolu-git**  
GitHub: https://github.com/gooolu-git  

## live application:- 
https://printum-pdf-generator.onrender.com/
