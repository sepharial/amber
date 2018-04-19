from __future__ import print_function
import sys
from random import choice
from flask import Flask, render_template
app=Flask("project")

dragon_location = 0,0
player_location = 0,0
number_of_moves = 0

@app.route("/")
def run():
    global number_of_moves
    number_of_moves = 7

    cave_width = 5
    cave_length = 5
    cave_xs = range(1,cave_width)
    cave_ys = range(1,cave_length)
    cave_number = cave_width*cave_length

    global dragon_location
    global player_location
    dragon_location = choice(cave_xs),choice(cave_ys)
    player_location = choice(cave_xs),choice(cave_ys)
    while player_location == dragon_location:
        player_location = choice(cave_xs),choice(cave_ys)

    both_locations = "Dragon location is " + str(dragon_location) + ", Player location is " + str(player_location)
    
    message = give_message()

    return render_template("finalproject.html", both_locations=both_locations, dragon_location = dragon_location, player_location = player_location, number_of_moves = number_of_moves, message = message)




@app.route("/up")
def up():
    global player_location
    global dragon_location
    global number_of_moves
    new_player_location = player_location[0], player_location[1]+1
    player_location = new_player_location
    number_of_moves = number_of_moves - 1
    both_locations = "Dragon location is " + str(dragon_location) + ", Player location is " + str(player_location)
    
    message = give_message()

    return render_template("finalproject.html", both_locations=both_locations, dragon_location = dragon_location, player_location = player_location, number_of_moves = number_of_moves, message = message)


@app.route("/left")
def left():
    global player_location
    global dragon_location
    global number_of_moves
    new_player_location = player_location[0]-1, player_location[1]
    player_location = new_player_location
    number_of_moves = number_of_moves - 1
    both_locations = "Dragon location is " + str(dragon_location) + ", Player location is " + str(player_location)
    
    message = give_message()

    return render_template("finalproject.html", both_locations=both_locations, dragon_location = dragon_location, player_location = player_location, number_of_moves = number_of_moves, message = message)

@app.route("/right")
def right():
    global player_location
    global dragon_location
    global number_of_moves
    new_player_location = player_location[0]+1, player_location[1]
    player_location = new_player_location
    number_of_moves = number_of_moves - 1
    both_locations = "Dragon location is " + str(dragon_location) + ", Player location is " + str(player_location)
    
    message = give_message()

    return render_template("finalproject.html", both_locations=both_locations, dragon_location = dragon_location, player_location = player_location, number_of_moves = number_of_moves, message = message)

@app.route("/down")
def down():
    global player_location
    global dragon_location
    global number_of_moves
    new_player_location = player_location[0], player_location[1]-1
    player_location = new_player_location
    number_of_moves = number_of_moves - 1
    both_locations = "Dragon location is " + str(dragon_location) + ", Player location is " + str(player_location)
    
    message = give_message()

    return render_template("finalproject.html", both_locations=both_locations, dragon_location = dragon_location, player_location = player_location, number_of_moves = number_of_moves, message = message)

@app.route("/victory")
def victory():
    return render_template("victory.html")


def give_message():
    global player_location
    global dragon_location
    global number_of_moves
    if (player_location == dragon_location):
        return "You've found the dragon egg"
    elif (number_of_moves < 1):
        return "You hear the roar of a fully grown dragon throughout the caverns"
    elif ((player_location[0] + 1 == dragon_location[0]) or (player_location[0] - 1 == dragon_location[0]) or (player_location[0] == dragon_location[0])) and ((player_location[1] + 1 == dragon_location[1]) or (player_location[1] - 1 == dragon_location[1]) or (player_location[1] == dragon_location[1])):
        return "You smell a dragon egg"
    else:
        return "You smell nothing"


app.run(debug=True)
