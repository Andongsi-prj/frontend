import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import joblib
import os 
from flask import Blueprint, request, jsonify

pipe_route = Blueprint('pipe', __name__)

# 모델 로드
pipe_model = tf.keras.models.load_model('pipe.keras')

def load_and_preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(150, 150))  # 모델에 맞는 입력 크기
    img_array = image.img_to_array(img)  # 이미지를 배열로 변환
    img_array = np.expand_dims(img_array, axis=0)  # 배치를 추가 (모델은 배치 형태를 요구)
    img_array = img_array / 255.0  # 스케일 조정 (0~1로)
    return img_array    


@pipe_route.route("/pipe", methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    # 이미지 파일 저장
    image_file = request.files['image']
    file_path = os.path.join("uploads", image_file.filename)
    os.makedirs("uploads", exist_ok=True)
    image_file.save(file_path)

    # 이미지 전처리 및 예측
    try:
        preprocessed_img = load_and_preprocess_image(file_path)
        prediction = pipe_model.predict(preprocessed_img)

        # 결과 반환
        if prediction[0] > 0.5:
            result = {
                "label": "양품",
                "confidence": float(prediction[0][0])
            }
        else:
            result = {
                "label": "불량품",
                "confidence": float(1 - prediction[0][0])
            }

        # 처리 후 임시 파일 삭제
        os.remove(file_path)

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500