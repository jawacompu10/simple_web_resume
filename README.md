# Really Free Resumes

A modern, responsive, and data-driven resume builder that stores data locally in your browser. This project is designed for easy customization, multiple profile management, and professional printing. **No backend required.**

## Features
- **JSON Driven:** Update your resume content easily via a form or direct JSON edit.
- **Multiple Profiles:** Create and manage multiple resume profiles (e.g., SDE, QA, Manager) stored locally in IndexedDB.
- **Autosave:** Your changes are automatically saved as you type (can be toggled).
- **Live Preview:** See your changes in real-time as you edit your profile.
- **Print Optimized:** Styled specifically for "Save to PDF" to ensure a high-quality physical or digital document.
- **Local First & Private:** Your data stays in your browser. No data is sent to any server.
- **Offline Ready**: Works completely without a server.

## Tech Stack
- **Frontend:** Plain HTML, Tailwind CSS, Alpine.js.
- **Components**: Native Web Components for shared UI (Navbar, Modals).
- **Storage:** IndexedDB (via Dexie.js) - local storage in the browser.
- **No Dependencies**: All libraries are hosted locally in `static/vendor`.

## Setup & Running

This is a **purely static application**. You don't need to install any backend dependencies.

### Running Locally
To avoid CORS issues and keep your project files secure, serve the `public` directory:

**Using Python:**
```bash
python3 -m http.server 8000 --directory public
```

**Using Node.js:**
```bash
npx serve public
```

After running the command, open `http://localhost:8000` in your browser.

## Deployment
This app is perfect for **Netlify**, **GitHub Pages**, or **Vercel**. Just upload the repository or the files in the root directory.

## Acknowledgements
This project is built upon the amazing work of the open-source community. Special thanks to:

- [Alpine.js](https://alpinejs.dev/) for providing lightweight reactivity.
- [Tailwind CSS](https://tailwindcss.com/) for modern UI development.
- [Dexie.js](https://dexie.org/) for the elegant wrapper around IndexedDB.
- [Font Awesome](https://fontawesome.com/) for the beautiful icons.
- [Google Fonts](https://fonts.google.com/) for the professional typography.
- [Formspree](https://formspree.io/) for power the contact form without a backend.

## Compliance
This site is powered by [Netlify](https://www.netlify.com).
