import sys
from PIL import Image, ImageDraw, ImageFont
import pandas as pd

data = pd.read_excel('data.xlsx')

#print(data)

character_info = data.values.tolist()

img = Image.new('RGBA', [2340, 1080], (255, 0, 0, 0))
draw = ImageDraw.Draw(img)
skill_font = ImageFont.truetype("arial.ttf", 25, encoding="unic")
skill_title_font = ImageFont.truetype("arial.ttf", 15, encoding="unic")
gun_font = ImageFont.truetype("arial.ttf", 20, encoding="unic")
gear_font = ImageFont.truetype("arial.ttf", 20, encoding="unic")

x_anchor=250
y_anchor=235

k=10

main_x=x_anchor
main_y=y_anchor

type = ""
icon = ""
place = [(main_x,main_y),(main_x+115,main_y+125)]
wp_icon = ""
wp_tier = 0
gear_type = ""
gear_tier = ""
gear_place = [[0,0],[0,0]]
title = ["Ex","Basic","Enhanced","Sub"]

next_down = 130
next_right = 465

pos = [1,2,3,4,5,6]

def Reset_x():
    global main_x
    main_x=x_anchor

def Reset_y():
    global main_y
    main_y=y_anchor

def Paint_skill(type, icon, skill_lvl, skill_title):
    place = [(main_x,main_y),(main_x+115,main_y+120)]
    line_place = [(main_x+106,main_y+96),(main_x+9,main_y+96)]
    bg_place = [(main_x+63,main_y+31),(main_x+52,main_y+31),(main_x+29,main_y+46),(main_x+29,main_y+76),(main_x+52,main_y+91),(main_x+63,main_y+91),(main_x+86,main_y+76),(main_x+86,main_y+46)]
    icon_place = (main_x+28,main_y+32)
    skill_lv_place = (main_x+58,main_y+99)
    skill_icon = Image.open(r'skill_icons'+"/"+icon+".png")
    draw.rounded_rectangle(place, radius=10, fill="white", outline="grey", width=2, corners=None)
    draw.line(line_place, fill="grey", width=2)
    draw.polygon(bg_place, fill=type, outline=None, width=None)
    img.paste(skill_icon,icon_place, skill_icon)
    draw.text(skill_lv_place, "Lv. "+str(skill_lvl), fill=type, anchor="mt", font=skill_font)
    draw.text((main_x+58,main_y+15), skill_title+" Skill", fill=type, anchor="mm", font=skill_title_font)

def Paint_gun(wp_icon, place, tier, wp_lvl):
    i_place = [(place[0][0],place[0][1]-97),(place[0][0]+340,place[0][1]-10)]
    icon_place = (place[0][0],place[0][1]-97)
    gun_icon = Image.open(r'gun_icons'+"/Weapon_Icon_"+wp_icon+".png")
    draw.rounded_rectangle(i_place, radius=10, fill="azure", outline="grey", width=2, corners=None)
    img.paste(gun_icon, icon_place, gun_icon)
    draw.rounded_rectangle(((i_place[1][0]-120,i_place[1][1]-30), i_place[1]), radius=10, fill="white", outline="grey", width=2, corners=(True, False, True, False))
    tier_place=(place[0][0]+320,place[0][1]-30)
    for w in range(tier):
        img.paste(Image.open("Star_Icon.webp"), tier_place, Image.open("Star_Icon.webp"))
        tier_place=(place[0][0]+305-(w*15),place[0][1]-30)
    tier_place=(place[0][0]+320-90,place[0][1]-30)
    draw.text(tier_place, "Lv. "+str(wp_lvl), fill="blue", anchor="lt", font=gun_font)

def Paint_gear(gear_tier, gear_place, gear_type, gear_lvl):
    gear_icon = Image.open(r'gear_icons'+"/equipment_icon_"+gear_type+"_tier"+str(gear_tier)+".webp")
    gear_icon = gear_icon.resize((146,116))
    draw.rounded_rectangle(gear_place, radius=10, fill="azure", outline="grey", width=2, corners=None)
    img.paste(gear_icon, (gear_place[0][0]-5,gear_place[0][1]), gear_icon)
    draw.rounded_rectangle((gear_place[0],(gear_place[0][0]+35,gear_place[0][1]+24)), radius=10, fill="white", outline="grey", width=2, corners=(True, False, True, False))
    draw.rounded_rectangle(((gear_place[0][0],gear_place[1][1]-25),(gear_place[0][0]+65,gear_place[1][1])), radius=10, fill="white", outline="grey", width=2, corners=(False, True, False, True))
    draw.text((gear_place[0][0]+5,gear_place[0][1]+5), "T"+str(gear_tier), fill="blue", anchor="lt", font=gear_font)
    draw.text((gear_place[0][0]+5,gear_place[1][1]-5), "Lv. "+str(gear_lvl), fill="blue", anchor="lb", font=gear_font)

def Paint_UI(UI_tier, UI_place, UI_icon):
    UI_icon = Image.open(r'unique_item_icon/'+UI_icon+"_UI.webp")
    UI_icon = UI_icon.resize((50,39))
    draw.rounded_rectangle(UI_place, radius=10, fill="cornsilk", outline="grey", width=2, corners=None)
    img.paste(UI_icon, (UI_place[0][0]+20,UI_place[0][1]+10), UI_icon)
    draw.rounded_rectangle((UI_place[0],(UI_place[0][0]+35,UI_place[0][1]+24)), radius=10, fill="white", outline="grey", width=2, corners=(True, False, True, False))
    draw.text((UI_place[0][0]+5,UI_place[0][1]+5), "T"+str(UI_tier), fill="blue", anchor="lt", font=gear_font)

