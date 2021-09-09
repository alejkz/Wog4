def test_scores_service(URL):
from selenium import webdriver

driver = webdriver.Chrome(executable_path="~/Desktop/ChromeDriver")
driver.get(URL)
score_element = driver.find_element_by_name("score")
if score_element >= 1 or score_element <= 1000:
    return True
else:
    return False


def main_function():

    URL = input("Enter a URL")
    if test_scores_service(URL) == True:
        return 0
    else:
        return -1


