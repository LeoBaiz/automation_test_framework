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