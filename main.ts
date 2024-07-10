controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    myDart = darts.create(img`
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
        `, SpriteKind.Projectile)
    myDart.setPosition(mySprite.x, mySprite.y)
    myDart.controlWithArrowKeys(true)
    controller.moveSprite(mySprite, 0, 0)
})
controller.down.onEvent(ControllerButtonEvent.Released, function () {
    direction = 3
})
controller.right.onEvent(ControllerButtonEvent.Released, function () {
    direction = 0
})
controller.left.onEvent(ControllerButtonEvent.Released, function () {
    direction = 1
})
controller.A.onEvent(ControllerButtonEvent.Released, function () {
    controller.moveSprite(mySprite)
})
controller.up.onEvent(ControllerButtonEvent.Released, function () {
    direction = 2
})
let myDart: Dart = null
let direction = 0
let mySprite: Sprite = null
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
tiles.setCurrentTilemap(tilemap`level2`)
tiles.placeOnRandomTile(mySprite, sprites.castle.tileGrass1)
scene.cameraFollowSprite(mySprite)
let blocksleft = 0
direction = 0
controller.moveSprite(mySprite)
