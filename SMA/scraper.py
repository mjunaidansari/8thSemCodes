from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in background (optional)
driver = webdriver.Chrome(options=options)

# Open the Audemars Piguet website
url = "https://www.audemarspiguet.com/com/en/watch-collection.html?_gl=1*1596jdz*_up*MQ..*_gs*MQ..&gclid=Cj0KCQiAkoe9BhDYARIsAH85cDOGxBJpHzE0WHpN8-hahcDtgny8swhhTPdodwSkG9DcASjbhsEktfQaAujtEALw_wcB"
driver.get(url)
time.sleep(5)  # Wait for JavaScript to load

# Extract Watch Names (Modify selector as needed)
watches = driver.find_elements(By.CLASS_NAME, "ap-watch-card__wrapper")  # Change class name if necessary
watch_names = [watch.text for watch in watches if watch.text.strip()]

# Close the driver
driver.quit()

# Save to CSV
df = pd.DataFrame({"Watch Name": watch_names})
df.to_csv("audemars_piguet_watches.csv", index=False)

print("Scraping completed! Data saved in 'audemars_piguet_watches.csv'.")
