# 효율적인 화폐 구성
### 문제 출처 : 책 - 이것이 코딩 테스트다.(나동빈)

N 종류의 화폐가 있을 때, 화폐 개수를 최소한으로 사용해 그 가치 합이 M원이 될 때의 화폐 개수를 구하는 프로그램을 작성한다.  
이 때, 각 화폐 개수는 마음대로 사용할 수 있으며, 사용한 화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 구분한다.

## 문제
### 입력 조건
- 첫째 줄에 N, M이 주어진다.
    - 1 <= N <= 100
    - 1 <= M <= 10,000
- 이후 N개의 줄에는 각 화폐의 가치가 주어진다.
    - 화폐 가치는 10,000보다 작거나 같은 자연수이다.
### 출력 조건
- 첫째 줄에 M원을 만들기 위한 최소한의 화폐 개수를 출력한다.
- 불가능할 때는 -1을 출력한다.
### 입력 예시 1
```
2 15
2
3
```
### 출력 예시 1
```
5
```
### 입력 예시 2
```
3 4
3
5
7
```
### 출력 예시 2
```
-1
```