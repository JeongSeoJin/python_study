import pyautogui
import time
import pyperclip

# Define the list of areas
area = ["런던","독일", "이탈리아"]

# Define the coordinates and dimensions of the screenshot area


# Move to the search bar
pyautogui.moveTo(400, 1070, 0.2)
pyautogui.click()
time.sleep(1)
# pyautogui.moveTo(700, 210, 0.2)
# pyautogui.click()
# time.sleep(1)

# pyperclip.copy("런던")
# pyautogui.hotkey("ctrl", "v")
# time.sleep(1)
# pyautogui.click()

i = 0
# Iterate over each area
for location in area:
    # Add " 날씨" (weather) to the location name
    location_with_weather = location + " 날씨"

    pyautogui.moveTo(400, 50, 0.2)
    pyautogui.click()
    time.sleep(1)


        # Copy the location name with "날씨" appended to clipboard
    pyperclip.copy("www.naver.com")
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)

    #     # Press enter to perform the search
    pyautogui.press("enter")
    time.sleep(1)

    # Move to the search bar
    pyautogui.moveTo(700, 210, 0.2)
    pyautogui.click()
    time.sleep(1)

    # Copy the location name with "날씨" appended to clipboard
    pyperclip.copy(location_with_weather)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)

    # Press enter to perform the search
    pyautogui.press("enter")
    time.sleep(1)

    # Take a screenshot of the specified area and save it with the location name
    pyautogui.screenshot("C://Users//pysuk//Documents//Coding// " + "weather{}.png".format(i), region = (400, 280, 750, 600))
    i += 1