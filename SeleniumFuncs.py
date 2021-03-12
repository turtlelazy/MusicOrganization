from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--headless")
youtube_search_heading = "https://www.youtube.com/results?search_query="


def getYoutubeVidID(searchQuery,driver):
    qURLForm = searchQuery.replace("+", "%2B")
    qURLForm = searchQuery.replace(" ", "+")
    driver.get(youtube_search_heading + qURLForm)
    videoAHref = driver.find_element_by_id("video-title")
    videoAHref = videoAHref.get_attribute('href')
    videoAHref = videoAHref[videoAHref.find("=") + 1:]
    return videoAHref

def getYoutubeVidIDsList(searchQueries):
    driver = webdriver.Chrome(chrome_options=chromeOptions)
    IdsList = []
    for searchQuery in searchQueries:
        IdsList.append(getYoutubeVidID(searchQuery,driver))
    driver.close()
    return IdsList



searchQueries = ["chungha"]

print(getYoutubeVidIDsList(searchQueries))