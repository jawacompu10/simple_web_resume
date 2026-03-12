from playwright.sync_api import Page, expect


def test_navbar_present(page: Page, server: str):
    page.goto(server)

    expect(page.get_by_text("Really Free Resumes")).to_be_visible()
    expect(page.get_by_text("Creator Corner:")).to_be_visible()

    # Check social links
    expect(page.get_by_title("LinkedIn")).to_have_attribute(
        "href", "https://www.linkedin.com/in/jawahar-vignesh-36418022/"
    )
    expect(page.get_by_title("GitHub Project")).to_have_attribute(
        "href", "https://github.com/jawacompu10/simple_web_resume"
    )


def test_hire_me_modal(page: Page, server: str):
    page.goto(server)

    # Click on "Work With Me" button
    page.get_by_text("Work With Me").click()

    # Check if modal is visible
    expect(page.get_by_text("Get in touch")).to_be_visible()
    expect(page.get_by_label("Name")).to_be_visible()
    expect(page.get_by_label("Email")).to_be_visible()
    expect(page.get_by_label("Message")).to_be_visible()

    # Fill out form
    page.get_by_label("Name").fill("Test User")
    page.get_by_label("Email").fill("test@example.com")
    page.get_by_label("Message").fill("This is a test message.")

    # Handle the alert that will pop up
    def handle_dialog(dialog):
        assert "Thanks! (This is a demo, no message was sent)" in dialog.message
        dialog.accept()

    page.on("dialog", handle_dialog)

    # Click send button
    page.get_by_text("Send Message").click()

    # Check if modal is closed
    expect(page.get_by_text("Get in touch")).not_to_be_visible()
