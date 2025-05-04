import time
import logging
from enum import Enum
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
import os
import uuid

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class LocatorType(Enum):
    """Enum for supported Selenium locator types."""
    XPATH = "xpath"
    ID = "id"


class GlobalFunctions:
    """A utility class for common Selenium WebDriver operations."""

    DEFAULT_TIMEOUT = 5  # Default timeout for WebDriverWait

    def __init__(self, driver):
        """Initialize with a Selenium WebDriver instance.

        Args:
            driver: Selenium WebDriver instance.
        """
        self.driver = driver

    def wait(self, seconds: float) -> None:
        """Pause execution for a specified number of seconds.

        Args:
            seconds: Number of seconds to wait.
        """
        time.sleep(seconds)

    def navigate_to(self, url: str, wait_seconds: float = 0) -> None:
        """Navigate to a specified URL.

        Args:
            url: The URL to navigate to.
            wait_seconds: Seconds to wait after navigation (default: 0).
        """
        self.driver.get(url)
        logger.info("Navigating to URL: %s", url)
        if wait_seconds > 0:
            self.wait(wait_seconds)

    def find_element(self, locator_type: LocatorType, selector: str) -> webdriver.WebElement:
        """Find an element by locator type and selector, scrolling it into view.

        Args:
            locator_type: The type of locator (XPATH or ID).
            selector: The selector string.

        Returns:
            WebElement: The located element.

        Raises:
            TimeoutException: If the element is not found within the timeout.
            ValueError: If the locator type is invalid.
        """
        by_type = By.XPATH if locator_type == LocatorType.XPATH else By.ID
        try:
            element = WebDriverWait(self.driver, self.DEFAULT_TIMEOUT).until(
                EC.visibility_of_element_located((by_type, selector))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            return self.driver.find_element(by_type, selector)
        except TimeoutException as ex:
            logger.error("Element not found: %s (%s)", selector, locator_type.value)
            raise ex
        except NoSuchElementException as ex:
            logger.error("Element not present: %s (%s)", selector, locator_type.value)
            raise ex

    def input_text(self, locator_type: LocatorType, selector: str, text: str, wait_seconds: float = 0) -> None:
        """Enter text into an input field.

        Args:
            locator_type: The type of locator (XPATH or ID).
            selector: The selector string.
            text: The text to input.
            wait_seconds: Seconds to wait after input (default: 0).

        Raises:
            TimeoutException: If the element is not found.
            ValueError: If the locator type is invalid.
        """
        try:
            element = self.find_element(locator_type, selector)
            element.clear()
            element.send_keys(text)
            logger.info("Entering text '%s' into element: %s (%s)", text, selector, locator_type.value)
            if wait_seconds > 0:
                self.wait(wait_seconds)
        except TimeoutException as ex:
            logger.error("Failed to input text into: %s (%s)", selector, locator_type.value)
            raise ex

    def click_element(self, locator_type: LocatorType, selector: str, wait_seconds: float = 0) -> None:
        """Click an element.

        Args:
            locator_type: The type of locator (XPATH or ID).
            selector: The selector string.
            wait_seconds: Seconds to wait after clicking (default: 0).

        Raises:
            TimeoutException: If the element is not found.
            ValueError: If the locator type is invalid.
        """
        try:
            element = self.find_element(locator_type, selector)
            element.click()
            logger.info("Clicking element: %s (%s)", selector, locator_type.value)
            if wait_seconds > 0:
                self.wait(wait_seconds)
        except TimeoutException as ex:
            logger.error("Failed to click: %s (%s)", selector, locator_type.value)
            raise ex

    def double_click(self, locator_type: LocatorType, selector: str, wait_seconds: float = 0.2) -> None:
        """Perform a double-click on an element.

        Args:
            locator_type: The type of locator (XPATH or ID).
            selector: The selector string.
            wait_seconds: Seconds to wait after action (default: 0.2).

        Raises:
            TimeoutException: If the element is not found.
            ValueError: If the locator type is invalid.
        """
        try:
            element = self.find_element(locator_type, selector)
            ActionChains(self.driver).double_click(element).perform()
            logger.info("Double-clicking element: %s (%s)", selector, locator_type.value)
            if wait_seconds > 0:
                self.wait(wait_seconds)
        except TimeoutException as ex:
            logger.error("Failed to double-click: %s (%s)", selector, locator_type.value)
            raise ex

    def right_click(self, locator_type: LocatorType, selector: str, wait_seconds: float = 0.2) -> None:
        """Perform a right-click on an element.

        Args:
            locator_type: The type of locator (XPATH or ID).
            selector: The selector string.
            wait_seconds: Seconds to wait after action (default: 0.2).

        Raises:
            TimeoutException: If the element is not found.
            ValueError: If the locator type is invalid.
        """
        try:
            element = self.find_element(locator_type, selector)
            ActionChains(self.driver).context_click(element).perform()
            logger.info("Right-clicking element: %s (%s)", selector, locator_type.value)
            if wait_seconds > 0:
                self.wait(wait_seconds)
        except TimeoutException as ex:
            logger.error("Failed to right-click: %s (%s)", selector, locator_type.value)
            raise ex

    def drag_and_drop(self, locator_type: LocatorType, source_selector: str, target_selector: str,
                      wait_seconds: float = 0.2) -> None:
        """Drag an element to another element.

        Args:
            locator_type: The type of locator (XPATH or ID).
            source_selector: The selector for the source element.
            target_selector: The selector for the target element.
            wait_seconds: Seconds to wait after action (default: 0.2).

        Raises:
            TimeoutException: If either element is not found.
            ValueError: If the locator type is invalid.
        """
        try:
            source = self.find_element(locator_type, source_selector)
            target = self.find_element(locator_type, target_selector)
            ActionChains(self.driver).drag_and_drop(source, target).perform()
            logger.info("Dragging element %s to %s (%s)", source_selector, target_selector, locator_type.value)
            if wait_seconds > 0:
                self.wait(wait_seconds)
        except TimeoutException as ex:
            logger.error("Failed to drag and drop: %s to %s (%s)", source_selector, target_selector, locator_type.value)
            raise ex

    def drag_and_drop_by_offset(self, locator_type: LocatorType, selector: str, x_offset: int, y_offset: int,
                                frame_index: int = None, wait_seconds: float = 0.2) -> None:
        """Drag an element to specified coordinates.

        Args:
            locator_type: The type of locator (XPATH or ID).
            selector: The selector for the element.
            x_offset: X-coordinate offset.
            y_offset: Y-coordinate offset.
            frame_index: Optional frame index to switch to (default: None).
            wait_seconds: Seconds to wait after action (default: 0.2).

        Raises:
            TimeoutException: If the element is not found.
            ValueError: If the locator type is invalid.
        """
        try:
            if frame_index is not None:
                self.driver.switch_to.frame(frame_index)
            element = self.find_element(locator_type, selector)
            ActionChains(self.driver).drag_and_drop_by_offset(element, x_offset, y_offset).perform()
            logger.info("Dragging element %s to coordinates (x: %s, y: %s) (%s)",
                        selector, x_offset, y_offset, locator_type.value)
            if wait_seconds > 0:
                self.wait(wait_seconds)
        except TimeoutException as ex:
            logger.error("Failed to drag and drop by offset: %s (%s)", selector, locator_type.value)
            raise ex
        finally:
            if frame_index is not None:
                self.driver.switch_to.default_content()

    def click_by_offset(self, locator_type: LocatorType, selector: str, x_offset: int, y_offset: int,
                        frame_index: int = None, wait_seconds: float = 0.2) -> None:
        """Click at specified coordinates relative to an element.

        Args:
            locator_type: The type of locator (XPATH or ID).
            selector: The selector for the element.
            x_offset: X-coordinate offset.
            y_offset: Y-coordinate offset.
            frame_index: Optional frame index to switch to (default: None).
            wait_seconds: Seconds to wait after action (default: 0.2).

        Raises:
            TimeoutException: If the element is not found.
            ValueError: If the locator type is invalid.
        """
        try:
            if frame_index is not None:
                self.driver.switch_to.frame(frame_index)
            element = self.find_element(locator_type, selector)
            ActionChains(self.driver).move_to_element_with_offset(element, x_offset, y_offset).click().perform()
            logger.info("Clicking at coordinates (x: %s, y: %s) relative to element %s (%s)",
                        x_offset, y_offset, selector, locator_type.value)
            if wait_seconds > 0:
                self.wait(wait_seconds)
        except TimeoutException as ex:
            logger.error("Failed to click by offset: %s (%s)", selector, locator_type.value)
            raise ex
        finally:
            if frame_index is not None:
                self.driver.switch_to.default_content()