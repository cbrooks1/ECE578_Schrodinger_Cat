/*
Connections between Arduino and qik 2s9v1:

      Arduino   qik 2s9v1
-------------------------
           5V - VCC
          GND - GND
Digital Pin 2 - TX
Digital Pin 3 - RX
Digital Pin 4 - RESET
*/

#include <SoftwareSerial.h>
#include <PololuQik.h>
#include <Firmata.h>


#define QIK1_ID 9
#define QIK2_ID 9
#define QIK_TX 2
#define QIK_RX 3
#define QIK_RESET 4
#define DEBUG
#define S_DELAY 200
#define L_DELAY 500

PololuQik2s9v1 qik(QIK_TX, QIK_RX, QIK_RESET);

int testIncrement = 0;
int fwd = 2;
int bkd = 3;
int lef = 4;
int rite = 5;
int stp = 6;
void setup()
{
  Serial.begin(115200);
  Serial.println("qik 2s9v1 dual serial motor controller");
  
  qik.init();
  
  Serial.print("Firmware version: ");
  Serial.write(qik.getFirmwareVersion());
  Serial.println();

  pinMode(fwd, INPUT);
  pinMode(bkd, INPUT);
  pinMode(lef, INPUT);
  pinMode(rite, INPUT);
  pinMode(stp, INPUT);
  
}

void demo()
{
  testIncrement++;
    int x ; //movement type: 1 = forward, 2 = backward, 3 = spin left, 4 = spin right, 5 = stop, 6 = right, 7 = left
    if(testIncrement < 200)
    {
      x = 1;
    }
    else if(testIncrement>200 && testIncrement < 400)
    {
      x=5;
    }
    else if(testIncrement > 400 && testIncrement <600)
    {
      x=2;
    }
    else if(testIncrement > 600 && testIncrement <700)
    {
      x=5;
    }
    else if(testIncrement > 700 && testIncrement <1000)
    {
      x=3;
    }
    else if(testIncrement > 1000 && testIncrement <1100)
    {
      x=5;
    }
    else if(testIncrement > 1100 && testIncrement <1400)
    {
      x=4;
    }
    else if(testIncrement > 1400 && testIncrement <1500)
    {
      x=5;
    }
    else if(testIncrement > 1500 && testIncrement <1700)
    {
      x=6;
    }
    else if(testIncrement > 1700 && testIncrement <1800)
    {
      x=5;
    }
    else if(testIncrement > 1800 && testIncrement <2000)
    {
      x=7;
    }
    else
    {
      x = 5;
    }
   #ifdef DEBUG
    Serial.print(F("Data passed: "));
    Serial.print(x);
    Serial.print(F(", "));
    #endif

 if ( x == 1)
  {
   qik.setSpeeds(127, 127);  // M0, M1 forward
   // delay(5);


  #ifdef DEBUG
  Serial.print(F("forward    "));
  #endif
  }
  else if (x == 2)
  {
   qik.setSpeeds(-127, -127);  // M0, M1 backward
   //delay(5);
   
  #ifdef DEBUG
  Serial.print(F("backward    "));
  #endif
  }
  else if (x == 3)
  {
    qik.setSpeeds(127, -127);  // M0, M1 spin right
   //delay(5);

   #ifdef DEBUG
  Serial.print(F("Spin Right    "));
  #endif
  }
  else if (x == 4)
  {
   qik.setSpeeds(-127, 127);  // M0, M1 spin left
   //delay(5);
   
  #ifdef DEBUG
  Serial.print(F("Spin Left    "));
  #endif
  }
   else if (x == 5)
  {
   
  qik.setSpeeds(0, 0);
  //delay(5);
  
  #ifdef DEBUG
  Serial.print(F("Stop    "));
  #endif
  }
  else if (x == 6)
  {
   
  qik.setSpeeds(127, -127);
  //delay(5);
  
  #ifdef DEBUG
  Serial.print(F("Right    "));
  #endif
  }
  else if (x == 7)
  {
   
  qik.setSpeeds(-127, 127);
  //delay(5);
  
  #ifdef DEBUG
  Serial.print(F("left    "));
  #endif
  }
}

