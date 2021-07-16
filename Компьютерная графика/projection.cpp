#include <iostream>
#include <GL/glut.h>
#include <cmath>


float dl = 4;

GLfloat  p = 0.1f, q = 0.1f;

GLfloat mat[4][4], v[3];

float Matrix[16];
float q_w = 1, q_x = 1, q_y = 1, q_z = 1;



void Mt(float q_x, float q_y, float q_z, float q_w)

	{
	
	Matrix[0] = 1 - 2 * (q_y * q_y + q_z * q_z);       
	Matrix[1] = 2 * (q_x * q_y - q_z * q_w);   
    	Matrix[2] = 2 * (q_x * q_z + q_y * q_w);   
    	Matrix[3] = 0.0;
 
	Matrix[4] = 2 * (q_x * q_y + q_z * q_w);       
    	Matrix[5] = 1 - 2 * (q_x * q_x + q_z * q_z);       
    	Matrix[6] = 2 * (q_y * q_z - q_x * q_w);       
    	Matrix[7] = 0.0;
 
    	Matrix[8] = 2 * (q_x * q_z - q_y * q_w);   
    	Matrix[9] = 2 * (q_y * q_z + q_x * q_w);   
    	Matrix[10] = 1 - 2 * (q_x * q_x + q_y * q_y);      
    	Matrix[11] = 0.0;
 
    	Matrix[15] = 1.0;



	}


void Rot(float _x, float _y, float _z, float _w)
{
	
	float angle;
    	angle = (_w / 180.0f) * M_PI; 
    	float result = sin( angle / 2.0f );
 
    	q_w = cos( angle / 2.0f );
   	q_x = _x * result;
    	q_y = _y * result;
    	q_z = _z * result;
	float module = sqrt(pow(q_w,2)+pow(q_x,2)+pow(q_y,2)+pow(q_z,2));
	q_w = cos( angle / 2.0f )/module;
   	q_x = _x * result/module;
    	q_y = _y * result/module;
    	q_z = _z * result/module;

}




void proj()
{
	
	mat[0][0] = 1.0f;
	mat[1][1] = 1.0f;
	mat[3][3] = 1.0f;
	mat[0][3] = p;
	mat[1][3] = q;
	mat[0][1] = 0.0f;
	mat[0][2] = 0.0f;
	mat[1][0] = 0.0f;
	mat[1][2] = 0.0f;
	mat[2][0] = 0.0f;
	mat[2][1] = 0.0f;
	mat[2][2] = 0.0f;
	mat[2][3] = 0.0f;
	mat[3][0] = 0.0f;
	mat[3][1] = 0.0f;
	mat[3][2] = 0.0f;
	v[0] = 5.0f;
	v[1] = 4;
	v[2] = 2;



}






