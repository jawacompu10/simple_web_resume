from playwright.sync_api import Page, expect


def test_edit_highlights_preview(page: Page, server: str):
    page.goto(server)

    # Create new profile
    page.get_by_text("Create New Profile").click()

    # Fill in highlights
    page.get_by_label("Key Achievements").fill(
        "Won Employee of the Month\nArchitected new testing platform"
    )
    page.get_by_label("Project Highlights").fill(
        "Migration to Playwright\nAPI automation coverage 90%"
    )

    # Check preview
    preview = page.locator("#resume-preview")

    # Key Achievements section should be visible and contain items
    expect(preview.locator("#key-achievements-section")).to_be_visible()
    expect(preview.locator("#key-achievements-list")).to_contain_text(
        "Won Employee of the Month"
    )
    expect(preview.locator("#key-achievements-list")).to_contain_text(
        "Architected new testing platform"
    )

    # Project Highlights section should be visible and contain items
    expect(preview.locator("#project-highlights-section")).to_be_visible()
    expect(preview.locator("#project-highlights-list")).to_contain_text(
        "Migration to Playwright"
    )
    expect(preview.locator("#project-highlights-list")).to_contain_text(
        "API automation coverage 90%"
    )


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
    expect(preview.locator("#project-highlights-section")).not_to_be_visible()


def test_highlights_preloaded_on_edit(page: Page, server: str):
    # 1. Create a profile with highlights
    page.goto(server)
    page.get_by_text("Create New Profile").click()

    page.locator("#form-name").fill("Preload Tester")
    page.locator("#form-keyAchievements").fill("Achievement 1\nAchievement 2")
    page.locator("#form-projectHighlights").fill("Project 1\nProject 2")

    # 2. Save the profile
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_text("Save Profile").first.click()

    # Wait for the profile to be saved and redirected to index
    expect(page).to_have_url(f"{server}/index.html")

    # 3. Go back to edit page for the profile
    page.get_by_title("Edit Profile").first.click()

    # Wait for data to load (form is wrapped in x-if=\"loaded\")
    page.wait_for_selector("#edit-profile-form")

    # 4. Check if the highlights are pre-loaded in the form
    key_achievements_val = page.locator("#form-keyAchievements").input_value()
    project_highlights_val = page.locator("#form-projectHighlights").input_value()

    assert "Achievement 1" in key_achievements_val
    assert "Achievement 2" in key_achievements_val
    assert "Project 1" in project_highlights_val
    assert "Project 2" in project_highlights_val
