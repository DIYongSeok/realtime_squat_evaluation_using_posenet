## Introduction
This project aims to evaluate posture during exercises, with a particular focus on squats. It provides real-time feedback on the accuracy of squat posture using PoseNet to capture joint positions and a perceptron model for deep learning analysis.

![demo_video](https://github.com/DIYongSeok/realtime_squat_evaluation_using_posenet/assets/146920174/de75f661-9019-46e0-b794-111f3d08c544)

## Requirements
- [Anaconda](https://www.anaconda.com/download)
    

- iVcam(optional)

    - This app helps you use your cellphone as a remote webcam. 
    - [Installation video](https://youtu.be/z2wRJlPKZU8)
    

## To Start
1. Install this project 
    ```
    git clone https://github.com/DIYongSeok/realtime_squat_evaluation_using_posenet.git
    cd realtime-squat-evaluation-using-posenet/
    ```
2. Launch virtual environment
    ```
    conda env create -f environment.yml
    ```
3. Check the available webcam
    ```
    python test_available_webcam.py
    ```
    - It shows list of webcams which are available on your computer.
    - If you install the iVcam, remember the cam number of iVcam.
4. Launch the program
    ```
    python realtime_squat_evaluation_program.py
    ```
    If you install the iVcam and the cam number of iVcam is 5 for example, try below line.
    ```
    python realtime_squat_evaluation_program.py --cam_id 5
    ```

## Perceptron Training

This section explains how I train the perceptron to assess the accuracy of squat posture.

To train the perceptron, I need to create a set of training data. In the 'perceptron' folder of this project, you will find a file named 'training_set_generator.py'. To run this file, use the following commands:
```
cd perceptron/
python training_set_generator.py
```

When you start 'training_set_generator.py', it will capture the positions of your joints and label them as 0. Perform a squat with the correct posture and maintain it in front of the webcam. Then, press 's' on the keyboard. By doing this, the positions of your joints will be labeled as 1.

![example](https://github.com/DIYongSeok/realtime_squat_evaluation_using_posenet/assets/146920174/93f3ea66-0aa6-4139-a6d9-881a5cf44d75)

If you press the 'q' button, the program will shut down and generate the training set file in the 'trainingSet' folder.

After that, run the file named 'perceptron_model_generator.py':
```
python perceptron_model_generator.py
```
This script reads the files in the 'trainingSet' folder and trains the perceptron. Once the training is complete, you will find the trained model in the 'output' folder. This model will be used by the 'realtime_squat_evaluation_program.py' to evaluate squat posture in real time.

## References
- [PoseNet](https://github.com/rwightman/posenet-python)