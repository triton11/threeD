import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

surfaces = {
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
}

def Cube():
    glBegin(GL_QUADS)
    for surface in surfaces:
        glColor3fv((0,1,0))
        for vertex in surface:
            glColor3fv((1,1,1))
            glVertex3fv(verticies[vertex])
    glEnd()


    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv((0,0,1))
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -20)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    glRotate(10, 0, 1, 0)
                if event.key == pygame.K_a:
                    glRotate(10, 0, -1, 0)
                if event.key == pygame.K_s:
                    glRotate(10, 0, 0, -1)
                if event.key == pygame.K_w:
                    glRotate(10, 0, 0, 1)
                if event.key == pygame.K_RIGHT:
                    glTranslate(1,0,0)
                if event.key == pygame.K_LEFT:
                    glTranslate(-1, 0, 0)
                if event.key == pygame.K_UP:
                    glTranslate(0, 0, -1)
                if event.key == pygame.K_DOWN:
                    glTranslate(0, 0, 1)



        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()