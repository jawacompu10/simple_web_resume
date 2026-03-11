import re
import pytest
from playwright.sync_api import Page, expect

def test_dashboard_loads(page: Page, server: str):
    page.goto(server)
    expect(page.get_by_text("Your Resume Profiles")).to_be_visible()
    expect(page.get_by_text("No profiles found")).to_be_visible()

def test_import_resume_json(page: Page, server: str):
    page.goto(server)
    
    # Click on import button
    page.get_by_text("Import resume.json").click()
    
    # Wait for the profile to appear in the list
    expect(page.get_by_text("Jawahar Vignesh")).to_be_visible()
    expect(page.get_by_text("Staff Software Development Engineer in Test")).to_be_visible()

def test_create_new_profile(page: Page, server: str):
    page.goto(server)
    
    # Click create new profile
    page.get_by_text("Create New Profile").click()
    
    # Should redirect to edit page
    expect(page).to_have_url(re.compile(r".*/edit/.*"))
    
    # Go back to dashboard and check if it's there
    page.goto(server)
    expect(page.get_by_text("New Profile", exact=True)).to_be_visible()
