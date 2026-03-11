import pytest
from playwright.sync_api import Page, expect

def test_autosave_persists_on_refresh(page: Page, server: str):
    page.goto(server)
    
    # Create new profile
    page.get_by_text("Create New Profile").click()
    
    # Wait for form
    page.wait_for_selector("#form-name")
    
    # Fill in some data
    page.get_by_label("Name").fill("Autosave Tester")
    page.get_by_label("Title").fill("Persistence Engineer")
    
    # Wait for autosave to trigger (debounce is 1.5s)
    # We look for the visual indicator
    expect(page.get_by_text("AUTOSAVED")).to_be_visible(timeout=5000)
    
    # Refresh the page
    page.reload()
    
    # Wait for form to re-render from DB
    page.wait_for_selector("#form-name")
    
    # Check if data persisted
    expect(page.get_by_label("Name")).to_have_value("Autosave Tester")
    expect(page.get_by_label("Title")).to_have_value("Persistence Engineer")
    
    # Check preview too
    preview = page.locator("#resume-preview")
    expect(preview.locator("#name")).to_have_text("Autosave Tester")
