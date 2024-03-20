input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    Score += 1
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    Score += -1
})
basic.showString("Home")
let Score = 0
basic.forever(function on_forever() {
    basic.showNumber(Score)
})
