def on_button_pressed_a():
    global Score
    Score += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Score
    Score += -1
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_string("Home")
Score = 0

def on_forever():
    basic.show_number(Score)
basic.forever(on_forever)
