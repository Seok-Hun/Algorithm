# 음료수 얼려 먹기
### 문제 출처 : 책 - 이것이 코딩 테스트다.(나동빈)
N × M 크기의 얼음 틀이 있다.  
구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시한다.  
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.  

얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림 개수를 구하는 프로그램을 작성한다.
## 문제
### 입력 조건
- 첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다.
    - 1 <= N, M <= 1000
- 두 번째 줄부터 N + 1번째 줄까지 얼음 틀의 형태가 주어진다.
- 이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.
### 출력 조건
- 한 번에 만들 수 있는 아이스크림 개수를 출력한다.
### 입력 예시
```
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111 
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
```
### 출력 예시
```
8
```
