##############################################################################
#   Скрипт для версии: 3.0.1                                                 #
#   Автор скрипта: _BrenD_                                                   #
#       Instagram: https://www.instagram.com/_brend__/                       #
#       Steam: https://steamcommunity.com/id/brend32/                        #
#       YouTube: https://www.youtube.com/channel/UCATCV8pfte6-lyUy0sjGXUQ    #
#       TikTok: https://www.tiktok.com/@_brend__                             #
##############################################################################

init -505 python:
    Mod.developer = True
    Mod.episodes.add(ModEpisode("Секреты", "_BrenD_", "secrets_select", "gui/window_icon.png", "для 3.0.0", "https://www.youtube.com/channel/UCATCV8pfte6-lyUy0sjGXUQ"))
    Mod.mod_menu.insert_menu_button(2, "Секреты", ShowMenu("secrets"))

define brend = Character(_('_BrenD_'), what_prefix='', what_suffix='')

label secrets_select:
    scene bg_black with Dissolve(0.3)
    show screen secrets_menu_button
    menu:
        "{color=#fff}Деталь #1: Текст в флешбеках" if True:
            jump secret1
        "{color=#fff}Секрет #2: Лисичка" if True:
            jump secret2
        "{color=#fff}Секрет #3: Полная анимация рисования дракончика" if True:
            jump secret3
        "{color=#fff}Секрет #4: Снижёк в окно" if True:
            jump secret4
        "{color=#fff}Секрет #5: Сова машет" if True:
            jump secret5
        "{color=#fff}Секрет #6: Жучка в холодильнике" if True:
            jump secret6
        "{color=#fff}Секрет #7: Пропажа Антона?" if True:
            jump secret7

label secret1:
    scene bg_black with Dissolve(0.3)
    show expression "locate/school/in_side/Sem_gone/Sem_fin/03.jpg" with Dissolve(0.3)
    brend "Деталь #1: Текст в флешбеках"
    brend "Свинья Свин Pig"
    show expression "locate/school/in_side/Sem_gone/Sem_fin/04.jpg" with Dissolve(0.3)
    brend "Сёма"
    show expression "locate/school/in_side/finger/07.jpg" with Dissolve(0.3)
    brend "Боль Страх Жуть Мрак Испуг Боязнь Паника Фобия Тоска"
    jump secret2

label secret2:
    scene bg_black with Dissolve(0.3)
    show bg_lisa_lying with Dissolve(0.3)
    brend "Секрет #2: Лисичка"
    jump secret3

label secret3:
    scene bg_black with Dissolve(0.3)
    scene table_art_01 with Dissolve(0.5)

    brend "Секрет #3: Полная анимация рисования дракончика\n(Самой анимации нету, есть только кадры)"
    window hide

    play test_one "sounds/pen_bumaga.ogg"
    play test_six "sounds/Karandash_01.ogg"
    scene table_art_02 with Dissolve(0.3)
    pause 0.5
    play test_six "sounds/Karandash_02.ogg"
    scene table_art_03 with Dissolve(0.3)
    pause 0.75
    play test_six "sounds/Karandash_01.ogg"
    scene table_art_04 with Dissolve(0.3)
    show miganie_t4_t5
    stop music fadeout 3.5
    play music2 "music/Dvar - Ariil Iaat.ogg" fadein 2.5
    play test_one "sounds/lamp.ogg"
    
    show miganie_t6_t7
    $ renpy.pause(4.0)
    scene table_art_06 with Dissolve(0.1)
    $ renpy.pause(0.09)
    scene table_art_07 with Dissolve(0.1):
        zoom 0.48
    scene table_art_07_1 with Dissolve(0.2)
    $ renpy.pause(1)
    scene table_art_08 with Dissolve(0.2):
        xsize 1920
        ysize 1080
    $ renpy.pause(1)
    scene table_art_09 with Dissolve(0.2)
    $ renpy.pause(1)
    scene table_art_10 with Dissolve(0.2)
    $ renpy.pause(1)
    scene table_art_11 with Dissolve(0.2)
    $ renpy.pause(1)
    scene table_art_12 with Dissolve(0.2)
    $ renpy.pause(1)
    scene table_art_13 with Dissolve(0.2)
    $ renpy.pause(1)
    scene table_art_14 with Dissolve(0.2)
    $ renpy.pause(1)

    window show
    brend "Конец"
    jump secret4

