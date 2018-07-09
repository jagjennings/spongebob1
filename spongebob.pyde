def setup():
    size(600, 700)
    fill(227,207,87)                               # fill head yellow
    rect(240, 100, 200, 240)                       # make face
    quad(200, 60, 400, 60, 440, 100, 240, 100)     # top of 3D head
    quad(200, 60, 240, 100, 240, 340, 200, 300)    # left side of 3D head
    
    fill(255, 255, 255)                            # fill eyes white
    ellipse(370, 170, 75, 95)                      # make right eye
    ellipse(310, 170, 75, 95)                      # make left eye
    fill(0, 255, 255)                              # make irises light blue
    ellipse(365, 170, 25, 33)                      # make right iris
    ellipse(310, 170, 25, 33)                      # make left iris
    fill(0, 0, 0)                                  # make pupils black
    ellipse(365, 170, 10, 13)                      # make right pupil
    ellipse(310, 170, 10, 13)                      # make left pupil
    fill(255, 255, 255)                            # fill eye sparkle
    noStroke()
    ellipse(370, 165, 7, 7)                        # make right eye sparkle
    ellipse(315, 165, 7, 7)                        # make left eye sparkle
    
    stroke(0)
    fill(227,207,87)
    bezier(340, 220, 355, 220, 387, 195, 390, 217) # make top of nose
    bezier(340, 233, 355, 235, 389, 235, 390, 217) # make bottom of nose
    
    fill(139, 35, 35)                              # fill mouth inside red
    bezier(290, 225, 310, 350, 369, 330, 375, 240) # make bottom of mouth
    fill(255, 255, 255)                            # fill teeth white
    rect(315, 237, 25, 30)                         # make left tooth
    rect(350, 240, 25, 27)                         # make left tooth
    fill(227,207,87)                               # fill mouth top yellow
    bezier(290, 224, 310, 240, 350, 255, 390, 241) # make top of mouth
    line(390, 241, 378, 232)                       # connect mouth to nose
    stroke(238, 106, 80)
    bezier(282, 225, 265, 203, 300, 190, 298, 220)
    
    stroke(0)
    fill(255, 255, 255)                            # fill shirt white
    rect(240, 340, 200, 30)                        # make front of shirt
    quad(200, 300, 240, 340, 240, 370, 200, 330)   # make left side of shirt
    triangle(290, 340, 330, 340, 315, 360)         # make left collar
    triangle(345, 340, 385, 340, 365, 358)         # make right collar
    
    fill(138, 54, 15)                              # fill pants brown
    rect(240, 370, 200, 40)                        # make front of shirt
    quad(200, 330, 240, 370, 240, 410, 200, 370)   # make left side of shirt
    beltWidth = 30
    beltHeight = 10
    fill(0, 0, 0)                                  # fill belt black
    rect(258, 385, beltWidth, beltHeight)
    rect(303, 385, beltWidth, beltHeight)
    rect(348, 385, beltWidth, beltHeight)
    rect(393, 385, beltWidth, beltHeight)
    quad(200, 343, 210, 353, 210, 363, 200, 353)
    quad(230, 373, 240, 383, 240, 393, 230, 383)
    
    
