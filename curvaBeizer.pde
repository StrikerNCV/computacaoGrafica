float px1 = 150;
float py1 = 150;

float px2 = 250;
float py2 = 150;

float px3 = 150;
float py3 = 250;

float px4 = 250;
float py4 = 250;

void setup()
{
  size(400,400);
  frameRate(30);
}

void draw(){
background(130);

line (px1,py1,px3,py3);
line (px2,py2,px4,py4);


circle(px1,py1,10);
circle(px2,py2,10);


float tam =8;
rect(px3 - tam / 2, py3, tam, tam);
rect(px4 - tam / 2, py4, tam, tam);



for(float t = 0; t <= 1; t += 0.001)
  {
    double x = px1 * (- Math.pow(t,3) + 3 * Math.pow(t,2) - 3 * t+1) + px3 * (3 * Math.pow(t,3)-6 * Math.pow(t,2) + 3 * t) + px4 * (-3*Math.pow(t,3) + 3 * Math.pow(t,2)) + px2 * (Math.pow(t,3));
    double y = py1 * (- Math.pow(t,3) + 3 * Math.pow(t,2) - 3 * t+1) + py3 * (3 * Math.pow(t,3)-6 * Math.pow(t,2) + 3 * t) + px4 * (-3*Math.pow(t,3) + 3 * Math.pow(t,2)) + py2 * (Math.pow(t,3));
    
    int x2 = (int)x;
    int y2 = (int)y;
    point(x2,y2);
  }
}

void mouseDragged(){
float inter = 15;

boolean hori_px1 = mouseX >= (px1 - inter) && mouseX <= (px1 + inter);
boolean ver_py1 = mouseY >= (py1 - inter) && mouseY <= (py1 + inter);

boolean hori_px2 = mouseX >= (px2 - inter) && mouseX <= (px2 + inter);
boolean ver_py2 = mouseY >= (py2 - inter) && mouseY <= (py2 + inter);

boolean hori_px3 = mouseX >= (px3 - inter) && mouseX <= (px3 + inter);
boolean ver_py3 = mouseY >= (py3 - inter) && mouseY <= (py3 + inter);

boolean hori_px4 = mouseX >= (px4 - inter) && mouseX <= (px4 + inter);
boolean ver_py4 = mouseY >= (py4 - inter) && mouseY <= (py4 + inter);

if (hori_px1 && ver_py1){
  px1 = mouseX;
  py1 = mouseY;
}
else if (hori_px2 && ver_py2){
  px2 = mouseX;
  py2 = mouseY;
}
else if(hori_px3 && ver_py3 && (! hori_px4) || (! ver_py4)){
  px3 = mouseX;
  py3 = mouseY;
}
else if (hori_px4 && ver_py4 && (! hori_px3) || (! ver_py3)){
  px4 = mouseX;
  py4 = mouseY;
}


}
