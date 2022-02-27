#!/usr/bin/env python3
"""
@Author: zfoteff
@Version: 1.1.0
"""
from tkinter import *
import time
from turtle import title

def generate_time_grid():
    """ Generate the 2d grid representing the current time

    Returns:
        list(string): list of padded binary strings that represent that hour, 
        minute, and second of the current time 
    """
    curr_time_grid = []
    t = time.strftime("%H%M%S")
    for digit in t:
        curr_time_grid.append(list(bin(int(digit))[2:].rjust(4,"0")))

    return curr_time_grid

#   create 6x4 grid for representing the binary clock
def create_clock(canvas: Canvas):
    """ Create the canvas objects for the structure of the clock

    Args:
        canvas (Canvas): Canvas object to draw objects on
    """
    #   hour segments
    canvas.create_rectangle(10,10,70,70, outline="black", width=5, tag="h00")
    canvas.create_rectangle(10,80,70,140, outline="black", width=5, tag="h01")
    canvas.create_rectangle(10,150,70,210, outline="black", width=5, tag="h02")
    canvas.create_rectangle(10,220,70,280, outline="black", width=5, tag="h03")
    canvas.create_rectangle(80,10,140,70, outline="black", width=5, tag="h10")
    canvas.create_rectangle(80,80,140,140, outline="black", width=5, tag="h11")
    canvas.create_rectangle(80,150,140,210, outline="black", width=5, tag="h12")
    canvas.create_rectangle(80,220,140,280, outline="black", width=5, tag="h13")
    #   minute segments
    canvas.create_rectangle(160,10,220,70, outline="black", width=5, tag="m00")
    canvas.create_rectangle(160,80,220,140, outline="black", width=5, tag="m01")
    canvas.create_rectangle(160,150,220,210, outline="black", width=5, tag="m02")
    canvas.create_rectangle(160,220,220,280, outline="black", width=5, tag="m03")
    canvas.create_rectangle(230,10,290,70, outline="black", width=5, tag="m10")
    canvas.create_rectangle(230,80,290,140, outline="black", width=5, tag="m11")
    canvas.create_rectangle(230,150,290,210, outline="black", width=5, tag="m12")
    canvas.create_rectangle(230,220,290,280, outline="black", width=5, tag="m13")
    #   second segments
    canvas.create_rectangle(310,10,370,70, outline="black", width=5, tag="s00")
    canvas.create_rectangle(310,80,370,140, outline="black", width=5, tag="s01")
    canvas.create_rectangle(310,150,370,210, outline="black", width=5, tag="s02")
    canvas.create_rectangle(310,220,370,280, outline="black", width=5, tag="s03")
    canvas.create_rectangle(380,10,440,70, outline="black", width=5, tag="s10")
    canvas.create_rectangle(380,80,440,140, outline="black", width=5, tag="s11")
    canvas.create_rectangle(380,150,440,210, outline="black", width=5, tag="s12")
    canvas.create_rectangle(380,220,440,280, outline="black", width=5, tag="s13")
    #   colons
    canvas.create_oval(145, 125, 155, 135, fill="white", width=3, outline="black")
    canvas.create_oval(145, 155, 155, 165, fill="white", width=3, outline="black")
    canvas.create_oval(295, 125, 305, 135, fill="white", width=3, outline="black")
    canvas.create_oval(295, 155, 305, 165, fill="white", width=3, outline="black")

#   update each section to be on or off corresponding with each number's binary representation
def draw_time(canvas: Canvas, time: str):
    """ Draw the current time onto the canvas 

    Args:
        canvas (Canvas): Canvas object to fill the time in on
        time (str): time string to read and process
    """
    #   flag to help determine which column the time should be drawn into
    first_column = True
    #   tag to determine whether time should be written to hours, mins, or seconds
    column_tag = "h"

    #   construct the list of 
    for i in range(6):
        if i % 2 == 0:
            first_column = True
        else:
            first_column = False

        if i==0 or i==1:
            column_tag = "h"
        elif i==2 or i==3:
            column_tag = "m"
        elif i==4 or i==5:
            column_tag = "s"

        for j in range(4):
            tag_str = ""
            #   create the tag for each element based on if they number should be in first column for the section
            if first_column:
                tag_str = "{col}0{id}".format(col=column_tag, id=str(j))
            else:
                tag_str = "{col}1{id}".format(col=column_tag, id=str(j))

            #   Update items based on if they should be on in the clock
            if time[i][j] == "0":
                canvas.itemconfig(tag_str, fill="")
            elif time[i][j] == "1":
                canvas.itemconfig(tag_str, fill="white")
    canvas.pack()

def main():
    root = Tk()
    root.title("Binary Clock")
    c = Canvas(root, bg="grey", height=300, width=450)
    create_clock(c)

    while True:
        draw_time(c, generate_time_grid())
        root.update()
        time.sleep(1)

if __name__ == '__main__':
    main()
