# 1이 될 때까지
어떤 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택해 수행
단, 두 연산은 N이 K로 나누어 떨어질 때만 선택 가능
1. N에서 1을 뺀다
2. N을 K로 나눈다.

## 예시
- N : 17
- K : 4

**연산 과정**
1. 1번 과정 수행 : N = 16
2. 2번 과정 수행 : N = 4
3. 2번 과정 수행 : N = 1

따라서 전체 과정 실행 횟수는 3이다.

# 문제
### 입력 조건
- 첫째 줄에 N과 K가 공백으로 구분되어 자연수로 주어진다.
    - 2 <= N <= 100000
    - 2 <= K <= 100000
- 입력으로 주어지는 N은 항상 K보다 크거나 같다.
### 출력 조건
- 첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값 출력
### 입력 예시
```
25 5
```
### 출력 예시
```
2
```