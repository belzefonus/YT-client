from colorama import Fore, Style
from bs4 import BeautifulSoup
import requests
import os

os.chdir(r"C:\Users\sarkd\OneDrive\Documents\Python\YouTubeClient")

def search():
  a = input('\nSearch: ')
  a.replace(' ', '+')
  r = requests.get('https://yewtu.be/search?q=' + a)
  r = BeautifulSoup(r.content, 'html.parser')
  videos = r.find_all('a', style = 'width:100%')
  times = r.find_all('p', class_ = 'length')
  chn = r.find_all('p', class_ = 'channel-name')
  dat = r.find_all('p', class_ = 'video-data')
  a = 1
  b = 0
  lst = []
  for v in videos:
    lst.append(v['href'][9:])
    i = v.find('p', dir = 'auto')
    print(Fore.WHITE + '{}. {}    [{}]'.format(a, i.text, times[a-1].text))
    print(Fore.RED + chn[a-1].text)
    print(Style.RESET_ALL + dat[b].text)
    print(dat[b+1].text)
    print('======')
    a = a + 1
    b += 2
    if a == 31:
      break
  a = int(input('Enter the number of the video you want to watch: '))
  comand = 'mpv https://yewtu.be/watch?v=' + lst[a-1]
  os.system(comand)

def subscribtions():
  s = open("subs.txt")
  s = s.readlines()
  channels = []
  a = 1
  for i in s:
    r = requests.get('https://yewtu.be/channel/' + i.strip())
    r = BeautifulSoup(r.content, 'html.parser')
    logo = r.find('div', class_ = 'channel-profile')
    name = logo.find('span')
    channels.append('{}.{}'.format(a, name.text))
    a += 1
  for i in channels:
    print(i)
  a = int(input('\nEnter the number of the channel you want to visit: '))
  print('\n')
  r = requests.get('https://yewtu.be/channel/' + s[a-1].strip())
  r = BeautifulSoup(r.content, 'html.parser')
  videos = r.find_all('a', style = 'width:100%')
  times = r.find_all('p', class_ = 'length')
  dat = r.find_all('p', class_ = 'video-data')
  a = 1
  b = 0
  lst = []
  for v in videos:
    lst.append(v['href'][9:])
    i = v.find('p', dir = 'auto')
    print(Fore.WHITE + '{}. {}    [{}]'.format(a, i.text, times[a-1].text))
    print(Style.RESET_ALL + dat[b].text)
    print(dat[b+1].text)
    print('======')
    a = a + 1
    b += 2
  a = int(input('Now, enter the number of the video you would like to watch: '))
  comand = 'mpv https://yewtu.be/watch?v=' + lst[a-1]
  os.system(comand)

while True:
  a = input('\nType search or subs: ')
  if a == 'search':
    search()
  elif a == 'subs':
    subscribtions()
  else:
    print('See ya')
    break