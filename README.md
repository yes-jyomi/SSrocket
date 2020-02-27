# 🚀 SSrocket 🚀
일본 기후 자전거 대여 예약 웹앱

## 변수 설정
### SIGN UP (회원가입)
* user_info : 유저인지 회사인지 선택

* joinForm : 회원가입 폼 아이디
* id : 아이디 (이메일)
* pwd : 비밀번호
* pwdck : 확인용 비밀번호
* name : 이름
* joinBt : 가입 버튼

* logo : 상단 로고
* barName : 이름 박스
* barEmail : 이메일 박스
* barEmailck : 이메일 중복확인 박스
* barPwd : 비밀번호 박스
* barPwdck : 비밀번호 재확인 박스
----- -----
### LOGIN
* loginForm : 로그인 폼 이름
* id : 아이디 (이메일)
* pwd : 비밀번호
* loginBt : 로그인 버튼
* logo : 상단 로고
* loginText : 로그인 글씨
* joinText : 회원가입 글씨
* underBar : 글씨 아래에 있는 바
* welcomeText : 환영합니다 글씨
----- -----
### RESERVATION
* db_user_id : DB에 있는 유저 아이디 (예약 시 필요)
* db_company_addr : 대여점 주소 (유저가 입력한 여행할 위치 근처이고)
* db_bike_num : 대여점이 갖고 있는 자전거 수 (자전거 수가 1개 이상이면 대여점 이름을 보여줌, 아니면 '일치하는 대여점 정보가 없다'는 메시지를 띄움.)
* db_company_phone : 대여점 전화번호
* current_loc : 유저가 입력한 여행할 위치
* db_user_name : DB에 있는 회사 이름 (유저가 선택한 정보를 바탕으로 화면에 나타남)
* form_r_btime : 사용자가 입력한 방문 시간
* form_r_rtime : 사용자가 입력한 반납 시간
* db_r_btime : DB에 있는 방문 시간 ( 예약 완료 시 DB에서 꺼내서 보여줌)
* db_r_rtime : DB에 있는 반납 시간

## Database
### USER
회원 정보 테이블
* id : 유저 아이디 [ VARCHAR(20) PRIMARY KEY ]
* name : 유저 이름 [ VARCHAR(20) NOT NULL ]
* pwd : 유저 비밀번호 [ VARCHAR(20) NOT NULL ]
* info : 0 은 user, 1 은 company [ INT(2) NOT NULL DEFAULT 0 ]

### HISTORY
예약 정보 테이블
* history_num : 예약 번호 [ INT PRIMARY KEY AUTO_INCREMENT ]
* history_place : 대여점 이름 [ VARCHAR(20) NOT NULL ]
* member_id : 유저 아이디 [ VARCHAR(20) NOT NULL ]
* r_btime : 예약한 방문 시간 [ DATETIME NOT NULL ]
* btime : 실제 방문 시간 [ DATETIME NOT NULL ]
* r_rtime : 예약한 반납 시간 [ DATETIME NOT NULL ]
* rtime : 실제 반납 시간 [ DATETIME NOT NULL ]
* reserved_At : 예약한 시간 [ DATETIME NOT NULL ]

### COURSE
코스 정보 테이블
* c_num : 코스 번호 [ INT PRIMARY KEY AUTO_INCREMENT ]
* c_name : 코스 이름 [ VARCHAR(20) NOT NULL ]
* c_info : 코스 정보 [ VARCHAR(20) NOT NULL ]
* c_loc : 코스 위치 [ VARCHAR(20) NOT NULL ]
* c_theme : 코스 테마 [ VARCHAR(20) ]
* c_time : 코스 소요 시간 [ INT(8) ]

### COMPANY
회사 정보 테이블
* company_num : 회사 번호 [ INT PRIMARY KEY AUTO_INCREMENT ]
* member_id : 회사 아이디 [ VARCHAR(20) NOT NULL ]
* member_name : 회사 이름 [ VARCHAR(20) NOT NULL ]
* company_addr : 회사 주소 [ VARCHAR(20) NOT NULL ]
* company_loc : 회사 위치 [ VARCHAR(20) NOT NULL ]
* company_phone : 회사 번호 [ VARCHAR(20) NOT NULL ]
* company_info : 회사 정보 [ VARCHAR(50) NOT NULL ]
* bicycle_num : 자전거 개수 [ INT(12) NOT NULL ]
* rent_num : 빌려준 자전거 개수 [ INT(12) NOT NULL ]
* s_business : 영업 시작 시간 (format 지정해서 시간만 나타냄) [ DATETIME ] [ date_format(datetime, '%h:%i:%s') ]
* e_business : 영업 종료 시간 (format 지정해서 시간만 나타냄) [ DATETIME ] [ date_format(datetime, '%h:%i:%s') ]
