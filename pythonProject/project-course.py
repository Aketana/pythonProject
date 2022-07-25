import sys
from tkinter import Tk, simpledialog, messagebox

def read_from_file():
    with open('venv/worldcapital.txt', 'r') as file:
        for line in line:
            line = line.rstrip('\n')
            country, capital = line.split('/') #สัญลักษณ์ ที่ใช้แยก ระหว่าง country กับ capital
            country = country.capitalize()
            capital = capital.capitalize()
            world_capital[country] = capital #แสดงผลให้เป็น capital ทั้งหมด

def write_to_file(country_name, capital_name):
    with open('venv/worldcapital.txt', 'a') as file:
        file.write('\n')
        file.write(country_name + '/' + capital_name)
        file.close()

root = Tk()
root.withdraw() #ปิดหน้าต่าง tk
world_capital = {}
while True:
    read_from_file()
    simpledialog.askstring
    query.country = ''
    query_country = simpledialog.askstring('Country', 'Type the name of a country: ')
    query_country = query_country.capitalize()
    if query_country in world_capital:
        result = world_capital[query_country]
        messagebox.showinfo('Answer', 'The capital city of ' + query_country + ' is ' + result + '!')
    else:
        new_capital = simpledialog.askstring('Teach me', 'I don\'t know the answer. What is the capital city of ' + query_country + '?:')
        messagebox.showinfo('Thanks', 'Thank you for teaching me')
        new_capital = new_capital.capitalize()
        write_to_file(query_country, new_capital)
    answer = simpledialog.askstring('Continue', 'Do you want to try again? y/n: ')
        if answer == 'n':
            messagebox.showinfo('Thanks', 'Thank you for playing!')
            root.destroy()
            sys.exit()