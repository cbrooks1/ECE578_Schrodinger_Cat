/*
 * ECE 478/578 Robotics I - Fall 2018
 * Project 1 Demo - Arduino Code
 * 
 * Robot: Schrodinger Cat
 * 
 * Team members:
 *    Rakhee Bhojakar
 *    Chelsea Brooks
 *    Erik Fox
 *    Dhakshayini Koppad
 *    Jamie Williams
 * 
 * Description:
 *    This is Arduino code to run the Project 1 demo.
 *    It recieves serial commands from a Raspberry Pi (mounted on the robot)
 *    and calls functions to move the robots omni-wheels and servos.
 */

// Include Statements
// *****************************************
#include <PololuMaestro.h> // For servo controller
#include <SoftwareSerial.h> // For additional serial connections
#include <PololuQik.h>
#ifdef SERIAL_PORT_HARDWARE_OPEN
#define maestroSerial SERIAL_PORT_HARDWARE_OPEN
#else
SoftwareSerial maestroSerial(10, 11);
#endif

// Define statements for demo code
// *****************************************
#define SERIAL_DEBUG 1
#define DEBUG 1
#define PI_CONNECTED_PIN A0
#define CHANNEL_NUMBER 12 // Channel number used to talk to maestro
#define RESET_PIN 13 // Pin on Arduino used to talk to maestro
#define DELAY 2000 // Define standard delay

// Define statements for servo control
#define NUM_CHANNELS 18 // Number of servo channels used on the maestro

// Define statements for wheel control
#define QIK1_ID 9
#define QIK2_ID 9
#define QIK_TX 2
#define QIK_RX 3
#define QIK_RESET 4
//#define DEBUG
#define S_DELAY 200
#define L_DELAY 500

PololuQik2s9v1 qik(QIK_TX, QIK_RX, QIK_RESET);
int testIncrement = 0;

// Define statements for servo positions
// *****************************************
#define NECK           15 // Moves neck (and head) left to right

#define NECK_MIN 1300 * 4
#define NECK_MAX 2240 * 4

// Arms ~~~~~~~~~~~~~~~~~~~~~~~~~~~
#define RIGHT_ELBOW    3 // Moves elbow up and down
#define RIGHT_FOREARM  1 // Twists forearm
#define RIGHT_SHOULDER 10 // Raises arm at shoulder
#define RIGHT_SHOULDER_TWIST 14 // Twists arm at shoulder

#define RIGHT_ELBOW_MIN 1300 * 4
#define RIGHT_ELBOW_MAX 2000 * 4
#define RIGHT_FOREARM_MIN 750 * 4 // *
#define RIGHT_FOREARM_MAX 2380 * 4  // *
#define RIGHT_SHOULDER_MIN 800 * 4
#define RIGHT_SHOULDER_MAX 1900 * 4
#define RIGHT_SHOULDER_TWIST_MIN 600 * 4 //  MADE UP VALUES
#define RIGHT_SHOULDER_TWIST_MAX 1700 * 4 // MADE UP VALUES


#define LEFT_ELBOW     12 
#define LEFT_FOREARM   0 
#define LEFT_SHOULDER    11 
#define LEFT_SHOULDER_TWIST 17 

#define LEFT_ELBOW_MIN 1000 * 4
#define LEFT_ELBOW_MAX 1700 * 4
#define LEFT_FOREARM_MIN 900 * 4
#define LEFT_FOREARM_MAX 1200 * 4
#define LEFT_SHOULDER_MIN 800 * 4
#define LEFT_SHOULDER_MAX 1850 * 4
#define LEFT_SHOULDER_TWIST_MIN 900 * 4 // MADE UP VALUES 
#define LEFT_SHOULDER_TWIST_MAX 2200 * 4 // MADE UP VALUES

// Legs ~~~~~~~~~~~~~~~~~~~~~~~~~~~
#define RIGHT_KNEE     5
#define RIGHT_HIP      7 
#define RIGHT_HIP_TWIST 2 

