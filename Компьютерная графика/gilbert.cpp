#include <iostream>
#include <GL/glut.h>
#include <cmath>

const int p = 7;
int  dl;

double dx[100000], dy[100000];

int j = 0;

void A(int i);
void B(int i);
void C(int i);
void D(int i);




int dlina()
{
	int k = pow(2, p);
	return int(400/(k-1));
}

void linedx() { 
	
	dx[j+1] = dx[j] + dl;
	dy[j+1] = dy[j];
j++;
	}


void olinedx() {
	dx[j+1] = dx[j] - dl;
	dy[j+1] = dy[j];
	j++;

	}	


void linedy() {
	dx[j+1] = dx[j];
	dy[j+1] = dy[j] + dl;
j++;

}



void olinedy() { 
	dx[j+1] = dx[j];
	dy[j+1] = dy[j] - dl;
j++;
}



void A(int i) {
	if (i > 0) {
		D(i-1);
		linedx();
		A(i-1);
		linedy();
		A(i-1);
		olinedx();
		C(i-1);
}}



void B(int i) {
	if (i > 0) {
		C(i-1);
		olinedx();
		B(i-1);
		olinedy();
		B(i-1);
		linedx();
		D(i-1);
}}




void C(int i) {
	if (i > 0) {
		B(i-1);
		olinedy();
		C(i-1);
		olinedx();
		C(i-1);
		linedy();
		A(i-1);
}}




void D(int i) {
	if (i > 0) {
		A(i-1);
		linedy();
		D(i-1);
		linedx();
		D(i-1);
		olinedy();
		B(i-1);
}}



void Draw() {
	int i = 0;
	glClear(GL_COLOR_BUFFER_BIT);
        glColor3d(0.0, 0.0, 1.0);
        glLineWidth(2.0);
	glBegin(GL_LINES);
		while ((dx[i+1]!=0) && (dy[i+1]!=0))   {
			glVertex2d(dx[i], dy[i]);
			glVertex2d(dx[i+1], dy[i+1]);
		i++;
	}
	glEnd();
	glFlush();
}


int main(int argc, char **argv) {
	dx[0] = 50;
	dy[0] = 50;
	dl = dlina();
	glutInit(&argc, argv);
        glutInitDisplayMode(GLUT_RGB);
        glutInitWindowPosition(400, 400);
        glutInitWindowSize(500, 500);
        glutCreateWindow("Fractal");
	glClearColor (1.0, 1.0, 1.0, 0.0);
	glMatrixMode (GL_PROJECTION);
	gluOrtho2D(0.0, 500.0, 0.0, 500.0);
	A(p);	
	glutDisplayFunc(Draw);
	
        glutMainLoop();
	return 0;
} 	    