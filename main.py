from browser import document, html, window, alert
import random  #This generates random colors 

def sketch(p): #The 'p' represent a parameter and it is needed. It will be the processing sketch itself. 
  #To do things like background, color
  #background(0) instead of p.background(0)

  def setup():  #setup
    p.createCanvas(1890, 1890)
    p.background(255)
    p.rectMode(p.CENTER)

  def draw(): #draw
    colorlist = ['pink', 'salmon', 'beige', 'tan','coral']
    p.noStroke()
    p.fill(random.choice(colorlist))
    p.ellipse(p.mouseX, p.mouseY, 50, 50)

  def mousePressed(self): #mousePressed
    p.background(0)
  def keyPressed(self): #keyPressed
    if p.key == " ":
      print("ALOHA!")
    
  p.setup = setup
  p.draw = draw
  p.mousePressed = mousePressed
  p.keyPressed = keyPressed

myp5 = window.p5.new(sketch)

