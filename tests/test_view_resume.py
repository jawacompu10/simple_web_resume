import pytest
from playwright.sync_api import Page, expect

def test_view_resume(page: Page, server: str):
    page.goto(server)
    page.get_by_text("Import resume.json").click()
    
    # Click View
    page.get_by_title("View Resume").first.click()
    
    # Check if resume is rendered
    expect(page.get_by_text("Jawahar Vignesh")).to_be_visible()
    expect(page.get_by_text("Staff Software Development Engineer in Test")).to_be_visible()
    expect(page.get_by_text("PROFESSIONAL SUMMARY")).to_be_visible()