#define RIGHT_HIP_MIN 1000 * 4
#define RIGHT_HIP_MAX 2070 * 4
#define RIGHT_KNEE_MIN 2280 * 4
#define RIGHT_KNEE_MAX 1450 * 4
#define RIGHT_HIP_TWIST_MIN 1000 * 4 // MADE UP VALUES 
#define RIGHT_HIP_TWIST_MAX 1000 * 4 // MADE UP VALUES

#define LEFT_KNEE      6 
#define LEFT_HIP       9 
#define LEFT_HIP_TWIST 16

#define LEFT_KNEE_MIN 650 * 4
#define LEFT_KNEE_MAX 1450 * 4
#define LEFT_HIP_MIN 1545 * 4
#define LEFT_HIP_MAX 707 * 4
#define LEFT_HIP_TWIST_MIN 1000 * 4 // MADE UP VALUES 
#define LEFT_HIP_TWIST_MAX 1000 * 4 // MADE UP VALUES

// Neutral positions  ~~~~~~~~~~~~~~~~~~~~~~~~~~~
#define RIGHT_ELBOW_NEUTRAL    1900 * 4
#define RIGHT_FOREARM_NEUTRAL  RIGHT_FOREARM_MIN
#define RIGHT_HIP_NEUTRAL      1175 * 4
#define RIGHT_HIP_TWIST_NEUTRAL      1000 * 4
#define RIGHT_SHOULDER_NEUTRAL 1050 * 4
#define RIGHT_SHOULDER_TWIST_NEUTRAL 1000 * 4 // MADE UP VALUES 
#define RIGHT_KNEE_NEUTRAL     RIGHT_KNEE_MAX
#define LEFT_ELBOW_NEUTRAL     1370 * 4
#define LEFT_FOREARM_NEUTRAL   1000  * 4// ?!?!0 since servo is broken
#define LEFT_SHOULDER_NEUTRAL  1955 * 4
#define LEFT_SHOULDER_TWIST_NEUTRAL 1000 * 4 // MADE UP VALUES 
#define LEFT_KNEE_NEUTRAL      LEFT_KNEE_MAX
#define LEFT_HIP_NEUTRAL       1389 * 4
#define LEFT_HIP_TWIST_NEUTRAL      1000 * 4
#define NECK_NEUTRAL           1700 * 4



// Define objects
// *****************************************
// Create Pololu Maestro object (stream, resetPin, channel#, CRC mode) - used for servo control
MiniMaestro maestro(maestroSerial, RESET_PIN, CHANNEL_NUMBER, false);

// Local variables
int isPiConnected;
int piCommand;

void setup() {
  // Set up serial communications
  // Serial communicates with either the monitor (for debug)
  //  or to Raspberry Pi, depending on if SERIAL_DEBUG or PI_CONNECTED is defined
  
  
  /*
  Serial.begin(115200);
  Serial.println("qik 2s9v1 dual serial motor controller");
  qik.init();
  */

  Serial.begin(9600);
  #ifdef SERIAL_DEBUG
  Serial.print("STARTING SETUP PROCESS\n");
  #endif
  // Define PI Connected pin (A0)
  pinMode(PI_CONNECTED_PIN, INPUT);
  
  maestroSerial.begin(9600);   // Set the serial baud rate.

  initialSpeedAcceleration();
  initialPositions();

  #ifdef SERIAL_DEBUG
  Serial.print("SETUP FINISHED - READY TO BEGIN LOOP\n");
  #endif 
}

