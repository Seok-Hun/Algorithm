# Greedy 알고리즘을 적용하여 최적의 수강신청 스케줄을 알아내는 알고리즘을 작성해야 함.

### 가천대학교 홍길동 학생이 KEA 강의를 수강하기 위해 강의 스케줄을 체크 및 조율하고 있음.

### 10개의 과목들 중 최대한 많이 들으려고 조율하고 있음. 따라서 강의시간이 서로 겹치면 안되기 때문에 최적의 강의시간을 산출해야 함. 입력조건은 튜플형태로 입력됨.

### 해당 학기의 수업 리스트는 아래와 같음.

>[(4,8),(3,5),(2,4),(1,4),(8,10),(6,8),(5,7),(4,5),(5,8),(9,11)]

- 상위 수업리스트의 형태에서 각 튜플의 **0번째는 강의시작교시**를 의미하고 **1번째는
종료교시**를 의미함.
    - 예를 들어 첫번째 튜플 인덱스 인 (4, 8)의 강의를 보면 4교시에 시작하고
종료는 8교시에 함.
    - 또한 (8, 10)강의와 (6, 8)강의를 보면 시작교시와 종료교시가 겹침. 이럴 경우에는 두
강의수강은 불가능한 것으로 간주함.
---
- 입력조건
    - 튜플형식의 [(4, 8), (3, 5), (2, 4), (1, 4), (8, 10), (6, 8), (5, 7), (4, 5), (5, 8), (9, 11)]

- 출력조건
    - 겹치지 않고 최적의 강의시간을 산출해야 함.

- 출력 예시
    - [(2, 4), (5, 7), (8, 10)]