label secret4:
    scene bg_black with Dissolve(0.3)
    show bg night_window2_sneg1 with Dissolve(0.3):
    brend "Секрет #4: Снижёк в окно"
    jump secret5

label secret5:
    scene bg_black with Dissolve(0.3)
    show expression LiveComposite((1920, 1080),
        (-259, 0), "locate/home/in_side/2st_floor/anton_room/window_par/024.jpg",
        (-259, 0), Animation("locate/home/in_side/2st_floor/anton_room/window_par/O_001.png", 1.50,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_002.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_003.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_004.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_005.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_006.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_007.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_008.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_009.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_010.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_011.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_012.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_013.png", 0.10,
            "locate/home/in_side/2st_floor/anton_room/window_par/O_014.png", 0.10)) with Dissolve(0.3)
    brend "Секрет #5: Сова машет\n(Здесь должно быть окно, но его нет в файлах)"
    jump secret6

image secret6Anim:
    "locate/home/in_side/1st_floor/kitchen/cold/Refrezirator_3.jpg" with Dissolve(0.3)
    2
    "locate/home/in_side/1st_floor/kitchen/cold/Refrezirator_4.jpg" with Dissolve(0.3)
    2
    "locate/home/in_side/1st_floor/kitchen/cold/Refrezirator_5.jpg" with Dissolve(0.3)
    2
    "locate/home/in_side/1st_floor/kitchen/cold/Refrezirator_6.jpg" with Dissolve(0.3)
    2
    repeat

label secret6:
    scene bg_black with Dissolve(0.3)
    show secret6Anim with Dissolve(0.3)
    brend "Секрет #6: Жучка в холодильнике"
    jump secret7

label secret7:
    scene bg_black with Dissolve(0.3)
    show expression "locate/Death.jpg" with Dissolve(0.3)
    brend "Секрет #7: Пропажа Антона?\n{size=-10}(Но это можно пока-что проигнорировать, так как данный файл используется только в тестовом скрипте)"
    show expression "images/interface/demo_end/bye.jpg" with Dissolve(0.3)
    brend "Другие газеты"
    show expression "images/interface/demo_end/bye2.png" with Dissolve(0.3)
    $ renpy.pause()
    show expression "images/interface/demo_end/bye3.png" with Dissolve(0.3)
    $ renpy.pause()


default objHov = "Unhovered"
init python:
    class UnlockAnimals:
        @property
        def owl(self):
            return persistent.animal_unlock[0]

        @owl.setter
        def owl(self, value):
            persistent.animal_unlock[0] = value

        @property
        def fox(self):
            return persistent.animal_unlock[1]

        @fox.setter
        def fox(self, value):
            persistent.animal_unlock[1] = value

        @property
        def wolf(self):
            return persistent.animal_unlock[2]

        @wolf.setter
        def wolf(self, value):
            persistent.animal_unlock[2] = value

        @property
        def beer(self):
            return persistent.animal_unlock[4]

        @beer.setter
        def beer(self, value):
            persistent.animal_unlock[4] = value

        @property
        def master(self):
            return persistent.animal_unlock[3]

        @master.setter
        def master(self, value):
            persistent.animal_unlock[3] = value

define unlockAnimals = UnlockAnimals()


init -501 screen toggle(variable):
    frame:
        style_prefix "main_menu"
        ysize 50
        xsize 150
        background Null()    
        textbutton _("Вкл"):
            action SetVariable(variable, True)
            xsize 150
        button:
            background Frame("interface/main_meny/plaska.png")
            text _("Вкл")
            at mm_but
            xsize 150
            action SetVariable(variable, True)

    frame:   
        style_prefix "main_menu"
        ysize 50
        xsize 150
        background Null()    
        textbutton _("Выкл"):
            action SetVariable(variable, False)
            xsize 150
        button:
            background Frame("interface/main_meny/plaska.png")
            text _("Выкл")
            at mm_but
            xsize 150
            action SetVariable(variable, False)

init -501 screen link_button(buttontext, link):
    button:
        text buttontext:
            size 50
            font "font/russia.ttf"
            hover_underline True
            hover_color "#285999"
        action OpenURL(link)

screen secrets_menu_button():
    vbox:
        xpos 1730
        ypos 20
        frame:   
            style_prefix "main_menu"
            ysize 50
            xsize 150
            background Null()    
            textbutton _("Меню"):
                action Jump("secrets_select")
                xsize 150
            button:
                background Frame("interface/main_meny/plaska.png")
                text _("Меню")
                at mm_but
                xsize 150
                action Jump("secrets_select")
    pass