void loop()
{
    rstop();
  #ifdef DEBUG
  Serial.print("STARTING MAIN LOOP AND test is: ");
  Serial.print(testIncrement);
  Serial.print("\n");
  #endif
        demo ();
  
       if (digitalRead(fwd) == 1)
          forward ();
          //delay (S_DELAY);
          //rstop ();

       else if (digitalRead(bkd) == 1)
          //delay (S_DELAY)
          backward ();
          //delay (S_DELAY);
          //rstop ();

       else if (digitalRead(rite) == 1)
          //delay (S_DELAY);
          right ();
          //delay (L_DELAY);
          //rstop ();

       else if (digitalRead(lef) == 1)
          //delay (S_DELAY);
          left ();
          //delay (L_DELAY);
         // rstop ();

       else if (digitalRead(stp) == 1)
          rstop ();
          
    //testIncrement = 1;
    #ifdef DEBUG
  Serial.print("FINISHED IF STATEMENT AND test is: ");
  Serial.print(testIncrement);
  Serial.print("\n");
  #endif   
  
/*
  //wheel test code, do not place the bot on the ground for this. This is just to test if all four wheels are functional
   for (int i = 0; i <= 127; i++) 
  {
    qik.setM0Speed(i);
    delay(5);
  }

  for (int i = 127; i >= -127; i--) 
  {
    qik.setM0Speed(i);
    delay(5);
  }

  for (int i = -127; i <= 0; i++)
  {
    qik.setM0Speed(i);
    delay(5);
  }


  for (int i = 0; i <= 127; i++)
  {
    qik.setM1Speed(i);
    delay(5);
  }

  for (int i = 127; i >= -127; i--)
  {
    qik.setM1Speed(i);
    delay(5);
  }

  for (int i = -127; i <= 0; i++)
  {
    qik.setM1Speed(i);
    delay(5);
  }
  */
  // check for errors
  int qikError = qik.getErrors();
  if((qikError & 248) > 0)  // check for errors
  {
    if((qikError & 8) > 0)  // bit 3 set
    {
      Serial.print(F("Data Overrun Error"));
    }
    if((qikError & 16) > 0)  // bit 4 set
    {
      Serial.print(F("Frame Error"));
    }
    if((qikError & 32) > 0)  // bit 5 set
    {
      Serial.print(F("CRC Error"));
    }
    if((qikError & 64) > 0)  // bit 6 set
    {
      Serial.print(F("Format Error"));
    }
    if((qikError & 128) > 0)  // bit 7 set
    {
      Serial.print(F("Timeout"));
    }
    // reset controllers
    digitalWrite(QIK_RESET, LOW);
    delay(5);
    digitalWrite(QIK_RESET, HIGH);
    qikError = 0;  // reset error variable
  } 
}

void forward ()
{
    qik.setSpeeds(127, 127);  // M0, M1 forward

    #ifdef DEBUG
    Serial.print(F("forward    "));
    #endif
}

void backward ()
{
    qik.setSpeeds(-127, -127);  // M0, M1 backward
   
  #ifdef DEBUG
  Serial.print(F("backward    "));
  #endif
}

void left ()
{
    qik.setSpeeds(-127, 127);  // M0, M1 spin left
   
  #ifdef DEBUG
  Serial.print(F("Spin Left    "));
  #endif
}

void right ()
{
    qik.setSpeeds(127, -127);  // M0, M1 spin right

   #ifdef DEBUG
  Serial.print(F("Spin Right    "));
  #endif
}

void rstop ()
{
    qik.setSpeeds(0, 0);  // M0, M1 stop

   #ifdef DEBUG
  Serial.print(F("Stop   "));
  #endif
}
