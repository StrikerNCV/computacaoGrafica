void setup() {
  size(640, 360);
}

void draw() {
  background(10);
  
  pushMatrix();
  translate(width*0.5, height*0.5);
  rotate(frameCount / -100.0);
  star(0, 0, 30, 70, 5); 
  popMatrix();
}

void star(float x, float y, float raio1, float raio2, int npontas) {
  float angulo = TWO_PI / npontas;
  float metAng = angulo/2.0;
  beginShape();
  for (float a = 0; a < TWO_PI; a += angulo) {
    float sx = x + cos(a) * raio2;
    float sy = y + sin(a) * raio2;
    vertex(sx, sy);
    sx = x + cos(a+metAng) * raio1;
    sy = y + sin(a+metAng) * raio1;
    vertex(sx, sy);
  }
  endShape(CLOSE);
}
