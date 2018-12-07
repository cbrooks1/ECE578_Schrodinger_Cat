Terminal 1
cd catkin_ws/
roscore

Terminal 2
sudo pip install boto3
sudo pip install awscli
sudo pip install pygame
cd catkin_ws/src/speech_synthesis/scripts/
chmod +x script.py
cd ../../../
catkin_make
source devel/setup.bash
rosrun speech_synthesis script.py
