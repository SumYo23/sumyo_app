# 🍽️DX Sprint - 숨요, 숨어있는 요리 찾기(앱)
<p style="text-align: center">
    <img src="https://img.shields.io/badge/Django-v3.10.5-green?logo=Django"/>
    <img src="https://img.shields.io/badge/flutter-v3.10.3-blue?logo=flutter" />
    <img src="https://img.shields.io/badge/Naver Cloud-00E7C3?logo=Naver"/>
    <img src="https://img.shields.io/badge/Postgresql-purple?logo=Postgresql"/>
    <img src="https://img.shields.io/badge/linux-red?logo=linux"/>
    <img src="https://img.shields.io/badge/nginx-green?logo=nginx"/>
    <img src="https://img.shields.io/badge/gunicorn-green?logo=gunicorn"/>
    <img src="https://img.shields.io/badge/yolov5-pink?logo=yolov5"/>
</p>

<p style="text-align: center">
<button style="display: inline-block;outline: 0;cursor: pointer;border-radius: 8px;box-shadow: 0 2px 5px 0 rgb(213 217 217 / 50%);background: #9EDAFB;border: 1px solid #9EDAFB;font-size: 13px;height: 31px;padding: 0 11px;text-align: center;width: 100%;min-width: 200px;font-weight: 500;color: #0F1111;" type="button" class="btn btn-info">App 다운받기</button>
</p>

## Summary
![image](https://github.com/SumYo23/sumyo_app/assets/82714785/b7565cd7-df7a-432a-8ae5-76b6dcc26522)
- 레시피 탐색이 번거롭고 맞춤화 되어있지 않음 👉 **냉장고 재고 기반 다양한 레시피 추천**
- 레시피를 직접 등록하는 과정에서 번거로움을 느낌 👉 **이미지 인식 기술을 통한 재고 등록 간편화**

## 인공지능
- ver 1.0 : google Teachable Machine을 이용해 23개 재료에 대한 이미지 인식 가능
- ver 2.0 : yolov5 를 이용해 재료 다양화 & 정확도 향상(2023.07.28 기준 진행중)

## 백엔드
![image](https://github.com/SumYo23/sumyo_app/assets/82714785/6fbee71f-0780-4bbb-ac7c-9358c79bd499)
- Django Rest Framework를 이용하여 api를 개발 후, api명세서를 작성하여였습니다. - [api명세서 확인하기](https://trapezoidal-calf-f67.notion.site/28074bb04d9c471b9db6cee1d28f9e11?v=eb028251ead14e39ade8e6c132017b12&pvs=4)
- 배포 : Naver Cloud의 서버에 배포하여 Nginx - gunicorn - Django연결 후 배포하였습니다. - [api서버 사용하기 http://223.130.139.200/](http://223.130.139.200/)

## 프론트엔드
![image](https://github.com/SumYo23/sumyo_app/assets/82714785/0cb2e483-f13c-44e7-a3f2-86fde1a825bd)
![image](https://github.com/SumYo23/sumyo_app/assets/82714785/e7bbfd6e-8387-44a5-88a1-0831e6d96966)
![image](https://github.com/SumYo23/sumyo_app/assets/82714785/cb767160-7cb8-4074-b932-c34a47b4c7b6)



                