def Down():
    global main_y
    main_y+=next_down

def Right():
    global main_x
    main_x+=next_right

Reset_x()
Reset_y()

for p in pos:
    match p:
        case 1:
            if character_info[p-1][0]!=0:
                t_place=[(main_x,main_y),(main_x+115,main_y+125)]
                Paint_gun(character_info[p-1][13], t_place, character_info[p-1][15], character_info[p-1][14])
                if character_info[p-1][26]>0:
                    Paint_UI(character_info[p-1][26], [(main_x+350,main_y-97),(main_x+425,main_y-39)], character_info[p-1][13])
                for x in range(3):
                    gear_place = [(main_x+((x)*145),main_y-222),(main_x+135+((x)*145),main_y+115-222)]
                    Paint_gear(character_info[p-1][22+x], gear_place, character_info[p-1][16+x], character_info[p-1][19+x])
                for x in range(4):
                    Paint_skill(character_info[p-1][25], character_info[p-1][9+x], character_info[p-1][1+x], title[x])
                    Down()
        case 2:
            Reset_y()
            Right()
            if character_info[p-1][0]!=0:
                main_x+=k
                t_place=[(main_x,main_y),(main_x+115,main_y+125)]
                Paint_gun(character_info[p-1][13], t_place, character_info[p-1][15], character_info[p-1][14])
                if character_info[p-1][26]>0:
                    Paint_UI(character_info[p-1][26], [(main_x+350,main_y-97),(main_x+425,main_y-39)], character_info[p-1][13])
                for x in range(3):
                    gear_place = [(main_x+((x)*145),main_y-222),(main_x+135+((x)*145),main_y+115-222)]
                    Paint_gear(character_info[p-1][22+x], gear_place, character_info[p-1][16+x], character_info[p-1][19+x])
                for x in range(4):
                    Paint_skill(character_info[p-1][25], character_info[p-1][9+x], character_info[p-1][1+x], title[x])
                    Down()
        case 3:
            Reset_y()
            if character_info[p-1][0]!=0:
                main_x+=790-k
                t_place=[(main_x-225,main_y),(main_x+115,main_y+125)]
                Paint_gun(character_info[p-1][13], t_place, character_info[p-1][15], character_info[p-1][14])
                if character_info[p-1][26]>0:
                    Paint_UI(character_info[p-1][26], [(main_x-300-10,main_y-97),(main_x-225-10,main_y-39)], character_info[p-1][13])
                for x in range(3):
                    gear_place = [(main_x+((x)*145)-310,main_y-222),(main_x+135+((x)*145)-310,main_y+115-222)]
                    Paint_gear(character_info[p-1][22+x], gear_place, character_info[p-1][16+x], character_info[p-1][19+x])
                for x in range(4):
                    Paint_skill(character_info[p-1][25], character_info[p-1][9+x], character_info[p-1][1+x], title[x])
                    Down()
        case 4:
            Reset_y()
            Right()
            if character_info[p-1][0]!=0:
                t_place=[(main_x-225,main_y),(main_x+115,main_y+125)]
                Paint_gun(character_info[p-1][13], t_place, character_info[p-1][15], character_info[p-1][14])
                if character_info[p-1][26]>0:
                    Paint_UI(character_info[p-1][26], [(main_x-300-10,main_y-97),(main_x-225-10,main_y-39)], character_info[p-1][13])
                for x in range(3):
                    gear_place = [(main_x+((x)*145)-310,main_y-222),(main_x+135+((x)*145)-310,main_y+115-222)]
                    Paint_gear(character_info[p-1][22+x], gear_place, character_info[p-1][16+x], character_info[p-1][19+x])
                for x in range(4):
                    Paint_skill(character_info[p-1][25], character_info[p-1][9+x], character_info[p-1][1+x], title[x])
                    Down()
        case 5:
            main_x=435
            main_y=950
            if character_info[p-1][0]!=0:
                t_place=[(main_x-225,main_y),(main_x+115,main_y+125)]
                Paint_gun(character_info[p-1][13], t_place, character_info[p-1][15], character_info[p-1][14])
                if character_info[p-1][26]>0:
                    Paint_UI(character_info[p-1][26], [(main_x-225,main_y-166),(main_x-150,main_y-97-10)], character_info[p-1][13])
                for x in range(3):
                    gear_place = [(main_x-375,main_y-375+(x*125)),(main_x-240,main_y-260+(x*125))]
                    Paint_gear(character_info[p-1][22+x], gear_place, character_info[p-1][16+x], character_info[p-1][19+x])
                for x in range(4):
                    Paint_skill(character_info[p-1][25], character_info[p-1][9+x], character_info[p-1][1+x], title[x])
                    main_x-=125
        case 6:
            main_x=1780
            main_y=950
            if character_info[p-1][0]!=0:
                t_place=[(main_x,main_y),(main_x+115,main_y+125)]
                Paint_gun(character_info[p-1][13], t_place, character_info[p-1][15], character_info[p-1][14])
                if character_info[p-1][26]>0:
                    Paint_UI(character_info[p-1][26], [(main_x+265,main_y-166),(main_x+340,main_y-97-10)], character_info[p-1][13])
                for x in range(3):
                    gear_place = [(main_x+355,main_y-375+(x*125)),(main_x+490,main_y-260+(x*125))]
                    Paint_gear(character_info[p-1][22+x], gear_place, character_info[p-1][16+x], character_info[p-1][19+x])
                for x in range(4):
                    Paint_skill(character_info[p-1][25], character_info[p-1][9+x], character_info[p-1][1+x], title[x])
                    main_x+=125

img.save('skills.png', 'PNG')