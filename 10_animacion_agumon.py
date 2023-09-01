from pygame_functions import *

screenSize(500, 245)
setBackgroundImage("corridor.png")  # A background image always sits behind the sprites

agent = makeSprite("./agumon/17.gif")  # We create the sprite with the default image
addSpriteImage(agent, "./agumon/9.gif")  # Add extra images. They are stored in the Sprite object
addSpriteImage(agent, "./agumon/10.gif")  # but not displayed yet
addSpriteImage(agent, "./agumon/11.gif")
addSpriteImage(agent, "./agumon/12.gif")
addSpriteImage(agent, "./agumon/25.gif")
addSpriteImage(agent, "./agumon/21.gif")
addSpriteImage(agent, "./agumon/22.gif")
addSpriteImage(agent, "./agumon/23.gif")  # See the alternative way of doing this with a Sprite Sheet
addSpriteImage(agent, "./agumon/24.gif")  # See the alternative way of doing this with a Sprite Sheet

agentX = 200  # Set the X position on the screen
agentImage = 0  # This lets us track the current animation frame for the agent
moveSprite(agent, agentX, 120)
showSprite(agent)
nextFrame = clock()  # This lets us schedule the time for the next animation frame using the internal clock

while True:

    if keyPressed("right"):
        if clock() > nextFrame:  # It is time for the next animation frame
            agentImage += 1  # Move the animation on by one frame
            print(f"RIGHT {agentImage}")
            if agentImage > 9:  # We have 8 frames, so loop round to the start
                agentImage = 6
            changeSpriteImage(agent, agentImage)
            nextFrame = clock() + 60  # schedule the next frame 60 milliseconds from now

        agentX += 7  # Change the position for the sprite
        if agentX > 500:  # If reached the edge, loop round the screen
            agentX = -20

        moveSprite(agent, agentX, 120)  # Actually move the sprite

    if keyPressed("left"):
        if clock() > nextFrame:  # It is time for the next animation frame
            agentImage += 1  # Move the animation on by one frame
            print(f"LEFT {agentImage}")
            if agentImage > 5:  # We have 8 frames, so loop round to the start
                agentImage = 1
            changeSpriteImage(agent, agentImage)
            nextFrame = clock() + 60  # schedule the next frame 60 milliseconds from now

        agentX -= 7  # Change the position for the sprite
        if agentX > 500:  # If reached the edge, loop round the screen
            agentX = 20

        moveSprite(agent, agentX, 120)  # Actually move the sprite

    #else:
    #    agentImage = 0  # If the key is not being pressed, switch back to "standing" frame
    #    changeSpriteImage(agent, agentImage)

    tick(30)  # The movement runs at 30 frames per second, even though the agent image is only changed every 60ms