// *****************************************
// MAIN LOOP
// *****************************************
void loop() {
  #ifdef SERIAL_DEBUG
  Serial.print("STARTING MAIN LOOP\n");
  #endif 

  // If defined Pi as connected, run Serial code
  isPiConnected = digitalRead(PI_CONNECTED_PIN);

  #ifdef SERIAL_DEBUG
  Serial.print("CHECKED PI CONNECTED PIN A0. VALUE IS: ");
  Serial.print(isPiConnected);
  Serial.print("\n");
  #endif
  
  //initialPositions();
  releaseServos();
  //delay(DELAY/4);

  if(isPiConnected)
  {
    //maestro.setTarget(NECK, NECK_NEUTRAL);
    /*
    piCommand = 0;
    // Check for Serial command
    if(Serial.available())
    {
        raiseArmRight();
        delay(DELAY/4);
        //initialPositions();
        releaseServos();
        delay(DELAY/4);
      piCommand = Serial.read();
      // Pi Connection code
      for(int i = 0; i< 0; i++)
      {
        basicWaveRight();
        delay(DELAY/4);
        initialPositions();
        releaseServos();
        delay(DELAY/4);
      }
    }
    */
  }
  else 
  {
    // Start Wheel demo
    #ifdef SERIAL_DEBUG
    Serial.print("STARTING WHEEL DEMO\n");
    #endif
    /*
    rstop();
    demo ();
    rstop ();
    */
    
    #ifdef SERIAL_DEBUG
    Serial.print("DETERMINED PI IS NOT CONNECTED\n");
    #endif 
    // Code testing area
    // Try to wave
    #ifdef SERIAL_DEBUG
    Serial.print("RIGHT ARM WAVE: \n");
    #endif
    basicWaveRight();
    delay(DELAY);

    basicArmDance();
  
    releaseServos();
    delay(DELAY/2);
    
  
  }

  releaseServos();
  delay(DELAY/2);






} // END OF MAIN LOOP

// Servo Functions
// *****************************************
// Arm Dance
void basicArmDance()
{
  #ifdef SERIAL_DEBUG
  Serial.print("BASIC ARM DANCE: \n");
  #endif
  // Set upper arm parrallel to bot/ set shoulder slightly forward
  maestro.setTarget(RIGHT_SHOULDER, (1200 * 4));
  maestro.setTarget(LEFT_SHOULDER, (1600 * 4));
  
  // bend elbow to ~90 degrees
  maestro.setTarget(RIGHT_ELBOW, (1500 * 4));
  maestro.setTarget(LEFT_ELBOW, (1200 * 4));
  
  // Hands face down
  maestro.setTarget(RIGHT_FOREARM, RIGHT_FOREARM_MAX);
  maestro.setTarget(LEFT_FOREARM, LEFT_FOREARM_MIN);
  
  // Twist arms in and out w/ slight elbow changes
  // Twist in
  maestro.setTarget(RIGHT_SHOULDER_TWIST, RIGHT_SHOULDER_TWIST_MAX);
  maestro.setTarget(LEFT_SHOULDER_TWIST, LEFT_SHOULDER_TWIST_MIN);
  delay(DELAY/2);
  maestro.setTarget(RIGHT_SHOULDER_TWIST, RIGHT_SHOULDER_TWIST_MIN);
  maestro.setTarget(LEFT_SHOULDER_TWIST, LEFT_SHOULDER_TWIST_MAX);
  delay(DELAY/2);
  maestro.setTarget(RIGHT_ELBOW, (1700 * 4));
  maestro.setTarget(LEFT_ELBOW, (1400 * 4));
  delay(DELAY/2);
  maestro.setTarget(RIGHT_SHOULDER_TWIST, RIGHT_SHOULDER_TWIST_MAX);
  maestro.setTarget(LEFT_SHOULDER_TWIST, LEFT_SHOULDER_TWIST_MIN);
  delay(DELAY/2);
  maestro.setTarget(RIGHT_SHOULDER_TWIST, RIGHT_SHOULDER_TWIST_MIN);
  maestro.setTarget(LEFT_SHOULDER_TWIST, LEFT_SHOULDER_TWIST_MAX);
  delay(DELAY/2);
  
  delay(DELAY*2);

}
// Waves once with the right arm
void basicWaveRight()
{
  // Try to wave

  maestro.setTarget(RIGHT_FOREARM, RIGHT_FOREARM_MAX);

  maestro.setTarget(RIGHT_SHOULDER, RIGHT_SHOULDER_MAX);
  delay(DELAY/4);
  maestro.setTarget(RIGHT_ELBOW, (1500*4));
  delay(DELAY/2);

  maestro.setTarget(RIGHT_SHOULDER_TWIST, (1300 * 4));
  delay(DELAY/4);
  maestro.setTarget(RIGHT_SHOULDER_TWIST, (800 * 4));
  delay(DELAY/4);
  maestro.setTarget(RIGHT_SHOULDER_TWIST, (1300 * 4));
  delay(DELAY/4);
  maestro.setTarget(RIGHT_SHOULDER_TWIST, (800 * 4));
  delay(DELAY/4);

}

