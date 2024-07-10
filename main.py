def on_a_pressed():
    global myDart
    myDart = darts.create(img("""
            ..........fffcc...fffffff...........
                    ..........fbbbbcffbbbbbbbf..........
                    ...........fbffbbbbb111bbf..........
                    ...........ffbbbbff11111bf..........
                    .........ffcbbbbbff1cccc1f..........
                    ........fcccbcbcbb1c1c1cff..........
                    ccccc..fcccbcbcbbb1333ccf...........
                    cbbddcfccccbcbcbbb1c333c............
                    .ccbddcccccbbbbbbb1c333c............
                    ..ccbbccccccbbbbb11c333c............
                    ..fccbfccccccbbbb11c133cc...........
                    ..fccfcbbcccccbbbc11c31cc...........
                    .fcbbf.cdddddfbbbc111111c...........
                    .fbbf...cdddfbbdbf1111cc............
                    fbbf.....ccfbbdbfffccc..............
                    fff........fffff....................
        """),
        SpriteKind.projectile)
    myDart.control_with_arrow_keys()
    controller.move_sprite(mySprite, 0, 0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_down_released():
    global direction
    direction = 3
controller.down.on_event(ControllerButtonEvent.RELEASED, on_down_released)

def on_right_released():
    global direction
    direction = 0
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def on_left_released():
    global direction
    direction = 1
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def on_a_released():
    controller.move_sprite(mySprite)
controller.A.on_event(ControllerButtonEvent.RELEASED, on_a_released)

def on_up_released():
    global direction
    direction = 2
controller.up.on_event(ControllerButtonEvent.RELEASED, on_up_released)

myDart: Dart = None
direction = 0
mySprite: Sprite = None
mySprite = sprites.create(img("""
        . . . . . . f f f f . . . . . . 
            . . . . f f f 2 2 f f f . . . . 
            . . . f f f 2 2 2 2 f f f . . . 
            . . f f f e e e e e e f f f . . 
            . . f f e 2 2 2 2 2 2 e e f . . 
            . . f e 2 f f f f f f 2 e f . . 
            . . f f f f e e e e f f f f . . 
            . f f e f b f 4 4 f b f e f f . 
            . f e e 4 1 f d d f 1 4 e e f . 
            . . f e e d d d d d d e e f . . 
            . . . f e e 4 4 4 4 e e f . . . 
            . . e 4 f 2 2 2 2 2 2 f 4 e . . 
            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
            . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
            . . . . . f f f f f f . . . . . 
            . . . . . f f . . f f . . . . .
    """),
    SpriteKind.player)
tiles.set_current_tilemap(tilemap("""
    level2
"""))
tiles.place_on_random_tile(mySprite, sprites.castle.tile_grass1)
scene.camera_follow_sprite(mySprite)
blocksleft = 0
direction = 0
controller.move_sprite(mySprite)