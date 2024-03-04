import pyautogui
import time
from datetime import datetime
import calendar
import pyperclip
# 본 프로그램은 투표 제목란에 마우스를 클릭 및 위치하고 실행하여야 함.

# 해당 년도의 월별 마지막 날짜 알기
lastDays = []
for i in range(1, 13):
    cal = calendar.month(2024, i)
    lastDays.append(int(cal.replace('\n', '')[-2:]))
    
# 현재 날짜 얻기
today = datetime.now().date()


x, y = pyautogui.position() # 현재 마우스 위치의 좌표를 얻기
print(f"현재 마우스 위치: x={x}, y={y}")

# 키보드 입력
pyperclip.copy(f'{today}, 청소 날짜 정하기')
pyautogui.hotkey('ctrl', 'v')
# 마우스 이동 및 클릭
pyautogui.click(x, y+250)




for i in range(0, 25):

    if i == 2:
        pyautogui.scroll(-500)
        pyautogui.click(x, y-250)
    elif i == 8:
        pyautogui.scroll(-500)
        x, y = pyautogui.position()
        pyautogui.click(x, y-243)
    elif i == 12:
        pyautogui.scroll(-500)
        x, y = pyautogui.position()
        pyautogui.click(x, y-243)
    elif i == 17:
        pyautogui.scroll(-500)
        x, y = pyautogui.position()
        pyautogui.click(x, y-243)
    elif i == 22:
        pyautogui.scroll(-500)
        x, y = pyautogui.position()
        pyautogui.click(x, y-243)
    x, y = pyautogui.position() # 현재 마우스 위치의 좌표를 얻기
    pyautogui.click(x, y+49)

pyautogui.scroll(2000)    
x, y = pyautogui.position()
pyautogui.click(x, y-44)

# 날짜 입력
month = int(today.month)
day = (today.day)
bull = False
print(x, y)
for i in range(0, 30):
    pass
    if bull==False:
        bull = True
        pyperclip.copy(f"{month}-{day}-오전")
        pyautogui.hotkey('ctrl', 'v')
    elif bull==True:
        bull = False
        pyperclip.copy(f"{month}-{day}-오후")
        pyautogui.hotkey('ctrl', 'v')
        day += 1
    # 해당 월의 마지막날 이후에는 - month에 1 더하고 / day를 1로 초기화
    if day == lastDays[month-1]:
        month += 1
        day = 1
    pyautogui.press('tab')
    pyautogui.press('tab')
