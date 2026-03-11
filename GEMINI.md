Really Free Resumes - Local-First Architecture
We are building a purely static, local-first web application for managing resumes. This ensures zero hosting costs (can be hosted on GitHub Pages) and zero backend maintenance, while still keeping user data private and locally available.

Architecture & Tech Stack
HTML/CSS: Pure HTML5 and vanilla CSS for structure and styling.
Interactivity & State: Alpine.js. It provides React/Vue-like reactivity directly in HTML attributes, perfect for our component-less static approach.
Data Storage: LocalStorage or IndexedDB (via a simple wrapper like localforage or just native APIs since the data is small JSON).
Testing: Playwright for End-to-End (E2E) acceptance testing, adhering to the TDD requirement.
Proposed Changes
Core Structure
[NEW] index.html (Dashboard)
The landing page showing the list of available resume profiles.

Alpine component to read profiles from LocalStorage.
Links to create a new profile or edit an existing one.
[NEW] edit.html (Edit Page)
The form page to edit the JSON data for a specific profile.

Alpine component that loads the selected profile's data into form fields.
Auto-saves or has a save button that updates LocalStorage.
"View Resume" button.
[MODIFY] view.html (formerly index.html from original concept)
The page that actually renders the beautiful resume.

Takes a profile_id from the URL or local storage.
Reads the specific profile data.
Injects the data into the HTML structure.
Javascript/Logic Layer
[NEW] js/store.js
A simple utility script to handle saving and loading resume profiles to/from LocalStorage.

getProfiles()
getProfile(id)
saveProfile(profile)
deleteProfile(id)
[NEW] js/app.js
Alpine.js component definitions mapping to our pages.

Testing Layer
[NEW] tests/e2e/dashboard.spec.js
Playwright test to verify:

Empty state shows "No profiles yet".
Creating a new profile adds it to the list.
[NEW] tests/e2e/edit.spec.js
Playwright test to verify:

Form fields correctly update the underlying data object.
Data persists across page reloads.
[NEW] package.json & playwright.config.js
For installing and configuring Playwright.