void internalEdgesLines(float x0, float y0, float z0)
{	
	
	float x[8], y[8], z[8];
	x[0] = x0 + dl; y[0] = y0 + dl; z[0] = z0;
	x[1] = x0 + dl; y[1] = y0 + 2*dl; z[1] = z0;
	x[2] = x0 + 2*dl; y[2] = y0 + dl; z[2] = z0;
	x[3] = x0 + 2*dl; y[3] = y0 + 2*dl; z[3] = z0;
	x[4] = x0 + dl; y[4] = y0 + dl; z[4] = z0 + dl;
	x[5] = x0 + dl; y[5] = y0 + 2*dl; z[5] = z0 + dl;
	x[6] = x0 + 2*dl; y[6] = y0 + dl; z[6] = z0 + dl;
	x[7] = x0 + 2*dl; y[7] = y0 + 2*dl; z[7] = z0 + dl;
	

	glBegin(GL_LINE_STRIP);
	glVertex3f(x[0], y[0] - dl, z[0]);
	glVertex3f(x[0], y[0], z[0]);
	glVertex3f(x[0] - dl, y[0], z[0]);
	glVertex3f(x[0], y[0], z[0]);
	glVertex3f(x[0], y[0], z[0] - dl);
	glEnd();

	glBegin(GL_LINE_STRIP);
	glVertex3f(x[1], y[1] + dl, z[1]);
	glVertex3f(x[1], y[1], z[1]);
	glVertex3f(x[1] - dl, y[1], z[1]);
	glVertex3f(x[1], y[1], z[1]);
	glVertex3f(x[1], y[1], z[1] - dl);
	glEnd();

	glBegin(GL_LINE_STRIP);
	glVertex3f(x[2], y[2] - dl, z[2]);
	glVertex3f(x[2], y[2], z[2]);
	glVertex3f(x[2] + dl, y[2], z[2]);
	glVertex3f(x[2], y[2], z[2]);
	glVertex3f(x[2], y[2], z[2] - dl);
	glEnd();
	
	glBegin(GL_LINE_STRIP);
	glVertex3f(x[3], y[3] + dl, z[3]);
	glVertex3f(x[3], y[3], z[3]);
	glVertex3f(x[3] + dl, y[3], z[3]);
	glVertex3f(x[3], y[3], z[3]);
	glVertex3f(x[3], y[3], z[3] - dl);
	glEnd();
	

	glBegin(GL_LINE_STRIP);
	glVertex3f(x[5], y[5] + dl, z[5]);
	glVertex3f(x[5], y[5], z[5]);
	glVertex3f(x[5] - dl, y[5], z[5]);
	glVertex3f(x[5], y[5], z[5]);
	glVertex3f(x[5], y[5], z[5] + dl);
	glEnd();

	glBegin(GL_LINE_STRIP);
	glVertex3f(x[4], y[4] - dl, z[4]);
	glVertex3f(x[4], y[4], z[4]);
	glVertex3f(x[4] - dl, y[4], z[4]);
	glVertex3f(x[4], y[4], z[4]);
	glVertex3f(x[4], y[4], z[4] + dl);
	glEnd();

	glBegin(GL_LINE_STRIP);
	glVertex3f(x[6], y[6] - dl, z[6]);
	glVertex3f(x[6], y[6], z[6]);
	glVertex3f(x[6] + dl, y[6], z[6]);
	glVertex3f(x[6], y[6], z[6]);
	glVertex3f(x[6], y[6], z[6] + dl);
	glEnd();

	glBegin(GL_LINE_STRIP);
	glVertex3f(x[7], y[7] + dl, z[7]);
	glVertex3f(x[7], y[7], z[7]);
	glVertex3f(x[7] + dl, y[7], z[7]);
	glVertex3f(x[7], y[7], z[7]);
	glVertex3f(x[7], y[7], z[7] + dl);
	glEnd();
	
}



void crossXLines(int x0, int y0, int z0)
{
	glBegin(GL_LINE_STRIP);
	glVertex3f(x0, y0, z0);
	glVertex3f(x0, y0 + dl, z0);
	glVertex3f(x0, y0 + dl, z0 + dl);
	glVertex3f(x0, y0 + 2*dl, z0 + dl);
	glVertex3f(x0, y0 + 2*dl, z0);
	glVertex3f(x0, y0 + 3*dl, z0);
	glVertex3f(x0, y0 + 3*dl, z0 - dl);
	glVertex3f(x0, y0 + 2*dl, z0 - dl);
	glVertex3f(x0, y0 + 2*dl, z0 -2*dl);
	glVertex3f(x0, y0 + dl, z0 -2*dl);
	glVertex3f(x0, y0 + dl, z0 -dl);
	glVertex3f(x0, y0, z0-dl);
	glVertex3f(x0, y0, z0);
	glEnd();
}


