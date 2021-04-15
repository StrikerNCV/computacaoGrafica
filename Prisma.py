from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

a = 0

cores = ( (1, 1, 0.8),(0.8, 1, 0.9),(0.3, 0.7, 0.6),(0.9, 0.3, 0.8),(0.2, 0.2, 0.8),(0.7, 0.9, 0.4),(0.2, 0.7, 1),(0.8, 0, 0.5) )

def prisma():
    r = 1.8
    N = 6
    H = 4
    pontosBase = []
    pontosTampa = []
    angulo = (2*math.pi)/N

    glPushMatrix()
    glTranslatef(0, -2,0)
    glRotatef(a, 0.0, 1.0, 0.0)
    glRotatef(-110, 1.0, 0.0, 0.0)
    glColor3fv(cores[0])

    glBegin(GL_POLYGON)
    for i in range(0, N):
        x = r * math.cos(i*angulo)
        y = r * math.sin(i*angulo)
        pontosBase += [(x,y)]
        glVertex3f(x, y, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for i in range(0, N):
        w = r * math.cos(i*angulo)
        z = r * math.sin(i*angulo)
        pontosTampa += [(w, z)]
        glVertex3f(w, z, H)
    glEnd()

    glBegin(GL_QUADS)
    for i in range(0, N):
        glColor3fv(cores[(i+1)%len(cores)])
        glVertex3f(pontosBase[i][0], pontosBase[i][1], 0.0)
        glVertex3f(pontosBase[(i+1)%N][0], pontosBase[(i+1)%N][1], 0.0)
        glVertex3f(pontosTampa[(i+1)%N][0], pontosTampa[(i+1)%N][1], H)
        glVertex3f(pontosTampa[i][0], pontosTampa[i][1], H)
        
       
    glEnd()

    glPopMatrix()


def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    prisma()
    a += 1
    glutSwapBuffers()
  
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10, timer, 1)

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800, 600)
glutCreateWindow("Trabalho: Prisma")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0, 0, 0, 1)
gluPerspective(45, 800.0/600.0, 0.1, 100.0)
glTranslatef(0.0, 0.0, -10)
glutTimerFunc(10, timer, 1)
glutMainLoop()



   
