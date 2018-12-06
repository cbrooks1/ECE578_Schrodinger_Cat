Terminal 1
cd catkin_ws/
roscore

Terminal 2
sudo pip install boto3
sudo pip install awscli
sudo pip install pygame
aws configure
    AWS Access Key ID [None]: ASK CHELSEA
    AWS Secret Access Key [None]: ASK CHELSEA
    Default region name [None]: us-west-2
    Default output format [None]: mp3
cd catkin_ws/src/speech_synthesis/scripts/
chmod +x speech.py
cd ../../../
catkin_make
source devel/setup.bash
rosrun speech_synthesis speech.py


Terminal 3
sudo apt remove python-pyasn1-modules
sudo pip uninstall pyasn
sudo pip install dialogflow
sudo apt-get install python-pyaudio
sudo apt install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
export GOOGLE_APPLICATION_CREDENTIALS="/home/chelsea/Desktop/schrodinger-cat-1e80208a5e2f.json"
cd catkin_ws/src/voice_recognition/src/
chmod +x dialogflow.py
chmod +x recognition.py
chmod +x record.py
cd ../../../
catkin_make
source devel/setup.bash
roslaunch voice_recognition voice_recognition.launch