void crossYLines(int x0, int y0, int z0) {
	glBegin(GL_LINE_STRIP);
	glVertex3f(x0, y0, z0);
	glVertex3f(x0, y0 , z0 + dl);
	glVertex3f(x0  - dl, y0, z0 + dl);
	glVertex3f(x0  - dl, y0 , z0 + 2*dl);
	glVertex3f(x0, y0 , z0 + 2*dl);
	glVertex3f(x0, y0 , z0 + 3*dl);
	glVertex3f(x0 + dl, y0, z0 + 3*dl);
	glVertex3f(x0 + dl, y0 , z0 + 2*dl);
	glVertex3f(x0 + 2*dl, y0 , z0 + 2*dl);
	glVertex3f(x0 + 2*dl, y0 , z0 + dl);
	glVertex3f(x0 + dl, y0 , z0 + dl);
	glVertex3f(x0 + dl, y0, z0);
	glVertex3f(x0, y0, z0);
	glEnd();


}

void crossZLines(int x0, int y0, int z0) {
	glBegin(GL_LINE_STRIP);
	//glColor3f(1.0f, 0.0f, 0.0f);
	glVertex3f(x0, y0, z0);
	glVertex3f(x0, y0 + dl, z0);
	glVertex3f(x0 - dl, y0 + dl, z0);
	glVertex3f(x0 - dl, y0 + 2*dl, z0);
	glVertex3f(x0, y0 + 2*dl, z0);
	glVertex3f(x0, y0 + 3*dl, z0);
	glVertex3f(x0 + dl, y0 + 3*dl, z0);
	glVertex3f(x0 + dl, y0 + 2*dl, z0);
	glVertex3f(x0 + 2*dl, y0 + 2*dl, z0);
	glVertex3f(x0 + 2*dl, y0 + dl, z0);
	glVertex3f(x0 + dl, y0 + dl, z0);
	glVertex3f(x0 + dl, y0, z0);
	glVertex3f(x0, y0, z0);
	glEnd();
}

