### Greedy 알고리즘을 적용하여 출발지로부터 목적지까지 최적의 동선을 파악하고 총 최소거리를 산출하는 알고리즘을 산출해야 함.
### 경기도 성남 가천대학교 정문(Gadhon university)에서 출발하여 부산(Busan cityhall)까지 가려고 할 때 아래와 같은 경로가 있다고 가정 함. 가장 최적의 경로를 기반으로 최소거리를 산출하는 알고리즘을 작성하기 바람. 경로는 가천대학교 → 대전시청 → 부산대학교로 가야 함.
---
- 입력조건
  - 첫번째는 Gachon university <-> Daejeon cityhall간의 여러 경로에 해당하는 리스트 임. Ex) [190, 150, 180]
  - 두번쨰는 Daejeon cityhall <-> Busan cityhall간의 여러 경로에 해당하는 리스트임. Ex) [230, 170, 220]
  - Min함수를 사용하면 안됨.
- 출력조건
  - 첫번째의 최단거리를 출력
  - 두번째의 최단거리를 출력
- 출력 예시
  - 첫번째 경로와 두번째 경로의 최단거리를 합한 수가 출력되어야 함. Ex) 330km