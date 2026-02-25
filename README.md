# Simple Web Resume

A clean, responsive, and data-driven resume template that populates content from a JSON file. This project is designed for easy customization and professional printing.

<img width="928" height="1045" alt="image" src="https://github.com/user-attachments/assets/663fa540-3acf-4a01-b6fb-6e4af42a2dc6" />


## Features
- **JSON Driven:** Update your resume content in one place (`resume.json`).
- **Clean Design:** Professional typography and icons using Google Fonts and Font Awesome.
- **Print Optimized:** Styled specifically for "Save to PDF" to ensure a high-quality physical or digital document.
- **No Build Step:** Pure HTML, CSS, and Vanilla JavaScript.

## Setup & Customization

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/simple-web-resume.git
   cd simple-web-resume
   ```

2. **Edit your details:**
   Open `resume.json` and replace the placeholder text with your own information. You can update:
   - Personal details (Name, Title, Contact Info)
   - Professional Summary
   - Key Achievements & Project Highlights
   - Work Experience & Education
   - Skills (categorized by type)

## How to Run Locally

Since the project uses the JavaScript `fetch` API to load `resume.json`, it must be served through a local web server to avoid CORS (Cross-Origin Resource Sharing) issues when opening the file directly.

### Using Python (3.x)
Python comes with a built-in HTTP server:
```bash
python3 -m http.server 8000
```

After running the command, open your browser and navigate to:
`http://localhost:8000`

### Using Node.js
If you have Node.js installed, you can use `npx` to run a server without installing it:
```bash
npx serve
```
*Note: This usually runs on `http://localhost:3000` or `http://localhost:5000`.*


## Printing to PDF

This resume is optimized for printing directly from the browser:

1. Open the resume in your browser (e.g., Chrome, Edge, or Firefox) via the local server.
2. Press `Ctrl + P` (or `Cmd + P` on Mac).
3. In the Print dialog:
   - **Destination:** Select "Save as PDF" or "Microsoft Print to PDF".
   - **Layout:** Portrait.
   - **Margins:** Set to "Default" or "None" (recommended "Default").
   - **Options:** Ensure "Background graphics" is checked if you want to preserve any background colors or icons.
   - Remove "Headers and Footers" in Options
4. Click **Save**.

## Project Structure
- `index.html`: The main structure and layout.
- `style.css`: All styling and print-specific media queries.
- `script.js`: Logic to fetch data from JSON and inject it into the DOM.
- `resume.json`: Your resume data.
