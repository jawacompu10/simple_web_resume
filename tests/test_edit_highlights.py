import pytest
from playwright.sync_api import Page, expect

def test_edit_highlights_preview(page: Page, server: str):
    page.goto(server)
    
    # Create new profile
    page.get_by_text("Create New Profile").click()
    
    # Fill in highlights
    page.get_by_label("Key Achievements").fill("Won Employee of the Month\nArchitected new testing platform")
    page.get_by_label("Project Highlights").fill("Migration to Playwright\nAPI automation coverage 90%")
    
    # Check preview
    preview = page.locator("#resume-preview")
    
    # Key Achievements section should be visible and contain items
    expect(preview.locator("#key-achievements-section")).to_be_visible()
    expect(preview.locator("#key-achievements-list")).to_contain_text("Won Employee of the Month")
    expect(preview.locator("#key-achievements-list")).to_contain_text("Architected new testing platform")
    
    # Project Highlights section should be visible and contain items
    expect(preview.locator("#project-highlights-section")).to_be_visible()
    expect(preview.locator("#project-highlights-list")).to_contain_text("Migration to Playwright")
    expect(preview.locator("#project-highlights-list")).to_contain_text("API automation coverage 90%")

def test_highlights_sections_hide_when_empty(page: Page, server: str):
    page.goto(server)
    
    # Create new profile
    page.get_by_text("Create New Profile").click()
    
    preview = page.locator("#resume-preview")
    
    # Sections should be hidden initially
    expect(preview.locator("#key-achievements-section")).not_to_be_visible()
    expect(preview.locator("#project-highlights-section")).not_to_be_visible()
    
    # Fill and check visibility
    page.get_by_label("Key Achievements").fill("Something")
    expect(preview.locator("#key-achievements-section")).to_be_visible()
    
    # Clear and check hidden
    page.get_by_label("Key Achievements").fill("")
    expect(preview.locator("#key-achievements-section")).not_to_be_visible()
