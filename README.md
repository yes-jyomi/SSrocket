# SSrocket
일본 기후 자전거 대여 예약 웹앱

## Database
### USER
회원 정보 테이블
* user_id : 유저 아이디
* user_name : 유저 이름
* user_pwd : 유저 비밀번호
* user_info : 0 은 user, 1 은 company

### HISTORY
예약 정보 테이블
* his_num : 번호
* place : 대여점 이름
* his_id : 유저 아이디
* r_btime : 예약한 방문 시간
* btime : 실제 방문 시간
* r_rtime : 예약한 반납 시간
* rtime : 실제 반납 시간

### COURSE
코스 정보 테이블
* c_num : 번호
* c_name : 코스 이름
* c_info : 코스 정보
* c_loc : 코스 위치
* c_theme : 코스 테마
* c_time : 코스 소요 시간
