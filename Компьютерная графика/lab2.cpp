#include <iostream>
#include <GL/glut.h>
#include <cmath>


void Draw() {
	glClear(GL_COLOR_BUFFER_BIT);

	glColor3d(0, 0.749, 1);
	glBegin(GL_QUADS);
		glVertex2f(0.0, 20.0);
		glVertex2f(0, 30);
		glVertex2f(30, 30);
		glVertex2f(30, 20);

	glEnd();

	glColor3d(1, 1, 0);
	glBegin(GL_QUADS);
		glVertex2f(25, 29);
		glVertex2f(29, 28);
		glVertex2f(28, 24);
		glVertex2f(24, 25);

	glEnd();
	
	glColor3d(0.678, 0.647, 0.529);
	glBegin(GL_TRIANGLES);
		glVertex2f(0, 17);
		glVertex2f(16, 17);
		glVertex2f(8, 29);

		glVertex2f(-3, 15);
		glVertex2f(11, 15);
		glVertex2f(4, 25);
		glColor3f(0.949, 0.952, 0.956);

		glVertex2f(6, 26);
		glVertex2f(8, 25);
		glVertex2f(8, 29);

		glVertex2f(8, 23);
		glVertex2f(8, 29);
		glVertex2f(10, 26);

		glVertex2f(2, 22);
		glVertex2f(4, 21);
		glVertex2f(4, 25);

		glVertex2f(4, 25);
		glVertex2f(4, 20);
		glVertex2f(6, 22);

		glColor3f(0.07, 0.039, 0.561);
		glVertex2f(20, 20);
		glVertex2f(30, 20);
		glVertex2f(30, 13);
		
		


		
	glEnd();


        glColor3d(0.49, 0.33, 0.16);
	//glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
	glBegin(GL_TRIANGLE_STRIP);	
		glVertex2f(25.0, 1.0);	
		glVertex2f(23.0, 3.0);
		glVertex2f(25.0, 4.0);
		glVertex2f(23.0, 6.0);
		glVertex2f(25.0, 8.0);
		glVertex2f(22.0, 10.0);
		glVertex2f(23.0, 12.0);
		glVertex2f(19.0, 13.0);	
	glEnd();
	glBegin(GL_TRIANGLE_STRIP);
		glVertex2f(22.0, 10.0);
		glVertex2f(19.0, 13.0);
		glVertex2f(18.0, 9.0);
		glVertex2f(15.0, 12.0);
		glVertex2f(15.0, 7.0);
		glVertex2f(12.0, 10.0);
		glVertex2f(11.0, 8.0);
		glVertex2f(8.0, 11.0);
	glEnd();
	glBegin(GL_TRIANGLE_STRIP);
		glVertex2f(15.0, 7.0);
		glVertex2f(18.0, 9.0);
		glVertex2f(20.0, 7.0);
		glVertex2f(22.0, 10.0);
		glVertex2f(23.0, 6.0);
	glEnd();
	
	glBegin(GL_TRIANGLE_STRIP);
		glVertex2f(13.0, 1.0);
		glVertex2f(11.0, 8.0);
		glVertex2f(13.0, 5.0);
		glVertex2f(15.0, 7.0);
		glVertex2f(13.0, 1.0);
	glEnd();
	
	glBegin(GL_TRIANGLE_STRIP);
		glVertex2f(15.0, 12.0);
		glVertex2f(12.0, 10.0);
		glVertex2f(10.0, 13.0);
		glVertex2f(8.0, 11.0);
		glVertex2f(7.0, 15.6);
		glVertex2f(5.0, 14.0);	
	glEnd();

	glBegin(GL_TRIANGLE_STRIP);
		glVertex2f(2.0, 17.0);
		glVertex2f(5.0, 14.0);
		glVertex2f(6.0, 16.0);
		glVertex2f(7.5, 16.0);
		glVertex2f(7.5, 17.5);
		glVertex2f(10, 16.0);
		glVertex2f(13, 15);
	
	glEnd();

	glColor3d(0, 0, 0);
	glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
	glBegin(GL_TRIANGLE_STRIP);	
		glVertex2f(25.0, 1.0);	
		glVertex2f(23.0, 3.0);
		glVertex2f(25.0, 4.0);
		glVertex2f(23.0, 6.0);
		glVertex2f(25.0, 8.0);
		glVertex2f(22.0, 10.0);
		glVertex2f(23.0, 12.0);
		glVertex2f(19.0, 13.0);	
	glEnd();
	glBegin(GL_TRIANGLE_STRIP);
		glVertex2f(22.0, 10.0);
		glVertex2f(19.0, 13.0);
		glVertex2f(18.0, 9.0);
		glVertex2f(15.0, 12.0);
		glVertex2f(15.0, 7.0);
		glVertex2f(12.0, 10.0);
		glVertex2f(11.0, 8.0);
		glVertex2f(8.0, 11.0);
	glEnd();
	glBegin(GL_TRIANGLE_STRIP);
		glVertex2f(15.0, 7.0);
		glVertex2f(18.0, 9.0);
		glVertex2f(20.0, 7.0);
		glVertex2f(22.0, 10.0);
		glVertex2f(23.0, 6.0);
	glEnd();
	
	glBegin(GL_TRIANGLE_STRIP);
		glVertex2f(13.0, 1.0);
		glVertex2f(11.0, 8.0);
		glVertex2f(13.0, 5.0);
		glVertex2f(15.0, 7.0);
		glVertex2f(13.0, 1.0);
	glEnd();
	
	glBegin(GL_TRIANGLE_STRIP);
		glVertex2f(15.0, 12.0);
		glVertex2f(12.0, 10.0);
		glVertex2f(10.0, 13.0);
		glVertex2f(8.0, 11.0);
		glVertex2f(7.0, 15.6);
		glVertex2f(5.0, 14.0);	
	glEnd();

	glBegin(GL_TRIANGLE_STRIP);
		glVertex2f(2.0, 17.0);
		glVertex2f(5.0, 14.0);
		glVertex2f(6.0, 16.0);
		glVertex2f(7.5, 16.0);
		glVertex2f(7.5, 17.5);
		glVertex2f(10, 16.0);
		glVertex2f(13, 15);
	
	glEnd();
	
	
	

	glFlush();

	





}





int main(int argc, char **argv) {
	glutInit(&argc, argv);
        glutInitDisplayMode(GLUT_RGB);
        glutInitWindowPosition(400, 400);
        glutInitWindowSize(500, 500);
        glutCreateWindow("figure");
	glClearColor (0.941, 0.501, 0.125, 0.0);
	glMatrixMode (GL_PROJECTION);
	gluOrtho2D(0.0, 30, 0.0, 30.0);
	glutDisplayFunc(Draw);
	
        glutMainLoop();
	return 0;
} 