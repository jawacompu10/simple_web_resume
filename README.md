# Simple Web Resume

A modern, responsive, and data-driven resume builder that stores data locally in your browser. This project is designed for easy customization, multiple profile management, and professional printing.

## Features
- **JSON Driven:** Update your resume content easily via a form or direct JSON edit.
- **Multiple Profiles:** Create and manage multiple resume profiles (e.g., SDE, QA, Manager) stored locally in IndexedDB.
- **Autosave:** Your changes are automatically saved as you type.
- **Live Preview:** See your changes in real-time as you edit your profile.
- **Print Optimized:** Styled specifically for "Save to PDF" to ensure a high-quality physical or digital document.
- **Local First:** Your data stays in your browser. No data is sent to any server.

## Tech Stack
- **Backend:** FastAPI (Python) - serves the application and partial templates.
- **Frontend:** Plain HTML, Tailwind CSS, Alpine.js.
- **Storage:** IndexedDB (via Dexie.js) - local storage in the browser.
- **Testing:** Playwright & Pytest.

## Setup & Running

### Prerequisites
- Python 3.13+
- `uv` (recommended) or `pip`

### Running Locally with `uv`
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/simple-web-resume.git
   cd simple-web-resume
   ```

2. **Run the application:**
   ```bash
   uv run python main.py
   ```

After running the command, open your browser and navigate to:
`http://localhost:8000`

### Running Locally with `pip`
1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python main.py
   ```

## Testing
The project uses Playwright for end-to-end testing.

1. **Install test dependencies:**
   ```bash
   uv pip install pytest-playwright
   playwright install
   ```

2. **Run tests:**
   ```bash
   uv run pytest
   ```

## Printing to PDF
This resume is optimized for printing directly from the browser:
1. Click the **PDF** button on the dashboard or **Print / Save PDF** on the view page.
2. In the Print dialog:
   - **Destination:** Select "Save as PDF".
   - **Margins:** Set to "Default".
   - **Options:** Ensure "Background graphics" is checked.
   - Remove "Headers and Footers".

## Project Structure
- `main.py`: FastAPI backend.
- `static/`: CSS, JS, and initial `resume.json`.
- `templates/`: Jinja2 templates for the dashboard, editor, and resume layout.
- `tests/`: End-to-End test suite.

## Acknowledgements
This project is built upon the amazing work of the open-source community. Special thanks to:

- [FastAPI](https://fastapi.tiangolo.com/) for the lightning-fast Python backend.
- [Alpine.js](https://alpinejs.dev/) for providing lightweight reactivity with minimal overhead.
- [Tailwind CSS](https://tailwindcss.com/) for making modern UI development a breeze.
- [Dexie.js](https://dexie.org/) for the elegant wrapper around IndexedDB.
- [HTMX](https://htmx.org/) for allowing high-power tools directly in HTML.
- [Playwright](https://playwright.dev/) and [Pytest](https://docs.pytest.org/) for the robust testing ecosystem.
- [Font Awesome](https://fontawesome.com/) for the beautiful icons.
- [Google Fonts](https://fonts.google.com/) for the professional typography.
- All our contributors and the broader open-source community!
