from fastapi import FastAPI, UploadFile, HTTPException, File
from fastapi.responses import HTMLResponse, StreamingResponse
import requests
import PyPDF2
import io
from fpdf import FPDF

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def upload_form():
    return """
    <html>
        <body>
            <h2>Upload PDF to Extract Text from First Page</h2>
            <form action="/extract-text" method="post" enctype="multipart/form-data">
                <input name="pdf_file" type="file" accept="application/pdf">
                <input type="submit">
            </form>
        </body>
    </html>
    """
@app.get("/generate-pdf/")
def generate_pdf():
    # Create a PDF object
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Hello, this is a PDF from FastAPI!", ln=True, align='C')
    
    # Save the PDF to a bytes buffer
    pdf_buffer = io.BytesIO()
    pdf.output(pdf_buffer)
    pdf_buffer.seek(0)

    # Return the buffer value as a StreamingResponse, setting the media type to pdf
    return StreamingResponse(pdf_buffer, media_type="application/pdf")


@app.get("/extract-text/")
async def extract_text_from_pdf():
    pdf_url = 'https://storage.googleapis.com/gg-lyrics.appspot.com/07a_Worksheet%20on%20Vocabulary1.pdf'
    pdf_response = requests.get(pdf_url)

    # Check if the response status code is OK (200)
    if pdf_response.status_code != 200:
        raise HTTPException(status_code=400, detail="Failed to fetch PDF file.")

    # Check the content type from the response headers
    content_type = pdf_response.headers.get('Content-Type')
    if content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="File must be a PDF.")

    try:
        # Read the content of the PDF
        contents = pdf_response.content
        reader = PyPDF2.PdfReader(io.BytesIO(contents))
        first_page = reader.pages[0]
        extracted_text = first_page.extract_text()
        
        return {"extracted_text": extracted_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    import os
    uvicorn.run(app, host="localhost", port=int(os.environ.get('PORT', 8080)))
