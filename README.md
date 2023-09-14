# Exam Project "Leuphana Pixelart" in Agents and Interfaces

This project contains: 
- the code for a specific pixelart design called leuphana_pixelart
- a script where the colors for each row are saved separately called leuphana_pixelcolors
- a report pdf to this project

## To start:

Open PyCharm, activate a virtual environment in your PyCharm terminal and install Tkinter.
Next, create a new folder, where you will add both Python scripts from this 
project: leuphana_pixelart.py and leuphana_pixelcolors.py. Or clone this repository. If you now
run the leuphana_pixelart Python Script, the turtle should draw this: 

![pixelart_result](https://github.com/jessiiimai/leuph_agents_interfaces/assets/136825243/2281ce91-43cf-46e4-9b25-24593ccae7c4)

In the following, I will explain what both scripts contain in detail.

## Recreating the code

To create this Pixelart with Turtle, we will start with importing turtle, 
our drawing tool for the pixels, and define its settings. For the best
result, it is advised to copy these settings.

```python

import turtle

turtle.Screen().setup(width=750, height=550, startx=0, starty=0)

t = turtle.Turtle()
t.speed(0)
turtle.tracer(0)  # This turns off the animation, otherwise the turtle would take too long to draw.

# This sends the turtle to its starting point. 
t.penup()
t.goto(-350, -240)
t.pendown()
```

Next, we need a function to create one pixel with Turtle. For that, we
also need to define our side_length variable which ultimately defines
the size of our pixels. You should use "5" in this case, so that the 
pixel size and screensize match later. 

```python
side_length = 5

def create_square(t, side_length, color):
    t.color(color)
    t.begin_fill()
    for num in range(4):
        t.forward(side_length)
        t.right(90)
    t.end_fill()
    t.forward(side_length)
```

After that, we create a function that draws a whole row of our 
pixels based on the length of a list, we defined our colors in. 

```python
def create_row(t, side_length, color_list):
    t.penup()
    t.left(90)
    t.forward(side_length)
    t.left(90)
    t.forward(side_length * len(color_list))
    t.right(180)
    t.pendown()
```

The color list this and the following code refer to is saved as a matrix
in the leuphana_pixelcolors script. Please copy it from there, as it is 
very long. It is basically a list called "matrix",
that contains a list of colors for each row of the image. So every
pixel is defined in this matrix essentially. We add a 
function after the matrix, so that we can later return the matrix in our
leuphana_pixelart script. 

```python
def get_matrix():
    return matrix
```

Back in our leuphana_pixelart script, we call the matrix, so that it 
returns the colors for our rows. 

```python
color_matrix = get_matrix()[::-1]
```
Last but not least, we let our Turtle iterate through each list inside
the matrix to create a row out of every color in each list.

```python
# l stands for each list in the matrix, c stands for each color in each list.

for l in color_matrix:
    for c in l:
        create_square(t, side_length, c)
        turtle.update()  # This makes the animation of the Turtle periodically visible again.
    create_row(t, side_length, l)


turtle.done()
```

And to explain one last detail: The speed of the animation of the Turtle.
As the Turtle has to draw many pixels in this artwork, it takes a long
time to finish, even if you let it go at its fastest speed which would
be t.speed(0). So to make it even faster, we turn off the animation 
completely with turtle.tracer(0). But then the picture just appears
without the signature movements of the turtle, which is a bit sad. So 
to make the animation visible shortly, we let the turtle update 
everytime after it creates a square with turtle.update(). So now, we have
a bit of an animated gradual appearance of the picture. 

And that's it! Now you should be able to generate the picture from the
beginning. 