// Raise right arm in greeting position
void raiseArmRight()
{
  maestro.setTarget(RIGHT_FOREARM, RIGHT_FOREARM_MAX);

  maestro.setTarget(RIGHT_SHOULDER, RIGHT_SHOULDER_MAX);
  delay(DELAY/4);
  maestro.setTarget(RIGHT_ELBOW, (1500*4));
  delay(DELAY/4);
}

// TEST: This function tests one servo at a time
void testServoAtChannel(int channelNum)
{
     int safeMin = 1000 * 4;
     int safeMax = 1400 * 4;
     int safeNeutral = 1200 * 4;

     releaseServos();
     maestro.setTarget(channelNum, safeNeutral);
     delay(DELAY/2);
     maestro.setTarget(channelNum, safeMin);
     delay(DELAY);
     maestro.setTarget(channelNum, safeMax);
     delay(DELAY);
     maestro.setTarget(channelNum, safeNeutral);
     delay(2* DELAY);
     releaseServos();

}

// Moves all servos to check channel pairings
void testAllServos()
{
  //  Use function: testServoAtChannel(int channelNum)
  int minChannel = 0; // Starts at 0
  int maxChannel = 17; // Maximum channel connected to body servos is 17 (18 total channels)
  for(int i=minChannel; i <= maxChannel; i++)
  {
    #ifdef SERIAL_DEBUG
    Serial.print("RUNNING TEST ON CHANNEL: ");
    Serial.print(i);
    Serial.print("\n");
    #endif
    testServoAtChannel(i);
  }
}

// TEST: This function tests one servo at a time to determine if range works
void testServoRange(int channelNum, int neutralPos, int minPos, int maxPos)
{
    #ifdef SERIAL_DEBUG
    Serial.print("STARTING TEST SERVO RANGE FUNCTION:\n");
    Serial.print("TESTING CHANNEL:  ");
    Serial.print(channelNum);
    Serial.print("\n");
    Serial.print("\n");
    #endif 
      #ifdef SERIAL_DEBUG
     Serial.print("Test positions: ");
     Serial.print(neutralPos);
     Serial.print("   +   ");
     Serial.print(minPos);
     Serial.print("   +   ");
     Serial.print(maxPos);
     Serial.print("\n");
     #endif 
     releaseServos();
     maestro.setTarget(channelNum, neutralPos);
     delay(DELAY);
     maestro.setTarget(channelNum, minPos);
     delay(DELAY/2);
     maestro.setTarget(channelNum, maxPos );
     delay(DELAY/2);
     maestro.setTarget(channelNum, neutralPos);
     delay(DELAY);
     releaseServos();

}

// TEST: This function tries to determine a servo's range of motion, as well as neutral position
void testServoRangeIncrements(int channelNum, int minRange, int maxRange)
{
  #ifdef SERIAL_DEBUG
  Serial.print("STARTING TEST SERVO RANGE FUNCTION:\n");
  Serial.print("TESTING CHANNEL:  ");
  Serial.print(channelNum);
  Serial.print("\n");
  Serial.print("\n");
  #endif 

  int increment = 50;
  int midPoint = int((minRange+maxRange)/2);
  int totalRange = maxRange - minRange;
  int totalPoints = int(totalRange / increment);
  
  int offset = 0;
  int lowPoint = 0;
  int highPoint = 0;
  
  for(int i = 1; i < totalPoints; i++ )
  {
     offset = i * increment;
     lowPoint = midPoint - offset;
     highPoint = midPoint + offset;
     releaseServos();
     #ifdef SERIAL_DEBUG
     Serial.print("Test positions: ");
     Serial.print((midPoint/4));
     Serial.print("   +   ");
     Serial.print((lowPoint/4));
     Serial.print("   +   ");
     Serial.print((highPoint/4));
     Serial.print("\n");
     #endif 
     maestro.setTarget(channelNum, midPoint);
     delay(DELAY/2);
     maestro.setTarget(channelNum, lowPoint);
     delay(DELAY/2);
     maestro.setTarget(channelNum, highPoint);
     delay(DELAY/2);
     maestro.setTarget(channelNum, midPoint);
     delay(DELAY/2);
     releaseServos();
  }
  
}
// This function sets all servos to neutral positions
void initialPositions()
{
  // Servo control postions are hadcoded
  uint16_t channel_array[NUM_CHANNELS] = { LEFT_FOREARM_NEUTRAL, RIGHT_FOREARM_NEUTRAL, RIGHT_HIP_TWIST_NEUTRAL, 
                RIGHT_ELBOW_NEUTRAL, 0, RIGHT_KNEE_NEUTRAL, LEFT_KNEE_NEUTRAL,
                RIGHT_HIP_NEUTRAL, 0, LEFT_HIP_NEUTRAL, RIGHT_SHOULDER_NEUTRAL, LEFT_SHOULDER_NEUTRAL, 
                LEFT_ELBOW_NEUTRAL, 0, RIGHT_SHOULDER_TWIST_NEUTRAL, NECK_NEUTRAL, 
                LEFT_HIP_TWIST_NEUTRAL, LEFT_SHOULDER_TWIST_NEUTRAL };
  maestro.setMultiTarget(NUM_CHANNELS, 0, channel_array);
}

