document.getElementById('generatePdf').addEventListener('click', async () => {
    // Simulate an async call (e.g., fetch API data)
    const asyncResponse = await new Promise(resolve => setTimeout(() => {
        resolve("Some text with an embedded font!");
    }, 1000));

    // Initialize jsPDF
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();

    // Set font size and add text from the async response
    doc.setFontSize(25);
    doc.text(asyncResponse, 20, 30); // Adjusted text position for simplicity

    // Save the created PDF
    doc.save("generated-document.pdf");
}