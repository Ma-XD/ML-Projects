import copy
from player import *
from player_draw import *
from field import *
from field_draw import *
from bank import *
from transformer import *
from immovables import *
from action import *
from drawer import *
from cube import *

def run_simulation():
    TILE_NAME = [
		"Jail",
		"St. Charles Place",
		"Electric Company",
		"States Avenue",
		"Verginia Avenue",
		"Pennsylvania Railroad",
		"St. James Place",
		"Community Chest",
		"Tennessee Avenue",
		"New York Avenue",
		"Free Parking",
		"Kentucky Avenue",
		"Chance",
		"Indiana Avenue",
		"Illinois Avenue",
		"B & O Railroad",
		"Atlantic Avenue",
		"Ventinor Avenue",
		"Waterworks",
		"Marvin Gardens",
		"Jail",
		"Pacific Avenue",
		"North Carolina Avenue",
		"Community Chest",
		"Pennsylvania Avenue",
		"Short Line",
		"Chance",
		"Park Place",
		"Taxes",
		"Boardwalk",
        "GO",
        "Mediterranean Avenue",
        "Community Chest",
		"Baltic Avenue",
		"Taxes",
		"Reading Railroad",
		"Oriental Avenue",
		"Chance",
		"Vermont Avenue",
		"Connecticut Avenue"
        ]

    #TILES_REAL_ESTATE = [1,3,5,6,8,9,11,12,13,14,15,16,18,19,21,23,24,25,26,27,28,29,31,32,34,35,37,39]
    #TILES_COMMUNITY   = [2,17,33]
    #TILES_CHANCE      = [7,22,36]
    #TILES_TAX         = [4,38]
    #TILES_NONE        = [20]
    #TILES_JAIL        = [10, 30]
    #TILES_GO          = [0]

    centers = [
               [955, 45], [875, 45], [818, 45], [764, 45], [710, 45], [655, 45], [600, 45], [540, 45], [485, 45], [420, 45], 
               [350, 45], [350, 120],[350, 173],[350, 232],[350, 287],[350, 347],[350, 405],[350, 457],[350, 515],[350, 570],
               [350, 635],[420, 635],[485, 635],[540, 635],[600, 635],[655, 635],[710, 635],[764, 635],[818, 635],[875, 635],
               [955, 635],[955, 570],[955, 515],[955, 457],[955, 405],[955, 347],[955, 287],[955, 232],[955, 173],[955, 120]]
    
    coordinates = []

    x_st = 700
    y_st = 1

    for i in range(0, 10):
        x_n = x_st - 57
        if i % 10 == 0:
            x_n = x_st - 93
        
        a = [[copy.copy(x_n), copy.copy(x_st)], [copy.copy(y_st), copy.copy(y_st) + 93]]
        
        coordinates.append(copy.deepcopy(a))
        
        if i % 10 == 0:
            x_st -= 93
        else:
            x_st -= 57

    for i in range(0, 10):
        y_n = y_st + 57
        if i % 10 == 0:
            y_n = y_st + 93
        
        a = [[copy.copy(x_st) - 93, copy.copy(x_st)], [copy.copy(y_st), copy.copy(y_n)]]
        
        coordinates.append(copy.deepcopy(a))
        
        if i % 10 == 0:
            y_st += 93
        else:
            y_st += 57

    x_st -= 93

    for i in range(0, 10):
        x_n = x_st + 57
        if i % 10 == 0:
            x_n = x_st + 93
        
        a = [[copy.copy(x_st), copy.copy(x_n)], [copy.copy(y_st), copy.copy(y_st) + 93]]
        
        coordinates.append(copy.deepcopy(a))
        
        if i % 10 == 0:
            x_st += 93
        else:
            x_st += 57
    
    y_st += 93
    for i in range(0, 10):
        y_n = y_st - 57
        if i % 10 == 0:
            y_n = y_st - 93
        
        a = [[copy.copy(x_st), copy.copy(x_st) + 93], [copy.copy(y_n), copy.copy(y_st)]]
        
        coordinates.append(copy.deepcopy(a))
        
        if i % 10 == 0:
            y_st -= 93
        else:
            y_st -= 57

    #print(coordinates)
    field_def = []
    price = 70
    for i in range(0, 40):
        if TILE_NAME[i] == "Jail":
            field_def.append(action(i, "Jail", coordinates[i], centers[i]))
        elif TILE_NAME[i] == "Taxes":
            field_def.append(action(i, "Taxes", coordinates[i], centers[i]))
        elif TILE_NAME[i] == "Community Chest":
            field_def.append(action(i, "Community Chest", coordinates[i], centers[i]))
        elif TILE_NAME[i] == "Chance":
            field_def.append(action(i, "Chance", coordinates[i], centers[i]))
        elif TILE_NAME[i] == "GO":
            field_def.append(action(i, "GO", coordinates[i], centers[i]))
        elif TILE_NAME[i] == "Free Parking":
            field_def.append(action(i, "Free Parking", coordinates[i], centers[i]))
        else:
            price += 5
            field_def.append(immovables(i, TILE_NAME[i], price, "bank", 0, price, coordinates[i], centers[i]))
        
    #carts on field
    chance = ["cash +150", "cash -50", "pay 50"]
    community = ["broke all houses", "cash +50", "tax 50"]
    
    #objects
    f_coor = [[93, 607], [93, 607]] 
    fld = field_draw(field_def, f_coor)
    bnk = bank(20000000000, fld)
    PLAYERS = [player_draw(0, 300, [], 30, False, [150, 690], fld, bnk), player_draw(1, 300, [], 30, False, [1150, 690], fld, bnk)]
    draw = drawer()
    cube1 = cube(650, 120)
    cube2 = cube(625, 120)

    fld.draw_field()

    con = 1
    chest = 1
    ch = 1
    while True:
        fld.draw_card(PLAYERS[1 - con].position)
        con = 1 - con
        numb = [cube1.get_con(), cube2.get_con()]
        PLAYERS[con].position += (numb[0] + numb[1])
        if PLAYERS[con].position >= 30 and (PLAYERS[con].position - (numb[0] + numb[1])) < 30:
            draw.draw_message(str(con + 1), "Ohoho You have a big salary")
            PLAYERS[con].pay(-200)
        PLAYERS[con].position %= 40

        cube1.draw(numb[0])
        cube2.draw(numb[1])
        
        PLAYERS[con].draw_player_def()
        PLAYERS[1 - con].draw_player_def()

        com = fld.field_definition[PLAYERS[con].position].name

        if com == "Jail":
            draw.draw_message(str(con + 1), " loser. He went to Jail and paid off -50$")
            PLAYERS[con].pay(50)
            if PLAYERS[con].is_bankrupt:
                    draw.draw_message(str(con + 1), "GAME OVER: " + str(2 - con) + " player win")
                    break
        elif com == "Taxes":
            draw.draw_message(str(con + 1), "Paid 200$")
            PLAYERS[con].pay(200)
            if PLAYERS[con].is_bankrupt:
                    draw.draw_message(str(con + 1), "GAME OVER: " + str(2 - con) + " player win")
                    break
        elif com == "Community Chest":
            if community[chest] == "broke all houses":
                draw.draw_message(str(con + 1), "COMMUNITY CHEST: destroyed all houses")
                PLAYERS[con].destroy_houses()
            elif community[chest] == "cash +100":
               draw.draw_message(str(con + 1), "COMMUNITY CHEST: Have a good money")
               PLAYERS[con].pay(-100)
            else:
                PLAYERS[con].pay(50)
                draw.draw_message(str(con + 1), "COMMUNITY CHEST: Paid 50$")
                if PLAYERS[con].is_bankrupt:
                    draw.draw_message(str(con + 1), "GAME OVER: " + str(2 - con) + " player win")
                    break
            chest += 1
            chest %= 3
        elif com == "Chance":
            if chance[ch] == "cash +150":
                draw.draw_message(str(con + 1), "CHANCE: Have a good money")
                PLAYERS[con].pay(-150)
            elif chance[ch] == "cash -50":
                draw.draw_message(str(con + 1), "CHANCE: Paid 50$")
                PLAYERS[con].pay(50)
                if PLAYERS[con].is_bankrupt:
                    draw.draw_message(str(con + 1), "GAME OVER: " + str(2 - con) + " player win")
                    break
            else:
                draw.draw_message(str(con + 1),"COMMUNITY CHEST: Paid 50$")
                PLAYERS[con].pay(50)
                if PLAYERS[con].is_bankrupt:
                    draw.draw_message(str(con + 1), "GAME OVER: " + str(2 - con) + " player win")
                    break
            ch += 1
            ch %= 3
        elif com == "GO":
            continue
        elif com == "Free Parking":
            draw.draw_message(str(con + 1), " decided to relax")
            continue
        else:
            if fld.field_definition[PLAYERS[con].position].owner == "bank":
                if PLAYERS[con].money >= fld.field_definition[PLAYERS[con].position].price:
                    draw.draw_message(str(con + 1), "bought " + str(fld.field_definition[PLAYERS[con].position].name))
                    PLAYERS[con].pay(fld.field_definition[PLAYERS[con].position].price)
                    PLAYERS[con].buy_immov(PLAYERS[con].position)
                else:
                    draw.draw_message(str(con + 1), "doesnt have money to buy a " + str(fld.field_definition[PLAYERS[con].position].name))
            elif fld.field_definition[PLAYERS[con].position].owner != PLAYERS[con].name:
                draw.draw_message(str(con + 1), " had a bad day because he paid a rent: " + str(fld.field_definition[PLAYERS[con].position].rent))
                PLAYERS[con].pay_rent(fld.field_definition[PLAYERS[con].position].rent, PLAYERS[1 - con])
            else:
                draw.draw_message(str(con + 1), " visit his immovables")

run_simulation()