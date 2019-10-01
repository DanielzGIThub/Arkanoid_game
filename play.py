from superwires import games, color

games.init(screen_width = 800, screen_height = 600, fps = 50)

class Ball(games.Sprite):

    def update(self):
        if self.right > games.screen.width or self.left < 0:
            self.dx  = -self.dx
        
        if self.top < 0:
            self.dy = -self.dy

        if self.bottom > games.screen.height:
            self.destroy()
            end()
   
    def handle_collision(self):
        self.dy  = -self.dy


class Base(games.Sprite):  

    def update(self):
        self.x = games.mouse.x
        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width
        self.collision()

    def collision(self):
        for ball in self.overlapping_sprites:
            ball.handle_collision()
            

class Yellow_Brick(games.Sprite):

    bricks =[]
    score = games.Text(value = 0,
                        size = 40,
                        color = color.yellow,
                        right = games.screen.width-20,
                        top = 20)
    games.screen.add(score)
    
    def __init__(self, image, angle, x, y):
        super().__init__(image, angle,  x, y)
        self.bricks.append(self)

    def update(self):
        self.destruction()

    def destruction(self):
        for ball in self.overlapping_sprites:
            ball.handle_collision()
            self.score.value += 1
            self.destroy()
            self.bricks.remove(self)
            if self.bricks == []:
                brick_wall()
    

def brick_wall():

    yellow_brick_image = games.load_image("yellow_brick.png")
    bricks = []
    for i in range(10):
        bricks.append("yellow_brick{}".format(i))
    
    for j in range(3,5):
        position = 0
        for brick in bricks:
            position += 72
            brick = Yellow_Brick(image = yellow_brick_image,
                                angle = 0,
                                x = position,
                                y = games.screen.height/j)
            games.screen.add(brick)


def end():
    game_over_message = games.Message(value = "**GAME OVER** Your Score: {}".format(Yellow_Brick.score.value),
                                        size = 70,
                                        color = color.red,
                                        x = games.screen.width/2,
                                        y = games.screen.height/2,
                                        lifetime = 3 * games.screen.fps,
                                        after_death = games.screen.quit,
                                        is_collideable = False)
    games.screen.add(game_over_message)


def main():
    bground = games.load_image("background.png", transparent=False)
    games.screen.background = bground

    ball_image = games.load_image("ball.png")
    ball = Ball(image = ball_image, 
                x = games.screen.width/2, 
                y = games.screen.height-14,
                dx = 2,
                dy = -2)
    games.screen.add(ball)

    base_image = games.load_image("base.png")
    base = Base(image = base_image,
                x = games.screen.width/2,
                y = games.screen.height-20)
    games.screen.add(base)

    brick_wall()

    games.mouse.is_visible = False
    games.screen.event_grab = True


main()

games.screen.mainloop()