void internalEdges(float x0, float y0, float z0)
{
	
	float x[8], y[8], z[8];
	x[0] = x0 + dl + 0.01; y[0] = y0 + dl + 0.01; z[0] = z0 + 0.01;
	x[1] = x0 + dl + 0.01; y[1] = y0 + 2*dl - 0.01; z[1] = z0 + 0.01;
	x[2] = x0 + 2*dl - 0.01; y[2] = y0 + dl + 0.01; z[2] = z0 + 0.01;
	x[3] = x0 + 2*dl -0.01; y[3] = y0 + 2*dl - 0.01; z[3] = z0 + 0.01;
	x[4] = x0 + dl + 0.01; y[4] = y0 + dl + 0.01; z[4] = z0 + dl - 0.01;
	x[5] = x0 + dl + 0.01; y[5] = y0 + 2*dl - 0.01; z[5] = z0 + dl - 0.01;
	x[6] = x0 + 2*dl - 0.01; y[6] = y0 + dl + 0.01; z[6] = z0 + dl - 0.01;
	x[7] = x0 + 2*dl - 0.01; y[7] = y0 + 2*dl - 0.01; z[7] = z0 + dl - 0.01;
	
	dl = 3.95;

	glBegin(GL_QUADS);
	glVertex3f(x[0], y[0], z[0] - dl);
	glVertex3f(x[0], y[0], z[0]);
	glVertex3f(x[0], y[0] - dl, z[0]);
	glVertex3f(x[0], y[0] - dl, z[0] - dl);

	glVertex3f(x[0] - dl, y[0], z[0]);
	glVertex3f(x[0], y[0], z[0]);
	glVertex3f(x[0], y[0] - dl, z[0]);
	glVertex3f(x[0] - dl, y[0] - dl, z[0]);

	glVertex3f(x[0] - dl, y[0], z[0]);
	glVertex3f(x[0], y[0], z[0]);
	glVertex3f(x[0], y[0] , z[0] - dl);
	glVertex3f(x[0] - dl, y[0], z[0]  - dl);
	glEnd();

	glBegin(GL_QUADS);
	glVertex3f(x[1], y[1], z[1] - dl);
	glVertex3f(x[1], y[1], z[1]);
	glVertex3f(x[1], y[1] + dl, z[1]);
	glVertex3f(x[1], y[1] + dl, z[1] - dl);

	glVertex3f(x[1], y[1], z[1] - dl);
	glVertex3f(x[1], y[1], z[1]);
	glVertex3f(x[1] - dl, y[1], z[1]);
	glVertex3f(x[1] - dl, y[1], z[1] - dl);

	glVertex3f(x[1]  - dl, y[1], z[1]);
	glVertex3f(x[1], y[1], z[1]);
	glVertex3f(x[1], y[1] + dl, z[1]);
	glVertex3f(x[1] - dl, y[1] + dl, z[1]);
	glEnd();

	glBegin(GL_QUADS);
	glVertex3f(x[2], y[2] - dl, z[2]);
	glVertex3f(x[2], y[2], z[2]);
	glVertex3f(x[2] + dl, y[2], z[2]);
	glVertex3f(x[2]+ dl, y[2] - dl, z[2]);

	glVertex3f(x[2], y[2] - dl, z[2]);
	glVertex3f(x[2], y[2], z[2] - dl);
	glVertex3f(x[2], y[2], z[2]);
	glVertex3f(x[2], y[2] - dl, z[2] - dl);
	
	glVertex3f(x[2], y[2] , z[2] - dl);
	glVertex3f(x[2] + dl, y[2], z[2] );
	glVertex3f(x[2], y[2], z[2]);
	glVertex3f(x[2] + dl, y[2], z[2] - dl);
	
	glEnd();
	
	glBegin(GL_QUADS);
	glVertex3f(x[3], y[3] + dl, z[3]);
	glVertex3f(x[3], y[3], z[3]);
	glVertex3f(x[3] + dl, y[3], z[3]);
	glVertex3f(x[3] + dl, y[3] + dl, z[3]);

	glVertex3f(x[3], y[3] + dl, z[3]);
	glVertex3f(x[3], y[3], z[3] - dl);
	glVertex3f(x[3], y[3], z[3]);
	glVertex3f(x[3], y[3] + dl, z[3] - dl);

	glVertex3f(x[3] + dl, y[3], z[3]);
	glVertex3f(x[3], y[3], z[3] - dl);
	glVertex3f(x[3], y[3], z[3]);
	glVertex3f(x[3] + dl, y[3], z[3] - dl);
	
	glEnd();
	

	glBegin(GL_QUADS);
	glVertex3f(x[4], y[4] - dl, z[4]);
	glVertex3f(x[4], y[4], z[4]);
	glVertex3f(x[4] - dl, y[4], z[4]);
	glVertex3f(x[4] - dl, y[4] - dl, z[4]);
	
	glVertex3f(x[4], y[4] - dl, z[4]);
	glVertex3f(x[4], y[4], z[4]);
	glVertex3f(x[4], y[4], z[4] + dl);
	glVertex3f(x[4], y[4] - dl, z[4] + dl);

	glVertex3f(x[4] - dl, y[4], z[4]);
	glVertex3f(x[4], y[4], z[4]);
	glVertex3f(x[4], y[4], z[4] + dl);
	glVertex3f(x[4]- dl, y[4], z[4] + dl);
	glEnd();

	glBegin(GL_QUADS);
	glVertex3f(x[5], y[5] + dl, z[5]);
	glVertex3f(x[5], y[5], z[5]);
	glVertex3f(x[5] - dl, y[5], z[5]);
	glVertex3f(x[5] - dl, y[5] + dl, z[5]);
	
	glVertex3f(x[5], y[5] + dl, z[5]);
	glVertex3f(x[5], y[5], z[5]);
	glVertex3f(x[5], y[5], z[5] + dl);
	glVertex3f(x[5], y[5] + dl, z[5] + dl);

	glVertex3f(x[5] - dl, y[5], z[5]);
	glVertex3f(x[5], y[5], z[5]);
	glVertex3f(x[5], y[5], z[5] + dl);
	glVertex3f(x[5]- dl, y[5], z[5] + dl);
	
	glEnd();

	glBegin(GL_QUADS);
	glVertex3f(x[6], y[6] - dl, z[6]);
	glVertex3f(x[6], y[6], z[6]);
	glVertex3f(x[6] + dl, y[6], z[6]);
	glVertex3f(x[6] + dl, y[6] - dl, z[6]);

	glVertex3f(x[6], y[6] - dl, z[6]);
	glVertex3f(x[6], y[6], z[6]);
	glVertex3f(x[6], y[6], z[6] + dl);
	glVertex3f(x[6], y[6] - dl, z[6] + dl);

	glVertex3f(x[6]  + dl, y[6], z[6]);
	glVertex3f(x[6], y[6], z[6]);
	glVertex3f(x[6], y[6], z[6] + dl);
	glVertex3f(x[6]  + dl, y[6], z[6] + dl);
	
	glEnd();

	glBegin(GL_QUADS);
	glVertex3f(x[7], y[7] + dl, z[7]);
	glVertex3f(x[7], y[7], z[7]);
	glVertex3f(x[7] + dl, y[7], z[7]);
	glVertex3f(x[7] + dl, y[7] + dl, z[7]);

	glVertex3f(x[7], y[7] + dl, z[7]);
	glVertex3f(x[7], y[7], z[7]);
	glVertex3f(x[7], y[7], z[7] + dl);
	glVertex3f(x[7], y[7] + dl, z[7] + dl);

	glVertex3f(x[7] + dl, y[7], z[7]);
	glVertex3f(x[7], y[7], z[7]);
	glVertex3f(x[7], y[7], z[7] + dl);
	glVertex3f(x[7] + dl, y[7], z[7] + dl);
	glEnd();

	dl = 4;

}



