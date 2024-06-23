# 0. 사용할 패키지 불러오기
from keras.models import Sequential
from keras.layers import Dense
from keras.models import load_model
import numpy as np
import os 

if __name__ == "__main__":
    
    # 1.랜덤시드 고정시키기
    np.random.seed(5)
    
    # 2. 모델 구성하기
    model = Sequential()
    model.add(Dense(30, input_dim=44, activation='relu'))
    model.add(Dense(15, activation='relu'))
    model.add(Dense(15, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    
    # 3. 모델 학습과정 설정하기
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    
    for root, subdirs, files in os.walk('trainingSet'):
        for file in files:
            # 4. 데이터 준비하기
            dataset = np.loadtxt('trainingSet/'+file, delimiter=",")
            x_train = dataset[:,0:44]
            y_train = dataset[:,44]
            
            # 5. 모델 학습시키기
            model.fit(x_train, y_train, epochs=80, batch_size=64)

    # 6. 모델 저장하기
    model.save('squat_mlp_model.h5')