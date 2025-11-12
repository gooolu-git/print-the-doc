# PrinTum: Dynamic PDF Generation Web Application Report

> This report outlines the architecture, features, and deployment strategy for PrinTum, a dedicated web service for generating custom No Dues Certificates (NOCs) using Flask and WeasyPrint.

***

## 1. Project Overview

The PrinTum application serves as a minimal **Flask** web service designed to generate a customizable "No Dues Certificate" (NOC) PDF on demand. The core functionality relies on the user providing a month and year via a simple web form. This input is then dynamically inserted into a stylized HTML template and converted into a ready-to-download PDF document using the **WeasyPrint** library.

### Core Technologies
* **Backend Framework:** Python (Flask)
* **PDF Generation:** WeasyPrint (requires system dependencies: Pango, Cairo)
* **Styling & UI:** Bootstrap 5 (for the landing page)
* **Deployment Strategy:** Docker (using Gunicorn for production)

***

## 2. Application Features

### 2.1 Frontend (`index.html`)

The user interface focuses on simplicity and clear interaction.

* **Branding:** Features the application header **PrinTum**.
* **Modern Interface:** Styled with **Bootstrap 5** for a responsive, clean, and modern look.
* **Input Form:** Collects the required **Month and Year** string from the user (e.g., `August-2025`).

### 2.2 Backend (`app.py`)

The Flask application manages data flow and the resource-intensive PDF generation process.

* **Routes:**
    * `/`: Serves the landing page.
    * `/generate-pdf` (POST): Processes the month input and triggers PDF creation.
* **Dynamic Content:** Inserts the user-provided month/year and the current date into the document template.
* **Robust Error Handling:** Includes specific `try...except` blocks to provide informative error messages in the event of missing WeasyPrint system dependencies.

### 2.3 Document Template (`noc_template.html`)

The document template is styled using precise inline CSS to ensure accurate PDF reproduction of the original document.

* **Structure:** Features a centered **YANTRAM MOBILE** header and a split layout for recipient details (left) and the date (right).
* **Visual Fidelity:**
    * **Highlighted Blocks:** Subject and Note sections feature a light blue background and border.
    * **Margins:** Reduced to `1.5cm` for a professional, minimized-margin look.
    * **Emphasis:** Key identifiers (Dealer ID, Dealer Name, Month) are styled in **bold**.

***

## 3. Deployment Readiness

The application is containerized and ready for deployment on modern platforms that support **Docker**.

### Required Deployment Files

| File | Purpose | Key Content |
| :--- | :--- | :--- |
| **`Dockerfile`** | Container Build Instructions | Ensures installation of all system dependencies (Pango, Cairo) required by WeasyPrint, and configures **Gunicorn** for reliable production serving. |
| **`requirements.txt`** | Python Dependencies | Lists `Flask`, `WeasyPrint`, and `gunicorn`. |

The inclusion of the `Dockerfile` is critical for deployment, as it guarantees that all dependencies—both Python and system-level—are correctly installed, preventing runtime dependency errors.