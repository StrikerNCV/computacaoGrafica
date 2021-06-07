from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *
import math 
import sys


diamRotacao = 0.5

numLados = 7


def tronco_iluminado():
    alt = 3.5
    tamRads = (2*math.pi)/numLados
    raioB = 2
    raioC = 1
    verticeB = []
    verticeC = []

    glPushMatrix()
    glRotatef(-100, 1.0, 0.0, 0.0)
    

    glBegin(GL_POLYGON)
    for i in range(0,numLados):
        x = raioB * math.cos(i*tamRads) - diamRotacao
        y = raioB * math.sin(i*tamRads) - diamRotacao
        verticeB += [ (x,y) ]
        glVertex3f(x, y, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for i in range(0,numLados):
        x = raioC * math.cos(i*tamRads) - diamRotacao
        y = raioC * math.sin(i*tamRads) - diamRotacao
        verticeC += [ (x,y) ]
        
        glVertex3f(x, y, alt)
    glEnd()


    glBegin(GL_QUADS)
    for i in range(0,numLados):
        glNormal3fv(contaNormal( (verticeB[i][0], verticeB[i][1],0.0), (-diamRotacao, -diamRotacao, alt), (verticeB[(i+1)%numLados][0], verticeB[(i+1)%numLados][1], 0.0)))
        glVertex3f(verticeB[i][0], verticeB[i][1], 0.0)
        glVertex3f(verticeC[i][0], verticeC[i][1],alt)
        glVertex3f(verticeC[(i+1)%numLados][0], verticeC[(i+1)%numLados][1],alt)
        glVertex3f(verticeB[(i+1)%numLados][0], verticeB[(i+1)%numLados][1],0.0)
    glEnd()

    glPopMatrix()

def contaNormal(a1, b1, c1):
    x = 0
    y = 1
    z = 2
    v0 = a1
    v1 = b1
    v2 = c1
    U = ( v2[x]-v0[x], v2[y]-v0[y], v2[z]-v0[z] )
    V = ( v1[x]-v0[x], v1[y]-v0[y], v1[z]-v0[z] )
    N = ( (U[y]*V[z]-U[z]*V[y]),(U[z]*V[x]-U[x]*V[z]),(U[x]*V[y]-U[y]*V[x]))
    NLength = sqrt(N[x]*N[x]+N[y]*N[y]+N[z]*N[z])
    return ( N[x]/NLength, N[y]/NLength, N[z]/NLength)

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2, 1, 3, 0)
    tronco_iluminado()
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def reshape(w,h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45,float(w)/float(h), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt( 10, 0, 0, 0, 0, 0, 0, 1, 0 )

def init():
    mat_ambient = (0.4, 0.0, 0.2, 1.0)
    mat_diffuse = (1.0, 0.0, 0.4, 1.0)
    mat_specular = (1.0, 0.5, 0.5, 1.0)
    mat_shininess = (50,)
    light_position = (10.0, 0.0, 0.0, 0.0)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glShadeModel(GL_FLAT)

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(800,600)
    glutCreateWindow("Tronco Iluminado")
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutTimerFunc(50, timer, 1)
    init()
    glutMainLoop()

main()