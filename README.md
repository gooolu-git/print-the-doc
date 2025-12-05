print-the-doc
Overview

This is a simple, yet robust, Flask web application designed to demonstrate the generation of stylized PDF reports from dynamic HTML content. It features a Bootstrap-themed landing page where users can select report parameters (like the month) before generating and downloading a clean, professional PDF file. The application leverages the power of Python's Flask framework combined with Flask-WeasyPrint for high-fidelity PDF output.

The frontend uses Bootstrap 5 for a responsive, modern user interface, ensuring a good experience both on the web and in the final printed document.

Features

Parameter Selection: A dedicated landing page allows users to select the month for which they want to generate a sales report.

Dynamic PDF Generation: Generates a full PDF document on the fly based on the selected parameters.

High-Fidelity Output: Uses WeasyPrint to convert HTML/CSS templates into pixel-perfect PDF documents, preserving styling and layout.

Bootstrap Styling: Utilizes Bootstrap 5 for clean, professional, and responsive web interface design and PDF report styling.

Technologies Used

Category

Technology

Purpose

Backend

Python 3

Core application logic and server runtime.

Web Framework

Flask

Micro web framework for routing and handling requests.

PDF Generation

Flask-WeasyPrint

Extension for generating PDF documents from HTML/CSS.

HTML Templating

Jinja2

Used by Flask to render dynamic HTML templates.

Frontend Styling

Bootstrap 5

CSS framework for responsive design and UI components.

Installation

Prerequisites

You need Python 3 installed on your system.

Crucial Dependency: Flask-WeasyPrint relies on the WeasyPrint library, which requires specific system dependencies to handle rendering and fonts (like Pango, Cairo, and Glib).

On Debian/Ubuntu, install the dependencies first:

sudo apt update
sudo apt install python3-dev libxml2-dev libxslt1-dev libgomp1 libpango1.0-0


On macOS (using Homebrew):

brew install cairo pango gdk-pixbuf libffi


Setup Steps

Clone the Repository (or create the file structure):

If you are setting this up manually, create the necessary folders:

mkdir pdf_app
cd pdf_app
mkdir templates static
# Now save app.py, landing.html, report.html, and style.css into their respective locations.


Create requirements.txt:

Flask
Flask-WeasyPrint


Install Python Packages:

pip install -r requirements.txt


Usage

Run the Flask application:

python app.py


The application will start, usually accessible at http://127.0.0.1:5000/.

Access the Landing Page:

Open the URL in your web browser. You will be presented with the "Gemini Analytics" landing page.

Generate Report:

Select a month from the dropdown menu.

Click the "Submit & Generate PDF" button.

A new browser tab will open, and the PDF file (e.g., sales_report_November_2025.pdf) will automatically download.

Project Structure

app.py: Main Flask application file. Defines routes, data, and PDF generation logic.

requirements.txt: Lists Python dependencies.

templates/: Directory for Jinja2 HTML template files.

landing.html: The Bootstrap-themed front page for parameter selection.

report.html: The HTML template used by WeasyPrint to generate the PDF content.

static/: Directory for static assets.

style.css: Minimal CSS overrides and print-specific rules.

Author

gooolu-git

GitHub: https://github.com/gooolu-git

Note: This is a placeholder GitHub profile as requested.
https://printum-pdf-generator.onrender.com/
