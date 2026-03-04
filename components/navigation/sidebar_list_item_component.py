from typing import Pattern

from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.image import Image
from elements.text import Text


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)
        self.identifier = identifier
        self.icon = Image(page, "{identifier}-drawer-list-item-icon", "Icon")
        self.title = Text(page, "{identifier}-drawer-list-item-title-text", "Title")
        self.button = Button(page, "{identifier}-drawer-list-item-button", "Button")

    def check_visible(self, title: str):
        self.icon.check_visible(identifier=self.identifier)

        self.title.check_visible(identifier=self.identifier)
        self.title.check_have_text(title, identifier=self.identifier)

        self.button.check_visible(identifier=self.identifier)

    def navigate(self, expected_url: Pattern[str]):
        self.button.click()
        self.check_current_url(expected_url)