init -501 screen secrets():
    style_prefix "pref"

    modal True tag menu
    on "show" action Play("test_five", "sounds/menu/menu-window-4.ogg")
    on "replace" action Play("test_five", "sounds/menu/menu-window-4.ogg")
    add "bg_menu_about" at conf_fon

    viewport id "autor":
        draggable True
        mousewheel True
        xsize 1600
        ysize 900
        xalign 0.5
        yalign 0.5

        has vbox:
            xalign 0.5
            spacing 46
            xsize 1600

    
        hbox:
            style_group "about"
            at for_yes_no_10
            spacing 20
            text _("{size=+10}Режим разработчика: "):
                ypos 18
            use toggle("Mod.developer")

        hbox:
            style_group "about"
            at for_yes_no_10
            spacing 20
            text _("{size=+10}Секретные сцены: "):
                ypos 18
            frame:   
                style_prefix "main_menu"
                ysize 50
                xsize 150
                background Null()    
                textbutton _("Запустить"):
                    action [Stop('music'), Start('secrets_select')]
                    xsize 350
                button:
                    background Frame("interface/main_meny/plaska.png")
                    text _("Запустить")
                    at mm_but
                    xsize 350
                    action [Stop('music'), Start('secrets_select')]

        vbox:
            style_group "about"
            at for_yes_no_10
            spacing 20
            xsize 1600
            text _("{size=+40}Звери в меню:"):
                ypos 18
                xalign 0.45
            hbox:
                xsize 1500
                xalign 0.5
                vbox:
                    spacing 20
                    text _("{size=+20}Лиса"):
                        ypos 18
                        xalign 0.5
                    use toggle("unlockAnimals.fox")
                vbox:
                    spacing 20
                    text _("{size=+20}Волк"):
                        ypos 18
                        xalign 0.5
                    use toggle("unlockAnimals.wolf")
                vbox:
                    spacing 20
                    text _("{size=+20}Сова"):
                        ypos 18
                        xalign 0.5
                    use toggle("unlockAnimals.owl")
                vbox:
                    spacing 20
                    text _("{size=+20}Медведь"):
                        ypos 18
                        xalign 0.5
                    use toggle("unlockAnimals.beer")
                vbox:
                    spacing 20
                    text _("{size=+20}Мастер"):
                        ypos 18
                        xalign 0.5
                    use toggle("unlockAnimals.master")

        vbox:
            style_group "about"
            at for_yes_no_10
            spacing 5

            frame:
                background Null()
                ysize 130
            text _("Скрипт написан для версии: 3.0.1"):
                size 50
                font "font/russia.ttf"
            text _("За основу взят оригинальный файл screens.rpy взятый из купленной стимовской версии игры"):
                size 50
                font "font/russia.ttf"

            text "Обратная связь:":
                size 50
                font "font/russia.ttf"
            vbox:
                xpos 30
                use link_button("Почта: brend.developer.ukr@gmail.com", 'mailto:brend.developer.ukr@gmail.com')
                use link_button("Instagram: @_brend__", 'https://www.instagram.com/_brend__/')
                use link_button("Steam: id/brend32/", 'https://steamcommunity.com/id/brend32/')
                use link_button("YouTube: _BrenD_", 'https://www.youtube.com/channel/UCATCV8pfte6-lyUy0sjGXUQ')
                use link_button("TikTok: @_brend__", 'https://www.tiktok.com/@_brend__')
                


    vbar:
        value YScrollValue("autor")
        xpos 1600
        yalign 0.5
        xsize 20
        ysize 900
        at for_yes_no_10

    imagemap:
        ground Null(1920, 1080)
        insensitive Null(1920, 1080)
        idle "interface/preferences/button/05.png"
        hover "interface/preferences/button/05.png"
        selected_idle "interface/preferences/button/05.png"
        selected_hover "interface/preferences/button/05.png"
        alpha True
        at for_yes_no_10

        hotspot (1673,821,108,88):
            hover_sound "sounds/menu/menu-button-select-1.ogg"
            activate_sound "sounds/menu/menu-button-click-1.ogg"
            action Return()
            at filepic_but3

    
    text _("Автор скрипта:  _BrenD_"):
        at for_yes_no_10
        size 55
        font "font/russia.ttf"
        xpos 30
        ypos 15

    key "game_menu" action Return()
    on "show" action Show("block_screen")
    timer 1.0 action Hide("block_screen")


##############################################################################