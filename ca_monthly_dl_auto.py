import os
import subprocess
import pyautogui
import time
import datetime

chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

def click_button(x, y):
    pyautogui.moveTo(x,y)
    time.sleep(1)
    pyautogui.click(x, y)
    time.sleep(1)  


def enter_date(date_str):  
    time.sleep(1)
    date_field_x = 1622
    date_field_y = 258
    pyautogui.moveTo(date_field_x,date_field_y)
    time.sleep(1) 
    pyautogui.click(date_field_x, date_field_y)
    pyautogui.write(date_str)
    time.sleep(1)  

def enter_date2(date_str):  
    time.sleep(1)
    date_field_x = 1608
    date_field_y = 409
    pyautogui.moveTo(date_field_x,date_field_y)
    time.sleep(1) 
    pyautogui.click(date_field_x, date_field_y)
    pyautogui.write(date_str)
    time.sleep(1)  


def enter_time(time_str):
    time.sleep(1)
    hour_field_x = 1565
    hour_field_y = 579
    minute_field_x = 1628
    minute_field_y = 580
    hours_str, minutes_str = time_str.split(':')

    pyautogui.moveTo(hour_field_x,hour_field_y)
    time.sleep(1)
    pyautogui.click(hour_field_x, hour_field_y)
    time.sleep(1)
    pyautogui.write(hours_str)
    time.sleep(1)
    pyautogui.moveTo(minute_field_x,minute_field_y)
    time.sleep(1)
    pyautogui.click(minute_field_x, minute_field_y)
    time.sleep(1)
    pyautogui.write(minutes_str)
    time.sleep(1)  

def enter_time2(time_str):
    time.sleep(1)
    hour_field_x = 1568
    hour_field_y = 737
    minute_field_x = 1628
    minute_field_y = 738
    hours_str, minutes_str = time_str.split(':')

    pyautogui.moveTo(hour_field_x,hour_field_y)
    time.sleep(1)
    pyautogui.click(hour_field_x, hour_field_y)
    time.sleep(1)
    pyautogui.write(hours_str)
    time.sleep(1)
    pyautogui.moveTo(minute_field_x,minute_field_y)
    time.sleep(1)
    pyautogui.click(minute_field_x, minute_field_y)
    time.sleep(1)
    pyautogui.write(minutes_str)
    time.sleep(1)  

def calculate_dates_for_month(year, month, start_time, increment_hours):
    current_date = datetime.datetime(year, month, 1)  
    end_date = datetime.datetime(year, month + 1, 1) if month < 12 else datetime.datetime(year + 1, 1, 1)  
    current_time = datetime.datetime.strptime(start_time, '%H:%M')  
    time.sleep(2)

    while current_date < end_date:
        end_date_1 = current_date + datetime.timedelta(hours=increment_hours)

        click_button(1869, 166)  
        click_button(1102, 255)  
        click_button(1015, 573)  
        click_button(1391, 253)  
        click_button(1390, 410)
        enter_date(current_date.strftime('%d/%m/%Y'))
        click_button(1761, 257)
        enter_time(start_time)
        click_button(1773, 582)
        click_button(1843, 253)

        if current_time.hour >= 18:
            current_date += datetime.timedelta(days=1)

        current_time += datetime.timedelta(hours=increment_hours)
        time.sleep(2)
        start_time = current_time.strftime('%H:%M')  

        click_button(1098, 417)
        click_button(1074, 730)
        enter_date2(current_date.strftime('%d/%m/%Y'))
        click_button(1758, 415)
        enter_time2(start_time)  
        click_button(1772, 741)
        click_button(1837, 413)
        click_button(1848, 299)

        click_button(1870, 167)
        click_button(1756, 299)


        file_name = f"{current_date.strftime('%Y-%m-%d %H_%M_%S')}.txt"

        if not os.path.exists(file_name):
            with open(file_name, "w") as file:
                pass  

        with open(file_name, 'a') as file:
            file.write(f"Start Date: {current_date.strftime('%d/%m/%Y')} {start_time}, End Date: {end_date_1.strftime('%d/%m/%Y')} {start_time}\n")

      
        time.sleep(5)  

year = 2024
month = 2  
start_time = '00:00'        
increment_hours = 6        

time.sleep(6)

calculate_dates_for_month(year, month, start_time, increment_hours)