void crossX(int x0, int y0, int z0)
{
	glBegin(GL_QUADS);

	glVertex3f(x0, y0, z0);
	glVertex3f(x0, y0 + dl, z0);
	glVertex3f(x0, y0 + dl, z0 + dl);
	glVertex3f(x0, y0, z0 + dl);

	glVertex3f(x0, y0 + dl, z0);
	glVertex3f(x0, y0 + dl, z0 - dl);
	glVertex3f(x0, y0 + 2*dl, z0 - dl);
	glVertex3f(x0, y0 + 2*dl, z0);

	glVertex3f(x0, y0 + dl, z0);
	glVertex3f(x0, y0 + dl, z0 + dl);
	glVertex3f(x0, y0 + 2*dl, z0 + dl);
	glVertex3f(x0, y0 + 2*dl, z0);

	glVertex3f(x0, y0 + dl, z0 + dl);
	glVertex3f(x0, y0 + dl, z0 + 2*dl);
	glVertex3f(x0, y0 + 2*dl, z0 + 2*dl);
	glVertex3f(x0, y0 + 2*dl, z0 + dl);

	glVertex3f(x0, y0 + 2*dl, z0);
	glVertex3f(x0, y0 + 2*dl, z0 + dl);
	glVertex3f(x0, y0 + 3*dl, z0 + dl);
	glVertex3f(x0, y0 + 3*dl, z0);

	
	glEnd();
}


void crossY(int x0, int y0, int z0) {
	glBegin(GL_QUADS);
	glVertex3f(x0, y0, z0);
	glVertex3f(x0 + dl, y0 , z0);
	glVertex3f(x0 + dl, y0, z0 + dl);
	glVertex3f(x0, y0, z0 + dl);

	glVertex3f(x0, y0 , z0 + dl);
	glVertex3f(x0 - dl, y0, z0 + dl );
	glVertex3f(x0 - dl, y0, z0 + 2*dl);
	glVertex3f(x0, y0 , z0 + 2*dl);

	glVertex3f(x0, y0 , z0 + dl);
	glVertex3f(x0 + dl, y0 , z0 + dl);
	glVertex3f(x0 + dl, y0, z0  + 2*dl);
	glVertex3f(x0, y0, z0  + 2*dl);

	glVertex3f(x0 + dl, y0, z0 + dl);
	glVertex3f(x0 + dl, y0, z0 + 2*dl);
	glVertex3f(x0 + 2*dl, y0, z0 + 2*dl);
	glVertex3f(x0 + 2*dl, y0, z0 + dl);

	glVertex3f(x0, y0, z0 + 2*dl);
	glVertex3f(x0 + dl, y0 , z0 + 2*dl);
	glVertex3f(x0 + dl, y0 , z0 + 3*dl);
	glVertex3f(x0, y0 , z0 + 3*dl);
	glEnd();


}

