# dx_sprint

# dx_sprint


## 1. 찜하기

* URL
> http://223.130.139.200/api/like/cook_like/

* Method
> POST

* URL Params
> Required: 없음

* Body
> Raw data 방식 또는 form-data 방식 \
> form-data 방식일 경우 key=value 방식 \
> cook=cook 테이블의 id, user=user 테이블의 id

* RequestHeader

| Key      | Value         | 설명       |
| -------- |---------------|----------|
| Authorization | user_number 값 | 기기 고유 번호 |

* Sample Call:

### 찜 요청(POST) 하는 경우
```bash
curl --location --request POST 'http://223.130.139.200/api/like/cook_like/' \
--header 'Authorization: 2' \
--form 'cook="10"' \
--form 'user="2"'
```
* Success Response & Error Response
```
* Success Response:
- Code: 201
- Content: {
    "cook": 10,
    "user": 2
}

* Error Response:
유효하지 않은 user의 id나 cook의 id를 넣을 경우 잘못 입력한 필드에 해당하는 데이터를 찾을 수 없다는 내용이 나옴

- Code: 404
- Content: {
    "user": [
        "Invalid pk \"22222222\" - object does not exist."
    ]
}
```

## 2. 찜 제거하기

* URL
> http://223.130.139.200/api/like/cook_unlike/3/  # 지워하야하는 cook의 id를 포함시킨다
* Method
> DELETE

* URL Params
> Required: 없음

* Body
> 없음

* RequestHeader

| Key      | Value         | 설명       |
| -------- |---------------|----------|
| Authorization | user_number 값 | 기기 고유 번호 |

* Sample Call:

### 찜 삭제(DELETE) 하는 경우
```bash
curl --location --request DELETE 'http://223.130.139.200/api/like/cook_unlike/59/' \
--header 'Authorization: 2'
```
* Success Response & Error Response
```
* Success Response:
- Code: 204
- Content: 없음

```
