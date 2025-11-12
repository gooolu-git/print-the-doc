from flask import Flask, render_template, request, make_response
from weasyprint import HTML, CSS
import datetime

# Initializing Flask application
app = Flask(__name__)

# --- Configuration ---
# Set the current date for the document (can be dynamic based on requirements)
CURRENT_DATE = datetime.datetime.now().strftime("%-m/%d/%Y")

# --- Routes ---

@app.route('/', methods=['GET'])
def index():
    """Renders the landing page with the month selection form."""
    return render_template('index.html')

@app.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    """
    Handles form submission, generates the PDF using WeasyPrint,
    and returns it as a downloadable file.
    """
    try:
        # Get the month text entered by the user
        month_text = request.form.get('month_text')
        
        if not month_text:
            # Handle case where month input is empty
            return "Month selection is required.", 400

        # Data to pass to the PDF template
        template_data = {
            'month_text': month_text,
            'current_date': CURRENT_DATE
        }
        
        # 1. Render the HTML content for the PDF using the template
        rendered_html = render_template('noc_template.html', **template_data)

        # 2. Use WeasyPrint to generate PDF from the rendered HTML string
        # WeasyPrint works best with full, well-formed HTML, including styles.
        pdf_bytes = HTML(string=rendered_html).write_pdf()

        # 3. Create the Flask response for file download
        response = make_response(pdf_bytes)
        response.headers['Content-Type'] = 'application/pdf'
        
        # Set the filename for download
        filename = f"NOC_Certificate_{month_text.replace(' ', '_')}.pdf"
        response.headers['Content-Disposition'] = f'attachment; filename="{filename}"'

        return response
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return "An internal server error occurred during PDF generation.", 500

if __name__ == '__main__':
    # Run the application
    app.run()