void crossZ(int x0, int y0, int z0) {
	glBegin(GL_QUADS);

	glVertex3f(x0, y0, z0);
	glVertex3f(x0, y0 + dl, z0);
	glVertex3f(x0 + dl, y0 + dl, z0);
	glVertex3f(x0 + dl, y0, z0);

	glVertex3f(x0, y0 + dl, z0);
	glVertex3f(x0 - dl, y0 + dl, z0);
	glVertex3f(x0 - dl, y0 + 2*dl, z0);
	glVertex3f(x0, y0 + 2*dl, z0);

	glVertex3f(x0, y0 + dl, z0);
	glVertex3f(x0 + dl, y0 + dl, z0);
	glVertex3f(x0 + dl, y0 + 2*dl, z0);
	glVertex3f(x0, y0 + 2*dl, z0);

	glVertex3f(x0 + dl, y0 + dl, z0);
	glVertex3f(x0 + 2*dl, y0 + dl, z0);
	glVertex3f(x0 + 2*dl, y0 + 2*dl, z0);
	glVertex3f(x0 + dl, y0 + 2*dl, z0);

	glVertex3f(x0, y0 + 2*dl, z0);
	glVertex3f(x0 + dl, y0 + 2*dl, z0);
	glVertex3f(x0 + dl, y0 + 3*dl, z0);
	glVertex3f(x0, y0 + 3*dl, z0);

	
	glEnd();

}


void init()
{	
	
	glClearColor (1, 0, 0, 1.0);
	glMatrixMode (GL_PROJECTION);
	glLoadIdentity();
	glOrtho(-15, 15, -15, 15, -15, 15);
	
	

}

void Cube(int x0, int y0, int z0) {
glColor3d(1, 0, 1);	

	//glColor3d(0, 0, 0);
	crossX(x0, y0, z0);
	crossX(x0 +3*dl, y0, z0);
	crossY(x0+dl, y0, z0 - dl);
	crossY(x0+dl, y0+3*dl, z0-dl);
	crossZ(x0+dl, y0, z0-dl);
	crossZ(x0+dl, y0, z0+2*dl);

//	internalEdges(x0, y0, z0); 
	
	
	
	

	
	glColor3d(0.5, 1, 0.3);

	internalEdges(x0, y0, z0);
	glColor3d(1, 1, 1);

	internalEdgesLines(x0, y0, z0);


	glColor3d(1, 1, 1);
	crossXLines(x0, y0, z0 + dl);
	crossXLines(x0 + 3*dl, y0, z0 + dl);
	crossYLines(x0 + dl, y0, z0 - dl);
	crossYLines(x0 + dl, y0 + 3*dl, z0 - dl);
	crossZLines(x0 + dl, y0, z0 - dl);
	crossZLines(x0 + dl, y0, z0 + 2*dl);

}



void Draw()
{
	
	glEnable(GL_DEPTH_TEST);
	glDepthFunc(GL_LEQUAL);
	
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	proj();
	glMultMatrixf(*mat);	
	Rot(1, 1, 0, 90);
	Mt(q_x, q_y, q_z, q_w);
	glMultMatrixf(Matrix);
	
	Cube(0, 0, 0);
	
//	Cube(0 + 3*dl, 0, 0);
//	Cube(0 - 3*dl, 0, 0);
//	Cube(0, 0 + 3*dl, 0);
//	Cube(0, 0 - 3*dl, 0);
	glutSwapBuffers();


}


int main(int argc, char **argv) {

	

	glutInit(&argc, argv);
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
        glutInitWindowPosition(400, 400);
        glutInitWindowSize(500, 500);
        glutCreateWindow("Figure");
	
	init();
	glutDisplayFunc(Draw);
	
        glutMainLoop();
	return 0;
} 	    