void initialSpeedAcceleration()
{
  maestro.setSpeed(RIGHT_ELBOW, 0);
  maestro.setSpeed(RIGHT_FOREARM, 0);
  maestro.setSpeed(RIGHT_HIP, 0);
  maestro.setSpeed(RIGHT_HIP_TWIST, 0);
  maestro.setSpeed(RIGHT_SHOULDER, 0);
  maestro.setSpeed(RIGHT_SHOULDER_TWIST, 0);
  maestro.setSpeed(RIGHT_KNEE, 0);
  maestro.setSpeed(LEFT_ELBOW, 0);
  maestro.setSpeed(LEFT_FOREARM, 0);
  maestro.setSpeed(LEFT_SHOULDER, 0);
  maestro.setSpeed(LEFT_SHOULDER_TWIST, 0);
  maestro.setSpeed(LEFT_KNEE, 0);
  maestro.setSpeed(LEFT_HIP, 0);
  maestro.setSpeed(LEFT_HIP_TWIST, 0);
  maestro.setSpeed(NECK, 0);

  maestro.setAcceleration(RIGHT_ELBOW, 0);
  maestro.setAcceleration(RIGHT_FOREARM, 0);
  maestro.setAcceleration(RIGHT_HIP, 0);
  maestro.setAcceleration(RIGHT_HIP_TWIST, 0);
  maestro.setAcceleration(RIGHT_SHOULDER, 0);
  maestro.setAcceleration(RIGHT_SHOULDER_TWIST, 0);
  maestro.setAcceleration(RIGHT_KNEE, 0);
  maestro.setAcceleration(LEFT_ELBOW, 0);
  maestro.setAcceleration(LEFT_FOREARM, 0);
  maestro.setAcceleration(LEFT_SHOULDER, 0);
  maestro.setAcceleration(LEFT_SHOULDER_TWIST, 0);
  maestro.setAcceleration(LEFT_KNEE, 0);
  maestro.setAcceleration(LEFT_HIP, 0);
  maestro.setAcceleration(LEFT_HIP_TWIST, 0);
  maestro.setAcceleration(NECK, 0);
}

// turns power to all servos off
void releaseServos()
{
  uint16_t channel_array[NUM_CHANNELS] = { 0, 0, 0, 0, 0, 0, 0,
                                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
  maestro.setMultiTarget(NUM_CHANNELS, 0, channel_array);
}
// Wheel Functions
// *****************************************
void demo()
{
  testIncrement = 0;
  #ifdef SERIAL_DEBUG
  Serial.print("STARTING DEMO FUNCTION: ");
  Serial.print(testIncrement);
  Serial.print("\n");
  #endif

  while(testIncrement <2100)
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
  #ifdef SERIAL_DEBUG
  Serial.print("ENDING DEMO FUNCTION: ");
  Serial.print(testIncrement);
  Serial.print("\n");
  #endif
}



void rstop ()
{
    qik.setSpeeds(0, 0);  // M0, M1 stop

   #ifdef DEBUG
  Serial.print(F("Stop   "));
  #endif
}
