#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

def lecture02_01_printHeroStatus() -> None:
    # lecture02_Hero.csvを読み込みidが1のHeroの名前とステータスを出力する関数
    hero_header = []
    hero_data = []
    
    with open('lecture02_Hero.csv') as f:
        for line in f:
            if len(hero_header) == 0:
                hero_header = line.rstrip().split(',')
            else:
                hero_data.append(line.rstrip().split(','))
    
    id_index = hero_header.index('ID')
    
    hero_name = None
    hero_hp = None
    hero_mp = None
    hero_atk = None
    hero_def = None
    hero_age = None
    
    for hero in hero_data:
        if hero[id_index] == "1":
            hero_name = hero[hero_header.index('Name')]
            hero_hp = int(hero[hero_header.index('HP')])
            hero_mp = int(hero[hero_header.index('MP')])
            hero_atk = int(hero[hero_header.index('Atk')])
            hero_def = int(hero[hero_header.index('Def')])
            hero_age = int(hero[hero_header.index('Age')])
    
    print(f"{hero_name}のステータスは" +
        f"HP:{hero_hp}," +
        f"MP:{hero_mp}," +
        f"Atk:{hero_atk}," +
        f"Def:{hero_def}," +
        f"Age:{hero_age}")

def lecture02_01_printWeaponStatus() -> None:
    # lecture02_Weapon.csvを読み込みidが1の武器の名前とステータスを出力する関数
    weapon_header = []
    weapon_data = []
    
    with open('lecture02_weapon.csv') as f:
        for line in f:
            if len(weapon_header) == 0:
                weapon_header = line.rstrip().split(',')
            else:
                weapon_data.append(line.rstrip().split(','))
    
    id_index = weapon_header.index('ID')
    
    weapon_name = None
    weapon_hp = None
    weapon_mp = None
    weapon_atk = None
    weapon_def = None
    weapon_age = None
    
    for weapon in weapon_data:
        if weapon[id_index] == "1":
            weapon_name = weapon[weapon_header.index('Weapon_Name')]
            weapon_hp = int(weapon[weapon_header.index('HP')])
            weapon_mp = int(weapon[weapon_header.index('MP')])
            weapon_atk = int(weapon[weapon_header.index('Atk')])
            weapon_def = int(weapon[weapon_header.index('Def')])
            weapon_age = int(weapon[weapon_header.index('Age')])
    
    print(f"{weapon_name}のステータスは" +
        f"HP:{weapon_hp}," +
        f"MP:{weapon_mp}," +
        f"Atk:{weapon_atk}," +
        f"Def:{weapon_def}," +
        f"Age:{weapon_age}")

def lecture02_01_printHeroStatusWithWeapon() -> None:
    hero_header = []
    hero_data = []
    
    with open('lecture02_Hero.csv') as f:
        for line in f:
            if len(hero_header) == 0:
                hero_header = line.rstrip().split(',')
            else:
                hero_data.append(line.rstrip().split(','))
    
    id_index = hero_header.index('ID')

    hero_name = None
    hero_hp = None
    hero_mp = None
    hero_atk = None
    hero_def = None
    hero_age = None
    hero_weapon = None
    
    for hero in hero_data:
        if hero[id_index] == "1":
            hero_name = hero[hero_header.index('Name')]
            hero_hp = int(hero[hero_header.index('HP')])
            hero_mp = int(hero[hero_header.index('MP')])
            hero_atk = int(hero[hero_header.index('Atk')])
            hero_def = int(hero[hero_header.index('Def')])
            hero_age = int(hero[hero_header.index('Age')])
            hero_weapon = int(hero[hero_header.index('Weapon')])
    
    weapon_header = []
    weapon_data = []
    
    with open('lecture02_weapon.csv') as f:
        for line in f:
            if len(weapon_header) == 0:
                weapon_header = line.rstrip().split(',')
            else:
                weapon_data.append(line.rstrip().split(','))
    
    id_index = weapon_header.index('ID')
    
    weapon_name = None
    weapon_hp = None
    weapon_mp = None
    weapon_atk = None
    weapon_def = None
    weapon_age = None
    
    for weapon in weapon_data:
        if int(weapon[id_index]) == hero_weapon:
            weapon_name = weapon[weapon_header.index('Weapon_Name')]
            weapon_hp = int(weapon[weapon_header.index('HP')])
            weapon_mp = int(weapon[weapon_header.index('MP')])
            weapon_atk = int(weapon[weapon_header.index('Atk')])
            weapon_def = int(weapon[weapon_header.index('Def')])
            weapon_age = int(weapon[weapon_header.index('Age')])

    
    
    # ステータス情報を出力する
    print(f"{weapon_name}を装備した{hero_name}のステータスは" +
        f"HP:{hero_hp+weapon_hp}," +
        f"MP:{hero_mp+weapon_mp}," +
        f"Atk:{hero_atk+weapon_atk}," +
        f"Def:{hero_def+weapon_def}," +
        f"Age:{hero_age+weapon_age}")

if __name__ == '__main__':
    lecture02_01_printHeroStatus()
    lecture02_01_printWeaponStatus()
    lecture02_01_printHeroStatusWithWeapon()