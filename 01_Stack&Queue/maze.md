# Maze 경로 탐색 문제
## 0. 변수
- row, col : 현재 탐색 좌표 위치
- dirt : 탐색할 방향
- nextRow, nextCol : 탐색 가능 여부를 확인할 좌표 위치

## 1. init
- [row, col, dirt] = [1, 1, 2]
    - dirt = 2 : 시작점의 상단부분은 벽으로 막혀있기 때문에 동쪽부터 탐색
- [row, dol, dirt] push

## 2. start loop 1
- 조건 (and)
    1. Found = False
    2. stack is not Empty : len(stack) > 0

## 3. 이전 경로 가져오기
- row, col, dirt = stack pop

## 4. start loop 2
- 조건 (and)
    1. dirt < 8
    2. Found = False

## 5. 다음 위치의 탐색가능 여부 확인하기
- nextRow, nextCol = 현재 row, col에서 dirt의 좌표이동값을 더한 것
1. 다음 위치가 도착점
    - 조건 : nextRow == exitRow, nextCol == exitCol
    - Found = True, loop 1과 loop2 탈출
2. 다음 위치가 탐색 가능
    - 조건 : (nextRow, nextCol) 위치의 값 == 0, 위치의 mark 값 == 0
    1. 방문하기 : mark의 (nextRow, nextCol) == 1
    2. 현재 위치 push
    3. 지금 위치 update : row = nextRow, col = nextCol
    4. 탐색 방향 처음부터 : dirt = 0