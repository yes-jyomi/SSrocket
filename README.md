# SSrocket
일본 기후 자전거 대여 예약 웹앱

## 변수 설정
### MEMBER
* db_user_id : DB에 있는 유저 아이디 (가입 시 아이디 중복확인, 로그인 시 필요)
* db_user_pwd : DB에 있는 유저 비밀번호 (로그인)
* db_user_name : DB에 있는 유저 이름 (예약 시 필요)
* db_user_info : DB에 있는 유저인지 회사인지 나타내는 것 (예약 시 유저인지 확인함)
----- ----- ----- -----
* join_user_info : 가입 시 유저인지 회사인지 선택 (이후 DB에 넣음)
* join_id : 가입 시 입력한 아이디
* join_pwd : 가입 시 입력한 비밀번호
* join_pwdck : 가입 시 확인용 비밀번호 (Javascript 로 맞는지 확인)
* join_name : 가입 시 입력한 이름
* login_id : 로그인 시 입력한 이름
* login_pwd : 로그인 시 입력한 비밀번호

### RESERVATION
* db_user_id : DB에 있는 유저 아이디 (예약 시 필요)
* db_company_addr : 대여점 주소 (유저가 입력한 여행할 위치 근처이고)
* db_bike_num : 대여점이 갖고 있는 자전거 수 (자전거 수가 1개 이상이면 대여점 이름을 보여줌, 아니면 '일치하는 대여점 정보가 없다'는 메시지)
* db_company_phone : 대여점 전화번호
----- ----- ----- -----
* current_loc : 유저가 입력한 여행할 위치
* bike_port_name : 대여점 이름

## Database
### USER
회원 정보 테이블
* user_id : 유저 아이디
* user_name : 유저 이름
* user_pwd : 유저 비밀번호
* user_info : 0 은 user, 1 은 company

### HISTORY
예약 정보 테이블
* hist_num : 예약 번호
* hist_place : 대여점 이름
* user_id : 유저 아이디
* r_btime : 예약한 방문 시간
* btime : 실제 방문 시간
* r_rtime : 예약한 반납 시간
* rtime : 실제 반납 시간

### COURSE
코스 정보 테이블
* c_num : 코스 번호
* c_name : 코스 이름
* c_info : 코스 정보
* c_loc : 코스 위치
* c_theme : 코스 테마
* c_time : 코스 소요 시간

### COMPANY
회사 정보 테이블
* company_num : 회사 번호
* user_id : 회사 아이디
* user_name : 회사 이름
* company_addr : 회사 주소
* company_phone : 회사 번호
* bicycle_num : 자전거 개수
