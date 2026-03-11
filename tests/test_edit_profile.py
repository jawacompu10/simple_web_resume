from playwright.sync_api import Page, expect


def test_edit_profile_saves(page: Page, server: str):
    page.goto(server)
    page.get_by_text("Import resume.json").click()
    page.get_by_title("Edit Profile").first.click()

    # Wait for form to load
    expect(page.get_by_label("Name")).to_be_visible()

    # Change name
    page.get_by_label("Name").fill("John Doe")

    # Save (handle dialog first)
    page.on("dialog", lambda dialog: dialog.accept())
    page.locator(".save-profile-btn").click()

    # Wait for redirect to dashboard
    expect(page).to_have_url(server + "/")
    expect(page.get_by_text("John Doe")).to_be_visible()


def test_live_preview(page: Page, server: str):
    page.goto(server)
    page.get_by_text("Create New Profile").click()

    # Change name and check preview
    page.get_by_label("Name").fill("Jane Smith")

    # The preview should update (it has a delay in the form, but my manual updatePreview is faster)
    # Wait for the preview to contain Jane Smith
    expect(page.locator("#resume-preview")).to_contain_text("Jane Smith")


def test_add_remove_experience(page: Page, server: str):
    page.goto(server)
    page.get_by_text("Create New Profile").click()

    # Click Add Experience
    page.get_by_text("Add Experience").click()

    # Fill in experience
    page.locator('input[name="experience[0][title]"]').fill("Senior Developer")
    page.locator('input[name="experience[0][company]"]').fill("Tech Corp")

    # Check preview
    expect(page.locator("#resume-preview")).to_contain_text("Senior Developer")
    expect(page.locator("#resume-preview")).to_contain_text("Tech Corp")

    # Remove experience
    page.locator(".remove-exp-btn").click()

    # Check preview (should be gone)
    expect(page.locator("#resume-preview")).not_to_contain_text("Senior Developer")
