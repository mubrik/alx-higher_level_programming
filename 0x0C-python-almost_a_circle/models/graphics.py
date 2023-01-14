#!/usr/bin/python3
""" Graphics Class  """
import turtle


class Display:
    """ handles displaying with turtle """
    pen_colors = [
        "#87a96b", "#318ce7", "#00cc99", "#cc0099",
        "#d2691e", "#002e63", "#da70d6", "#872657",
    ]
    pen_color_ind = 0

    def __init__(self):
        """ init method """
        self.window = turtle.Screen()
        self.window.resetscreen()
        self.window.title("Welcome")
        self.window.bgcolor("#f0f8ff")
        self.pen = turtle.RawTurtle(self.window)
        self.pen.shape("circle")
        self.pen.width(5)

    def config_pen(self):
        """ sets pen up before drawing """
        if self.pen_color_ind >= len(self.pen_colors):
            self.pen_color_ind = 0
        self.pen.fillcolor(self.pen_colors[self.pen_color_ind])
        self.pen_color_ind += 1

    def keep_on(self):
        """ keep the display open """
        # bind escape
        self.window.onkey(self.end, "Escape")
        self.window.listen()
        self.window.mainloop()
        self.is_running = True

    def draw_rect(self, rect_list):
        self.pen.speed(1)
        """ draw rectangles """
        if rect_list:
            for rect in rect_list:
                # position
                if self.pen.isdown():
                    self.pen.penup()
                self.pen.setposition(rect.x, rect.y)
                # drop pen
                self.config_pen()
                self.pen.pendown()
                self.pen.begin_fill()
                self.pen.forward(rect.width)
                self.pen.right(90)
                self.pen.forward(rect.height)
                self.pen.right(90)
                self.pen.forward(rect.width)
                self.pen.right(90)
                self.pen.forward(rect.height)
                self.pen.penup()
                self.pen.end_fill()

    def test_draw(self):
        """ testing """
        self.pen.speed(1)
        self.pen.circle(150)

    def end(self):
        """ end the screen """
        self.window.bye()
        self.is_running = False
