import random
import time
import urllib.request
import win32api, win32con
import keyboard
import pygetwindow as gw
from PIL import ImageGrab
import numpy as np
import cv2
from tkinter import *
import tkinter.ttk as ttk

def AtoN(char):
    return ord(char) - 65

month = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06',
    'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
url = 'http://www.google.co.kr'
date = urllib.request.urlopen(url).headers['Date'][5:-4]
d, m, y, hour, min, sec = date[:2], month[date[3:6]], date[7:11], date[12:14], date[15:17], date[18:]
date_now = format(y, "04") + format(m, "02") + format(d, "02")
# upper codes are for check is password available
# password made simply mixed, added, and multiplied

pw = open('./password.txt', 'r')
data = pw.read().splitlines()
pw.close()
key = []
for word in data:
    key.append(word.split())

password = list(key[1][0])
for i in range(len(password)):
    password[i] = AtoN(password[i])

for i in range(len(password)):
    if password[19 - i] + i % 2 == 0:
        password[i] = 25 - password[i]

for i in range(len(password) // 2):
    password[i] = password[i] - password[19 - i]

temp = []
for i in range(4):
    temp.append([password[i*5 + 0], password[i*5 + 1], password[i*5 + 2], password[i*5 + 3], password[i*5 + 4]])
password = []
for i in range(20):
    password.append(temp[i%4][i//4])

pwa = password[:8]
pwb = password[8:16]
a = ""
b = ""
for i in range(len(pwa)):
    a = a + str(pwa[i])

for i in range(len(pwb)):
    b = b + str(pwb[i])

pwa = int(b) - int(a)
pwa = list(format(pwa, "04"))

for i in range(4):
    if pwa[i] != str(password[i+16]):
        quit()


class Location:
    def __init__(self, loc_x, loc_y):
        self.x = loc_x
        self.y = loc_y

    x: int
    y: int

if int(b) - int(date_now) < 0 or int(a) - int(date_now) > 0:
    quit()

# decoding the password and check is available
# if password was expired, end of code in here so lower code is never run

# lower code is x, y position in game. must be full screen or windowed full screen in 1920 x 1080.
void_Loc = Location(979, 927)   # location where void stone is
inven_Loc = Location(1272, 588) # location where inventory start position

# lower var is inventory slot location
loc_x = [1274, 1327, 1380, 1432, 1485, 1538, 1590, 1643, 1696, 1748, 1801, 1853]
loc_y = [608, 660, 713, 766, 818]

slot_list = [[Location(loc_x[i], loc_y[j]) for j in range(5)] for i in range(12)]

# lower var is quad-tap's slot location
loc_quad_x =[18, 44, 71, 97, 123, 150, 176, 202, 228, 255, 281, 307, 334, 360, 386, 413, 439, 465, 492, 518, 544, 571, 597, 623]
loc_quad_y =[129, 155, 181, 208, 234, 260, 287, 313, 339, 366, 392, 418, 444, 471, 497, 523, 550, 576, 602, 629, 655, 681, 708, 734]

slot_quad_list = [[Location(loc_quad_x[i], loc_quad_y[j]) for j in range(24)] for i in range(24)]

# lower images are allocated for img search
img_Sextant = cv2.imread("./image/Sextant.png", cv2.IMREAD_GRAYSCALE)
img_Stash = cv2.imread("./image/Stash.png", cv2.IMREAD_GRAYSCALE)
img_kirac = cv2.imread("./image/kirac.png", cv2.IMREAD_GRAYSCALE)
img_Compass = cv2.imread("./image/Compass.png", cv2.IMREAD_GRAYSCALE)
img_ChargedCompass = cv2.imread("./image/ChargedCompass.png", cv2.IMREAD_GRAYSCALE)
img_sextantempty = cv2.imread("./image/sextantempty.png", cv2.IMREAD_GRAYSCALE)
img_compassempty = cv2.imread("./image/compassempty.png", cv2.IMREAD_GRAYSCALE)
img_tapcur = cv2.imread("./image/tapcur.png", cv2.IMREAD_GRAYSCALE)
img_tapcuractive = cv2.imread("./image/tapcuractive.png", cv2.IMREAD_GRAYSCALE)
img_tap00 = cv2.imread("./image/tap00.png", cv2.IMREAD_GRAYSCALE)
img_tap01 = cv2.imread("./image/tap01.png", cv2.IMREAD_GRAYSCALE)
img_tap02 = cv2.imread("./image/tap02.png", cv2.IMREAD_GRAYSCALE)
img_tap03 = cv2.imread("./image/tap03.png", cv2.IMREAD_GRAYSCALE)

img_taps = [img_tap00, img_tap01, img_tap02, img_tap03]

img_sext8mod = cv2.imread("./image/sext_option/8mod.png", cv2.IMREAD_GRAYSCALE)
img_sextenraged = cv2.imread("./image/sext_option/enraged.png", cv2.IMREAD_GRAYSCALE)
img_sextbeyond = cv2.imread("./image/sext_option/beyond.png", cv2.IMREAD_GRAYSCALE)
img_sextharbinger = cv2.imread("./image/sext_option/harbinger.png", cv2.IMREAD_GRAYSCALE)
img_sextconqueror = cv2.imread("./image/sext_option/conqueror.png", cv2.IMREAD_GRAYSCALE)
img_sextshaper = cv2.imread("./image/sext_option/shaper.png", cv2.IMREAD_GRAYSCALE)
img_sextelder = cv2.imread("./image/sext_option/elder.png", cv2.IMREAD_GRAYSCALE)
img_sextchayula = cv2.imread("./image/sext_option/chayula.png", cv2.IMREAD_GRAYSCALE)
img_sextlifeforce = cv2.imread("./image/sext_option/lifeforce.png", cv2.IMREAD_GRAYSCALE)
img_sextgrove = cv2.imread("./image/sext_option/grove.png", cv2.IMREAD_GRAYSCALE)
img_sextrune = cv2.imread("./image/sext_option/rune.png", cv2.IMREAD_GRAYSCALE)
img_sextmirror = cv2.imread("./image/sext_option/mirror.png", cv2.IMREAD_GRAYSCALE)
img_sextdelirium = cv2.imread("./image/sext_option/delirium.png", cv2.IMREAD_GRAYSCALE)
img_sextcopybeast = cv2.imread("./image/sext_option/copybeast.png", cv2.IMREAD_GRAYSCALE)
img_sextgilded = cv2.imread("./image/sext_option/gilded.png", cv2.IMREAD_GRAYSCALE)
img_sextmagic = cv2.imread("./image/sext_option/magic.png", cv2.IMREAD_GRAYSCALE)
img_sextvaultcurrupt = cv2.imread("./image/sext_option/vaultcorrut.png", cv2.IMREAD_GRAYSCALE)
img_sextemblem = cv2.imread("./image/sext_option/emblem.png", cv2.IMREAD_GRAYSCALE)

img_sextunidentified = cv2.imread("./image/sext_option/unidentified.png", cv2.IMREAD_GRAYSCALE)
img_sextqualtorare = cv2.imread("./image/sext_option/qualtorare.png", cv2.IMREAD_GRAYSCALE)
img_sextraremapck = cv2.imread("./image/sext_option/raremapack.png", cv2.IMREAD_GRAYSCALE)
img_sextbossunique = cv2.imread("./image/sext_option/bossunique.png", cv2.IMREAD_GRAYSCALE)
img_sextbodyguard = cv2.imread("./image/sext_option/bodyguard.png", cv2.IMREAD_GRAYSCALE)
img_sextreflected = cv2.imread("./image/sext_option/reflected.png", cv2.IMREAD_GRAYSCALE)
img_sextalva = cv2.imread("./image/sext_option/alva.png", cv2.IMREAD_GRAYSCALE)
img_sexteinhar = cv2.imread("./image/sext_option/einhar.png", cv2.IMREAD_GRAYSCALE)
img_sextjun = cv2.imread("./image/sext_option/jun.png", cv2.IMREAD_GRAYSCALE)
img_syndicateintel = cv2.imread("./image/sext_option/syndicateintel.png", cv2.IMREAD_GRAYSCALE)
img_sextaltars = cv2.imread("./image/sext_option/altars.png", cv2.IMREAD_GRAYSCALE)
img_sextmetamorph = cv2.imread("./image/sext_option/metamorph.png", cv2.IMREAD_GRAYSCALE)
img_sextcatalysts = cv2.imread("./image/sext_option/catalysts.png", cv2.IMREAD_GRAYSCALE)
img_sextsmuggler = cv2.imread("./image/sext_option/smuggler.png", cv2.IMREAD_GRAYSCALE)
img_sextcontract = cv2.imread("./image/sext_option/contract.png", cv2.IMREAD_GRAYSCALE)
img_sextblight = cv2.imread("./image/sext_option/blight.png", cv2.IMREAD_GRAYSCALE)
img_sextoilstier = cv2.imread("./image/sext_option/oilstier.png", cv2.IMREAD_GRAYSCALE)
img_sextbreach = cv2.imread("./image/sext_option/breach.png", cv2.IMREAD_GRAYSCALE)
img_sextlegion = cv2.imread("./image/sext_option/legion.png", cv2.IMREAD_GRAYSCALE)
img_sextabyss = cv2.imread("./image/sext_option/abyss.png", cv2.IMREAD_GRAYSCALE)
img_sextexile = cv2.imread("./image/sext_option/exile.png", cv2.IMREAD_GRAYSCALE)
img_sexthunted = cv2.imread("./image/sext_option/hunted.png", cv2.IMREAD_GRAYSCALE)
img_sextunique = cv2.imread("./image/sext_option/unique.png", cv2.IMREAD_GRAYSCALE)
img_sextmap = cv2.imread("./image/sext_option/map.png", cv2.IMREAD_GRAYSCALE)
img_sextpolished = cv2.imread("./image/sext_option/polished.png", cv2.IMREAD_GRAYSCALE)
img_sextessence = cv2.imread("./image/sext_option/essence.png", cv2.IMREAD_GRAYSCALE)



img_sextquality = cv2.imread("./image/sext_option/quality.png", cv2.IMREAD_GRAYSCALE)

img_chosen = cv2.imread("./image/chosenCompass.png", cv2.IMREAD_GRAYSCALE)
img_none = cv2.imread("./image/noneChosen.png", cv2.IMREAD_GRAYSCALE)
img_empty = cv2.imread("./image/empty.png", cv2.IMREAD_GRAYSCALE)
img_miniempty = cv2.imread("./image/miniEmpty.png", cv2.IMREAD_GRAYSCALE)

# var for what mod is
img_sextMod = [
    img_sext8mod, img_sextenraged, img_sextbeyond, img_sextharbinger, img_sextconqueror, img_sextshaper, img_sextelder, img_sextchayula, img_sextlifeforce, img_sextgrove, img_sextrune, img_sextmirror, img_sextdelirium, img_sextcopybeast, img_sextgilded, img_sextmagic, img_sextquality, img_sextvaultcurrupt, img_sextemblem, img_sextunidentified, img_sextqualtorare, img_sextraremapck, img_sextbossunique, img_sextbodyguard, img_sextreflected, img_sextalva, img_sexteinhar, img_sextjun, img_syndicateintel, img_sextaltars, img_sextmetamorph, img_sextcatalysts, img_sextsmuggler, img_sextcontract, img_sextblight, img_sextoilstier, img_sextbreach, img_sextlegion, img_sextabyss, img_sextexile, img_sexthunted, img_sextunique, img_sextmap, img_sextpolished, img_sextessence
]

txt_sextMod = [
    "8 mod", "enraged", "beyond", "harbinger", "conqueror", "shaper", "elder", "chayula", "lifeforce", "grove", "rune", "mirror", "delirium", "copybeast", "gilded", "magic", "quality", "vaultcorrupt", "emblem", "unidentified", "qualtorare", "raremapack", "bossunique", "bodyguard", "reflected", "alva", "einhar", "jun", "intel", "altars", "metamorph", "catalysts", "smuggler", "contract", "blight", "oilstier", "breach", "legion", "abyss", "exile", "hunted", "unique", "map", "polished", "essence"
]

img_tapMod = [

]
txt_tapMod = [
    "8", "격앙", "이계", "선구자", "정복자", "쉐이퍼", "엘더", "생기"
]


def randomrange(min_max):
    return int(((random.random() - 1) * 2) * min_max)

# function for move mouse pointer to location x to x, y to y, in time in t
def move(x, y, t):
    start_x, start_y = win32api.GetCursorPos()
    for mouse_seq in range(100):
        win32api.SetCursorPos((int(x * (mouse_seq / 99) + start_x * ((99 - mouse_seq) / 99)),
                               int(y * (mouse_seq / 99) + start_y * ((99 - mouse_seq) / 99))))
        time.sleep(float((t / 100) * ((random.random() + 5) / 5)))

# similar to function move, move to position and click in the position and can set randomness
def click(x, y, z, min_delay, ran_range_x, ran_range_y):
    x = x + randomrange(ran_range_x)
    y = y + randomrange(ran_range_y)
    move(x, y, min_delay * ((random.random() / 2) + 1))
    time.sleep(min_delay * ((random.random() / 2) + 1))
    if z == 0:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        time.sleep(min_delay * ((random.random() / 2) + 1))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
        time.sleep(min_delay * ((random.random() / 2) + 1))
    if z == 1:
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
        time.sleep(min_delay * ((random.random() / 2) + 1))
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)
        time.sleep(min_delay * ((random.random() / 2) + 1))

# function when user click button start. this code will work for make selected sextant mode
# this code only can use sextant and chaos to buy compass
def start():
    window_seq = 0
    titles = gw.getAllTitles()
    for i in titles:
        if i == 'Path of Exile':
            break
        window_seq += 1

    # active Game window

    time.sleep(1)

    move(void_Loc.x, void_Loc.y, 1)

    windows = gw.getWindowsWithTitle(titles[window_seq])[0]
    windows.activate()
    label_status_cur.config(text="processing")

    time_start = time.time()

    used_sext = 0
    used_comp = 0
    num_option = [0 for i in range(len(txt_sextMod))]

    label_sext_num.config(text='0')
    label_comp_num.config(text='0')
    for i in range(len(label_option_cur)):
        label_option_cur[i].config(text='0')

    active_option =[]

    for i in range(len(txt_sextMod)):
        if chkvar_option[i].get() == 1:
            active_option.append(i)

    req_acc = float(label_accuracy_ent.get())/100
    cap_delay = float(label_capturedelay_ent.get())/1000
    click_delay = float(label_clickdelay_ent.get())/1000

    search_inven_seq_x = 10
    search_inven_seq_y = 4

    # upper code is just set up, clear variable

    print("proc start")

    keyboard.press('s')
    keyboard.release('s')
    keyboard.press('c')
    keyboard.release('c')
    keyboard.press('esc')
    keyboard.release('esc')
    # this is not essence. just clear your game screen


    time.sleep(1)

    pil_img = ImageGrab.grab((0, 0, 1920, 1080))
    np_img = np.array(pil_img)
    img_scr = cv2.cvtColor(np_img, cv2.COLOR_RGB2GRAY)
    # get game screen and convert images for process

    result = cv2.matchTemplate(img_scr, img_Stash, cv2.TM_SQDIFF_NORMED)
    stash_minVal, stash_maxVal, stash_minLoc, stash_maxLoc = cv2.minMaxLoc(result)
    stash_loc_x, stash_loc_y = stash_minLoc
    # compare game screen and image var. and get where is best fit
    # upper code are very many times appear

    click(stash_loc_x + 36, stash_loc_y + 11, 0, click_delay, 10, 5)

    time.sleep(1)

    pil_img = ImageGrab.grab((0, 0, 1920, 1080))
    np_img = np.array(pil_img)
    img_scr = cv2.cvtColor(np_img, cv2.COLOR_RGB2GRAY)
    img_shortStash = img_scr[100:808, 689:806]
    result = cv2.matchTemplate(img_shortStash, img_tapcuractive, cv2.TM_SQDIFF_NORMED)
    tapcur_minVal, tapcur_maxVal, tapcur_minLoc, tapcur_maxLoc = cv2.minMaxLoc(result)
    if tapcur_minVal > 0.01:
        result = cv2.matchTemplate(img_shortStash, img_tapcur, cv2.TM_SQDIFF_NORMED)
        tapcur_minVal, tapcur_maxVal, tapcur_minLoc, tapcur_maxLoc = cv2.minMaxLoc(result)
        tap_loc_x, tap_loc_y = tapcur_minLoc
        click(tap_loc_x + 50 + 689, tap_loc_y + 10 + 100, 0, click_delay, 10, 5)

    time.sleep(1)

    keyboard.press('g')
    keyboard.release('g')
    keyboard.press('i')
    keyboard.release('i')

    time.sleep(cap_delay)
    pil_img = ImageGrab.grab((0,0,1920,1080))

    search_sext = True
    is_repeat = True
    while is_repeat:
        if keyboard.is_pressed('f12'):
            label_status_cur.config(text="stopping")
            break

        # start search Sextant
        np_img = np.array(pil_img)
        img_scr = cv2.cvtColor(np_img, cv2.COLOR_RGB2GRAY)

        search_sext_seq = 0
        while True:
            if keyboard.is_pressed('f12'):
                is_repeat = False
                label_status_cur.config(text="stopping")
                break

            img_shortSext = img_scr[
                            slot_list[search_sext_seq // 5][search_sext_seq % 5].y:slot_list[search_sext_seq // 5][
                                                                                       search_sext_seq % 5].y + 31,
                            slot_list[search_sext_seq // 5][search_sext_seq % 5].x:slot_list[search_sext_seq // 5][
                                                                                       search_sext_seq % 5].x + 48]
            result = cv2.matchTemplate(img_shortSext, img_Sextant, cv2.TM_SQDIFF_NORMED)
            sext_minVal, sext_maxVal, sext_minLoc, sext_maxLoc = cv2.minMaxLoc(result)
            if sext_minVal < 0.8:
                search_sext = False
                break
            else:
                search_sext_seq += 1
                if search_sext_seq == 10:
                    search_sext_seq = 0
                    print("no sext")
                    keyboard.press('esc')
                    keyboard.release('esc')

                    time.sleep(cap_delay)

                    time.sleep(cap_delay)
                    pil_img = ImageGrab.grab((0, 0, 1920, 1080))
                    np_img = np.array(pil_img)
                    img_scr = cv2.cvtColor(np_img, cv2.COLOR_RGB2GRAY)

                    result = cv2.matchTemplate(img_scr, img_Stash, cv2.TM_SQDIFF_NORMED)
                    stash_minVal, stash_maxVal, stash_minLoc, stash_maxLoc = cv2.minMaxLoc(result)
                    stash_loc_x, stash_loc_y = stash_minLoc

                    click(stash_loc_x + 36, stash_loc_y + 11, 0, click_delay, 10, 5)

                    time.sleep(2)

                    pil_img = ImageGrab.grab((0, 0, 1920, 1080))
                    np_img = np.array(pil_img)
                    img_scr = cv2.cvtColor(np_img, cv2.COLOR_RGB2GRAY)
                    img_sextstash = img_scr[371:371 + 50, 413: 413 + 50]
                    result = cv2.matchTemplate(img_sextstash, img_sextantempty, cv2.TM_SQDIFF_NORMED)
                    sextempty_minVal, sextempty_maxVal, sextempty_minLoc, sextempty_maxLoc = cv2.minMaxLoc(result)

                    if sextempty_minVal < 0.1:
                        is_repeat = False
                        break

                    move(437, 396, click_delay)
                    time.sleep(.1)
                    keyboard.press('ctrl')
                    for i in range(10):
                        click(437, 396, 0, click_delay, 3, 3)

                    keyboard.release('ctrl')
                    keyboard.press('g')
                    keyboard.release('g')
                    keyboard.press('i')
                    keyboard.release('i')
                    break

        if not is_repeat:
            break
        # end search Sextant

        click(slot_list[search_sext_seq // 5][search_sext_seq % 5].x + 24,
              slot_list[search_sext_seq // 5][search_sext_seq % 5].y, 1, click_delay, 10, 10)
        click(void_Loc.x, void_Loc.y, 0, click_delay, 5, 5)
        used_sext += 1
        label_sext_num.config(text=str(used_sext))

        time.sleep(cap_delay)
        pil_img = ImageGrab.grab((0, 0, 1920, 1080))
        np_img = np.array(pil_img)
        img_scr = cv2.cvtColor(np_img, cv2.COLOR_RGB2GRAY)
        img_shortscr = img_scr[662:792, 874:1086]
        check_mod = True
        seq = 0
        sext_result = 0
        while check_mod:
            if keyboard.is_pressed('f12'):
                is_repeat = False
                label_status_cur.config(text="stopping")
                break

            result = cv2.matchTemplate(img_shortscr, img_sextMod[active_option[seq]], cv2.TM_SQDIFF_NORMED)
            sext_minVal, sext_maxVal, sext_minLoc, sext_maxLoc = cv2.minMaxLoc(result)

            if sext_minVal < req_acc:
                sext_result = 2
                check_mod = False
            else:
                if len(active_option) - seq == 1:
                    sext_result = 1
                    break
                else:
                    seq += 1

        if sext_result == 2:
            search_comp = True
            while search_comp:
                if keyboard.is_pressed('f12'):
                    is_repeat = False
                    label_status_cur.config(text="stopping")
                    break

                np_img = np.array(pil_img)
                img_scr = cv2.cvtColor(np_img, cv2.COLOR_RGB2GRAY)

                search_comp_seq = 0
                take_compass = False
                while True:
                    if keyboard.is_pressed('f12'):
                        is_repeat = False
                        label_status_cur.config(text="stopping")
                        break

                    img_shortCompass = img_scr[slot_list[11][search_comp_seq].y:slot_list[11][search_comp_seq].y + 31,
                                       slot_list[11][search_comp_seq].x:slot_list[11][search_comp_seq].x + 48]
                    result = cv2.matchTemplate(img_shortCompass, img_Compass, cv2.TM_SQDIFF_NORMED)
                    comp_minVal, comp_maxVal, comp_minLoc, comp_maxLoc = cv2.minMaxLoc(result)

                    if comp_minVal < 0.2:
                        click(slot_list[11][search_comp_seq].x + 24, slot_list[11][search_comp_seq].y, 1, click_delay,
                              10, 10)
                        click(void_Loc.x, void_Loc.y, 0, click_delay, 5, 5)

                        num_option[active_option[seq]] += 1
                        label_option_cur[active_option[seq]].config(text=str(num_option[active_option[seq]]))

                        used_comp += 1
                        label_comp_num.config(text=str(used_comp))
                        search_comp = False
                        break
                    else:
                        search_comp_seq += 1
                    if search_comp_seq == 5:
                        print("no comp")
                        take_compass = True

                    if take_compass:
                        skip_stash_comp = False
                        keyboard.press('esc')
                        keyboard.release('esc')

                        time.sleep(cap_delay)

                        pil_img = ImageGrab.grab((0, 0, 1920, 1080))
                        np_img = np.array(pil_img)
                        img_scr = cv2.cvtColor(np_img, cv2.COLOR_RGB2GRAY)
                        result = cv2.matchTemplate(img_scr, img_Stash, cv2.TM_SQDIFF_NORMED)
                        stash_minVal, stash_maxVal, stash_minLoc, stash_maxLoc = cv2.minMaxLoc(result)
                        stash_loc_x, stash_loc_y = stash_minLoc

                        click(stash_loc_x + 36, stash_loc_y + 11, 0, click_delay, 10, 10)

                        time.sleep(2)

                        pil_img = ImageGrab.grab((0, 0, 1920, 1080))
                        np_img = np.array(pil_img)
                        img_scr = cv2.cvtColor(np_img, cv2.COLOR_RGB2GRAY)
                        img_compstash = img_scr[643:643 + 50, 481: 481 + 50]
                        result = cv2.matchTemplate(img_compstash, img_compassempty, cv2.TM_SQDIFF_NORMED)
                        compempty_minVal, compempty_maxVal, compempty_minLoc, compempty_maxLoc = cv2.minMaxLoc(result)

                        if compempty_minVal < 0.2:
                            skip_stash_comp = True

                            search_tap = True
                            search_tap_seq = 0
                            while search_tap:
                                if search_tap_seq == 4:
                                    print('no tap')
                                    is_repeat = False
                                    search_inven = False
                                    label_status_cur.config(text="stopping")
                                    break

                                pil_img = ImageGrab.grab((0, 0, 1920, 1080))
                                np_img = np.array(pil_img)
                                img_scr = cv2.cvtColor(np_img, cv2.COLOR_RGB2GRAY)
                                img_shortStash = img_scr[100:808, 689:806]
                                result = cv2.matchTemplate(img_shortStash, img_taps[search_tap_seq],
                                                           cv2.TM_SQDIFF_NORMED)
                                tap_minVal, tap_maxVal, tap_minLoc, tap_maxLoc = cv2.minMaxLoc(result)
                                tap_loc_x, tap_loc_y = tap_minLoc
                                click(tap_loc_x + 50 + 689, tap_loc_y + 10 + 100, 0, click_delay, 10, 5)

                                time.sleep(1)
                                pil_img = ImageGrab.grab((0, 0, 1920, 1080))
                                np_img = np.array(pil_img)
                                img_scr = cv2.cvtColor(np_img, cv2.COLOR_RGB2GRAY)

                                quad_seq_x = 23
                                quad_seq_y = 23
                                quantity = 0
                                while True:
                                    img_shortTap = img_scr[
                                                   slot_quad_list[quad_seq_x][quad_seq_y].y:slot_quad_list[quad_seq_x][
                                                                                                quad_seq_y].y + 24,
                                                   slot_quad_list[quad_seq_x][quad_seq_y].x:slot_quad_list[quad_seq_x][
                                                                                                quad_seq_y].x + 24]
                                    result_chosen = cv2.matchTemplate(img_shortTap, img_chosen, cv2.TM_SQDIFF_NORMED)
                                    chosen_minVal, chosen_maxVal, chosen_minLoc, chosen_maxLoc = cv2.minMaxLoc(
                                        result_chosen)
                                    result_none = cv2.matchTemplate(img_shortTap, img_miniempty, cv2.TM_SQDIFF_NORMED)
                                    none_minVal, none_maxVal, none_minLoc, none_maxLoc = cv2.minMaxLoc(result_none)

                                    if chosen_minVal > none_minVal:
                                        quantity += 1
                                        if quantity == 45:
                                            search_tap = False
                                            break
                                    quad_seq_y -= 1
                                    if quad_seq_y == -1:
                                        quad_seq_y = 23
                                        quad_seq_x -= 1
                                        if quad_seq_x == -1:
                                            search_tap_seq += 1
                                            break

                            time.sleep(.1)

                            seq_x = 0
                            seq_y = 0
                            keyboard.press('ctrl')
                            while True:
                                img_shortInven = img_scr[slot_list[seq_x][seq_y].y - 18:slot_list[seq_x][seq_y].y + 32,
                                                 slot_list[seq_x][seq_y].x:slot_list[seq_x][seq_y].x + 50]
                                result_empty = cv2.matchTemplate(img_shortInven, img_empty, cv2.TM_SQDIFF_NORMED)
                                empty_minVal, empty_maxVal, empty_minLoc, empty_maxLoc = cv2.minMaxLoc(result_empty)

                                if empty_minVal > .9:
                                    click(slot_list[seq_x][seq_y].x + 25, slot_list[seq_x][seq_y].y + 7, 0, click_delay, 10, 10)

                                seq_y += 1
                                if seq_y == 5:
                                    seq_y = 0
                                    seq_x += 1
                                    if seq_x == 12:
                                        keyboard.release('ctrl')
                                        break

                            keyboard.press('esc')
                            keyboard.release('esc')

                            time.sleep(cap_delay)

                            pil_img = ImageGrab.grab((0, 0, 1920, 1080))
                            np_img = np.array(pil_img)
                            img_scr = cv2.cvtColor(np_img, cv2.COLOR_RGB2GRAY)
                            result = cv2.matchTemplate(img_scr, img_kirac, cv2.TM_SQDIFF_NORMED)
                            kirac_minVal, kirac_maxVal, kirac_minLoc, kirac_maxLoc = cv2.minMaxLoc(result)
                            kirac_loc_x, kirac_loc_y = kirac_minLoc
                            keyboard.press('ctrl')
                            click(kirac_loc_x + 50, kirac_loc_y + 11, 0, click_delay, 10, 5)
                            keyboard.release('ctrl')

                            time.sleep(2)

                            keyboard.press('ctrl')
                            keyboard.press('shift')
                            for i in range(60):
                                click(339, 389, 0, click_delay, 3, 3)

                            keyboard.release('shift')
                            keyboard.release('ctrl')

                            keyboard.press('esc')
                            keyboard.release('esc')

                            time.sleep(.2)

                            keyboard.press('esc')
                            keyboard.release('esc')

                            time.sleep(cap_delay)

                            pil_img = ImageGrab.grab((0, 0, 1920, 1080))
                            np_img = np.array(pil_img)
                            img_scr = cv2.cvtColor(np_img, cv2.COLOR_RGB2GRAY)
                            result = cv2.matchTemplate(img_scr, img_Stash, cv2.TM_SQDIFF_NORMED)
                            stash_minVal, stash_maxVal, stash_minLoc, stash_maxLoc = cv2.minMaxLoc(result)
                            stash_loc_x, stash_loc_y = stash_minLoc

                            click(stash_loc_x + 36, stash_loc_y + 11, 0, click_delay, 10, 5)

                            time.sleep(2)

                            pil_img = ImageGrab.grab((0, 0, 1920, 1080))
                            np_img = np.array(pil_img)
                            img_scr = cv2.cvtColor(np_img, cv2.COLOR_RGB2GRAY)
                            img_shortStash = img_scr[100:808, 689:806]
                            result = cv2.matchTemplate(img_shortStash, img_tapcur, cv2.TM_SQDIFF_NORMED)
                            tapcur_minVal, tapcur_maxVal, tapcur_minLoc, tapcur_maxLoc = cv2.minMaxLoc(result)
                            tap_loc_x, tap_loc_y = tapcur_minLoc
                            click(tap_loc_x + 50 + 689, tap_loc_y + 10 + 100, 0, click_delay, 10, 3)


                            seq_x = 0
                            seq_y = 0
                            for i in range(2):
                                click(slot_list[seq_x][seq_y].x + 25, slot_list[seq_x][seq_y].y + 7, 0, click_delay, 10, 10)
                                time.sleep(.5)
                                click(506, 668, 0, click_delay, 10, 10)
                                time.sleep(.5)
                                seq_y += 1
                            keyboard.press('ctrl')
                            while True:
                                click(slot_list[seq_x][seq_y].x + 25, slot_list[seq_x][seq_y].y + 7, 0, click_delay, 10, 10)
                                seq_y += 1
                                if seq_y == 5:
                                    seq_y = 0
                                    seq_x += 1
                                    if seq_x == 11:
                                        keyboard.release('ctrl')
                                        break

                            search_inven_seq_x = 10
                            search_inven_seq_y = 4

                        if not skip_stash_comp:
                            for take_compass_seq in range(5):
                                click(506, 667, 0, click_delay, 10, 10)
                                click(slot_list[11][take_compass_seq].x + 24, slot_list[11][take_compass_seq].y + 7, 0, click_delay, 10, 10)

                        keyboard.press('g')
                        keyboard.release('g')
                        keyboard.press('i')
                        keyboard.release('i')

                        move(void_Loc.x, void_Loc.y, click_delay)

                        time.sleep(.2)
                        pil_img = ImageGrab.grab((0,0,1920,1080))

                        np_img = np.array(pil_img)
                        img_scr = cv2.cvtColor(np_img, cv2.COLOR_RGB2GRAY)
                        search_comp_seq = 0
                        take_compass = False

            if not is_repeat:
                break


            if sext_result == 2:
                # start search inven
                time.sleep(cap_delay)
                pil_img = ImageGrab.grab((0, 0, 1920, 1080))

                np_img = np.array(pil_img)
                img_scr = cv2.cvtColor(np_img, cv2.COLOR_RGB2GRAY)
                reset_inven = False
                search_inven = True
                while search_inven:
                    if keyboard.is_pressed('f12'):
                        is_repeat = False
                        label_status_cur.config(text="stopping")
                        break

                    img_shortInven = img_scr[
                                     slot_list[search_inven_seq_x][search_inven_seq_y].y:slot_list[search_inven_seq_x][
                                                                                             search_inven_seq_y].y + 31,
                                     slot_list[search_inven_seq_x][search_inven_seq_y].x:slot_list[search_inven_seq_x][
                                                                                             search_inven_seq_y].x + 48]
                    result = cv2.matchTemplate(img_shortInven, img_ChargedCompass, cv2.TM_SQDIFF_NORMED)
                    inven_minVal, inven_maxVal, inven_minLoc, inven_maxLoc = cv2.minMaxLoc(result)
                    if inven_minVal > 0.999:
                        click(slot_list[search_inven_seq_x][search_inven_seq_y].x + 24,
                              slot_list[search_inven_seq_x][search_inven_seq_y].y + 7, 0, click_delay, 10, 10)
                        time.sleep(.1)
                        if search_inven_seq_y < 0:
                            search_inven_seq_x -= 1
                            search_inven_seq_y = 4
                        if search_inven_seq_x == 2 and search_inven_seq_y == 0:
                            print("no inven")
                            reset_inven = True
                        else:
                            break
                    else:
                        search_inven_seq_y -= 1
                        if search_inven_seq_y < 0:
                            search_inven_seq_x -= 1
                            search_inven_seq_y = 4
                            if search_inven_seq_x < 2:
                                print("no inven")
                                reset_inven = True

                    if reset_inven:
                        keyboard.press('esc')
                        keyboard.release('esc')

                        time.sleep(cap_delay)

                        pil_img = ImageGrab.grab((0,0,1920,1080))
                        np_img = np.array(pil_img)
                        img_scr = cv2.cvtColor(np_img, cv2.COLOR_RGB2GRAY)

                        result = cv2.matchTemplate(img_scr, img_Stash, cv2.TM_SQDIFF_NORMED)
                        stash_minVal, stash_maxVal, stash_minLoc, stash_maxLoc = cv2.minMaxLoc(result)
                        stash_loc_x, stash_loc_y = stash_minLoc
                        click(stash_loc_x + 36, stash_loc_y + 11, 0, click_delay, 10, 5)

                        time.sleep(2)

                        search_tap = True
                        search_tap_seq = 0
                        while search_tap:
                            if search_tap_seq == 4:
                                print('no tap')
                                is_repeat = False
                                search_inven = False
                                label_status_cur.config(text="stopping")
                                break

                            pil_img = ImageGrab.grab((0,0,1920,1080))
                            np_img = np.array(pil_img)
                            img_scr = cv2.cvtColor(np_img, cv2.COLOR_RGB2GRAY)
                            img_shortStash = img_scr[100:808, 689:806]
                            result = cv2.matchTemplate(img_shortStash, img_taps[search_tap_seq], cv2.TM_SQDIFF_NORMED)
                            tap_minVal, tap_maxVal, tap_minLoc, tap_maxLoc = cv2.minMaxLoc(result)
                            tap_loc_x, tap_loc_y = tap_minLoc
                            click(tap_loc_x + 50 + 689, tap_loc_y + 10 + 100, 0, click_delay, 10, 5)

                            time.sleep(1)
                            pil_img = ImageGrab.grab((0,0,1920,1080))
                            np_img = np.array(pil_img)
                            img_scr = cv2.cvtColor(np_img, cv2.COLOR_RGB2GRAY)

                            quad_seq_x = 23
                            quad_seq_y = 23
                            quantity = 0
                            while True:
                                img_shortTap = img_scr[
                                               slot_quad_list[quad_seq_x][quad_seq_y].y:slot_quad_list[quad_seq_x][
                                                                                            quad_seq_y].y + 24,
                                               slot_quad_list[quad_seq_x][quad_seq_y].x:slot_quad_list[quad_seq_x][
                                                                                            quad_seq_y].x + 24]
                                result_chosen = cv2.matchTemplate(img_shortTap, img_chosen, cv2.TM_SQDIFF_NORMED)
                                chosen_minVal, chosen_maxVal, chosen_minLoc, chosen_maxLoc = cv2.minMaxLoc(
                                    result_chosen)
                                result_none = cv2.matchTemplate(img_shortTap, img_miniempty, cv2.TM_SQDIFF_NORMED)
                                none_minVal, none_maxVal, none_minLoc, none_maxLoc = cv2.minMaxLoc(result_none)

                                if chosen_minVal > none_minVal:
                                    quantity += 1
                                    if quantity == 45:
                                        search_tap = False
                                        break
                                quad_seq_y -= 1
                                if quad_seq_y == -1:
                                    quad_seq_y = 23
                                    quad_seq_x -= 1
                                    if quad_seq_x == -1:
                                        search_tap_seq += 1
                                        break

                        time.sleep(cap_delay)

                        pil_img = ImageGrab.grab((0, 0, 1920, 1080))
                        np_img = np.array(pil_img)
                        img_scr = cv2.cvtColor(np_img, cv2.COLOR_RGB2GRAY)

                        input_inven_seq_x = 10
                        input_inven_seq_y = 4
                        while True:
                            if keyboard.is_pressed('f12'):
                                is_repeat = False
                                label_status_cur.config(text="stopping")
                                break
                            img_shortenInven = img_scr[slot_list[input_inven_seq_x][input_inven_seq_y].y:
                                                       slot_list[input_inven_seq_x][input_inven_seq_y].y + 31,
                                               slot_list[input_inven_seq_x][input_inven_seq_y].x:
                                               slot_list[input_inven_seq_x][input_inven_seq_y].x + 48]
                            result = cv2.matchTemplate(img_shortenInven, img_ChargedCompass, cv2.TM_SQDIFF_NORMED)
                            ininven_minVal, ininven_maxVal, ininven_minLoc, ininven_maxLoc = cv2.minMaxLoc(result)
                            keyboard.press('ctrl')
                            if ininven_minVal < 0.2:
                                click(slot_list[input_inven_seq_x][input_inven_seq_y].x + 24,
                                      slot_list[input_inven_seq_x][input_inven_seq_y].y + 7, 0, click_delay, 10, 10)

                            input_inven_seq_y -= 1
                            if input_inven_seq_y < 0:
                                input_inven_seq_x -= 1
                                input_inven_seq_y = 4

                            if input_inven_seq_x == 1:
                                keyboard.release('ctrl')
                                time.sleep(.1)
                                img_shortStash = img_scr[100:808, 689:806]
                                result = cv2.matchTemplate(img_shortStash, img_tapcur, cv2.TM_SQDIFF_NORMED)
                                tapcur_minVal, tapcur_maxVal, tapcur_minLoc, tapcur_maxLoc = cv2.minMaxLoc(result)
                                tap_loc_x, tap_loc_y = tapcur_minLoc
                                click(tap_loc_x + 50 + 689, tap_loc_y + 10 + 100, 0, click_delay, 10, 5)
                                search_inven_seq_x = 10
                                search_inven_seq_y = 4

                                time.sleep(.1)

                                keyboard.press('g')
                                keyboard.release('g')
                                keyboard.press('i')
                                keyboard.release('i')

                                time.sleep(cap_delay)

                                pil_img = ImageGrab.grab((0, 0, 1920, 1080))

                                print("reset complete")
                                search_inven = False
                                break
                # end search invent

        time_cur = time.time()
        time_gap = int(time_cur - time_start)
        spm = round(used_sext/((time_gap//60)+1), 2)
        cpm = round(used_comp / ((time_gap // 60) + 1), 2)
        label_spm_num.config(text=str(spm)+"/m")
        label_cpm_num.config(text=str(cpm)+"/m")
        label_time_num.config(text='{:02d}'.format(time_gap//3600) + ":" + '{:02d}'.format(time_gap//60) + ":" + '{:02d}'.format(time_gap%60))
        root.update()
    label_status_cur.config(text="ready")
    window_seq = 0
    titles = gw.getAllTitles()
    for i in titles:
        if i == 'sextant status':
            break
        window_seq += 1
    windows = gw.getWindowsWithTitle(titles[window_seq])[0]
    windows.activate()

def stop():
    label_status_cur.config(text="stopping")
    quit()

def cleanStash():
    window_seq = 0
    titles = gw.getAllTitles()
    for i in titles:
        if i == 'Path of Exile':
            break
        window_seq += 1

    time.sleep(1)

    move(void_Loc.x, void_Loc.y, 1)

    windows = gw.getWindowsWithTitle(titles[window_seq])[0]
    windows.activate()
    label_status_cur.config(text="processing")

    click_delay = float(label_clickdelay_ent.get()) / 1000

    print("proc start")

    keyboard.press('s')
    keyboard.release('s')
    keyboard.press('c')
    keyboard.release('c')
    keyboard.press('esc')
    keyboard.release('esc')

    time.sleep(1)

    pil_img = ImageGrab.grab((0, 0, 1920, 1080))
    np_img = np.array(pil_img)
    img_scr = cv2.cvtColor(np_img, cv2.COLOR_RGB2GRAY)
    result = cv2.matchTemplate(img_scr, img_Stash, cv2.TM_SQDIFF_NORMED)
    stash_minVal, stash_maxVal, stash_minLoc, stash_maxLoc = cv2.minMaxLoc(result)
    stash_loc_x, stash_loc_y = stash_minLoc

    click(stash_loc_x + 36, stash_loc_y + 11, 0, click_delay, 10, 5)

    time.sleep(1)

# this code using tkinter library.
root = Tk()
root.geometry("800x600")
root.title("sext machine")
root.option_add("*Font", "맑은고딕25")
root.resizable(False, False)
root.iconbitmap("./image/sext_icon.ico")

notebook = ttk.Notebook(root, width=800, height=600)
notebook.pack()

tab_status = ttk.Frame(root)
notebook.add(tab_status, text="status")
tab_sextantoption = ttk.Frame(root)
notebook.add(tab_sextantoption, text="sextant option")
tab_setting = ttk.Frame(root)
notebook.add(tab_setting, text="setting")

label_option = [0 for i in range (len(img_sextMod))]
label_option_cur = [0 for i in range (len(img_sextMod))]

    # start tab_status
        # first line
label_status = ttk.Label(tab_status)
label_status.config(text="status: ")
label_status.config(width=20)
label_status.place(x=10, y=10)

label_status_cur = ttk.Label(tab_status)
label_status_cur.config(text="ready")
label_status_cur.config(width=20)
label_status_cur.place(x=90, y=10)

label_time = ttk.Label(tab_status)
label_time.config(text="time: ")
label_time.config(width=20)
label_time.place(x=170, y=10)

label_time_num = ttk.Label(tab_status)
label_time_num.config(text="00:00:00")
label_time_num.config(width=20)
label_time_num.place(x=250, y=10)

label_spm = ttk.Label(tab_status)
label_spm.config(text="SpM: ")
label_spm.config(width=20)
label_spm.place(x=330, y=10)

label_spm_num = ttk.Label(tab_status)
label_spm_num.config(text="00:00:00")
label_spm_num.config(width=20)
label_spm_num.place(x=410, y=10)

btn_start = ttk.Button(tab_status)
btn_start.config(width=20)
btn_start.config(text="start")
btn_start.config(command=start)
btn_start.place(x=490, y=10)

        #second line
label_sext = ttk.Label(tab_status)
label_sext.config(text="sextant: ")
label_sext.config(width=20)
label_sext.place(x=10, y=35)

label_sext_num = ttk.Label(tab_status)
label_sext_num.config(text="0")
label_sext_num.config(width=20)
label_sext_num.place(x=90, y=35)

label_comp = ttk.Label(tab_status)
label_comp.config(text="compass: ")
label_comp.config(width=20)
label_comp.place(x=170, y=35)

label_comp_num = ttk.Label(tab_status)
label_comp_num.config(text="0")
label_comp_num.config(width=20)
label_comp_num.place(x=250, y=35)

label_cpm = ttk.Label(tab_status)
label_cpm.config(text="CpM: ")
label_cpm.config(width=20)
label_cpm.place(x=330, y=35)

label_cpm_num = ttk.Label(tab_status)
label_cpm_num.config(text="00:00:00")
label_cpm_num.config(width=20)
label_cpm_num.place(x=410, y=35)

btn_stop = ttk.Button(tab_status)
btn_stop.config(width=20)
btn_stop.config(text="stop")
btn_stop.config(command=stop)
btn_stop.place(x=490, y=35)

        #3 line
for i in range(len(txt_sextMod)):
    label_option[i] = ttk.Label(tab_status)
    label_option[i].config(text=str(txt_sextMod[i] + ": "))
    label_option[i].config(width=20)
    label_option[i].place(x=10+(i//24)*200, y=70+(i%24)*20)

    label_option_cur[i] = ttk.Label(tab_status)
    label_option_cur[i].config(text="0")
    label_option_cur[i].config(width=20)
    label_option_cur[i].place(x=110+(i//24)*200, y=70+(i%24)*20)

    # end tab_status

    # start tab_sextantoption
        #1 line
label_option_describe = ttk.Label(tab_sextantoption)
label_option_describe.config(text="sextant option list")
label_option_describe.config(width=40)
label_option_describe.place(x=10, y=10)

chkvar_option = [0 for i in range(len(txt_sextMod))]
chkbox_option = [0 for i in range(len(txt_sextMod))]

for i in range(len(txt_sextMod)):
    chkvar_option[i] = IntVar()
    if i < 19:
        chkvar_option[i].set(1)
    chkbox_option[i] = ttk.Checkbutton(tab_sextantoption, variable=chkvar_option[i], text=str(txt_sextMod[i]))
    chkbox_option[i].place(x=10+(i//24)*200, y=45+(i%24)*20)

    # end tab_sextantoption

    # start tap_setting
        # 1 line
label_accuracy = ttk.Label(tab_setting)
label_accuracy.config(text="accuracy: ")
label_accuracy.config(width=20)
label_accuracy.place(x=10, y=10)

label_accuracy_ent = ttk.Entry(tab_setting)
label_accuracy_ent.insert(0, 1)
label_accuracy_ent.config(width=20)
label_accuracy_ent.place(x=150, y=10)

        # 2 line
label_capturedelay = ttk.Label(tab_setting)
label_capturedelay.config(text="capture delay: ")
label_capturedelay.config(width=20)
label_capturedelay.place(x=10, y=35)

label_capturedelay_ent = ttk.Entry(tab_setting)
label_capturedelay_ent.insert(0, 100)
label_capturedelay_ent.config(width=20)
label_capturedelay_ent.place(x=150, y=35)

        # 3 line
label_clickdelay = ttk.Label(tab_setting)
label_clickdelay.config(text="click delay: ")
label_clickdelay.config(width=20)
label_clickdelay.place(x=10, y=60)

label_clickdelay_ent = ttk.Entry(tab_setting)
label_clickdelay_ent.insert(0, 40)
label_clickdelay_ent.config(width=20)
label_clickdelay_ent.place(x=150, y=60)
        # second line
# label_sext = ttk.Label(tab_setting)
# label_sext.config(text="sextant: ")
# label_sext.config(width=20)
# label_sext.place(x=10, y=35)
#
# label_sext_num = ttk.Label(tab_setting)
# label_sext_num.config(text="0")
# label_sext_num.config(width=20)
# label_sext_num.place(x=90, y=35)
    # end tap_setting

# btn = ttk.Button(tab1)
# btn.config(width=20)
# btn.config(text="버튼")
# btn.config(command=btnpress)
# btn.pack()

# btn = Button(root)
# btn.config(width=20, height=5)
# btn.config(padx=20, pady=20)
# btn.config(text="버튼")
# btn.config(fg="red", bg="yellow")
# btn.config(command=btnpress)
# btn.pack()

# ent = ttk.Entry(tab2)
# ent.config(width=30)
# ent.insert(0, "글자 입력가능")
# ent.pack()
#
# tl = ttk.Label(tab2)
# tl.config(text="글자를 보여줍니당")
# tl.pack()

# img = PhotoImage(file="파일 위치")
# tl = Label(root)
# tl.config(image=img)
# tl.pack()

# ent1 = Text(root)
# ent1.pack()
# ent.get()
# ent1.get("1.0", END)

# listbox = Listbox(root)
# listbox.config(selectmode="extended")
# listbox.config(height=0)
# listbox.insert(1, "python")
# listbox.insert(2, "C")
# listbox.insert(END, "java")
# listbox.pack()
#
# a = listbox.curselection()
# print(a)

# chkvar = IntVar()
# chkbox = ttk.Checkbutton(tab2, variable=chkvar)
# chkbox.config(text="체크해주세요")
# chkbox.pack()

# if chkvar.get() == 1:
#     print("checked")
#
# lang_var = StringVar() # str 형으로 변수 저장
# btn_lang1 = Radiobutton(tab2, text="Phython", value="Phython", variable=lang_var) # root라는 창에 "Phython"이라는 내용을 가지고 "Python"이라는 value값을 가진 라디오 버튼 생성
# btn_lang2 = Radiobutton(tab2, text="C", value="C", variable=lang_var)
# btn_lang3 = Radiobutton(tab2, text="JAVA", value="JAVA", variable=lang_var)
# btn_lang1.pack() # 라디오 버튼 배치
# btn_lang2.pack()
# btn_lang3.pack()
# print(lang_var.get())
#
# a=["python", "java", "c"]
# combobox = ttk.Combobox(tab2)
# combobox.config(height=5)
# combobox.config(values=a)
# combobox.config(state="readonly")
# combobox.set("select")
# combobox.pack()
#
# p_g = DoubleVar()
# pb = ttk.Progressbar(tab1)
# pb.config(maximum=100)
# pb.config(length=150)
# pb.config(variable=p_g)
# pb.pack()
#
# lb = Label(tab1)
# lb.pack()

root.mainloop()