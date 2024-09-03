def find_largest_piece(width, height, cuts):
    # 가로, 세로 자를 인덱스 저장 
    width_cuts = []
    height_cuts = [] 

    for cut in cuts:
        direction, position = cut
        if direction == 0:
            width_cuts.append(position)
        else:
            height_cuts.append(position)

    # 정렬
    width_cuts.sort()
    height_cuts.sort()

    max_height = 0
    last_cut = 0
    for cut in height_cuts:
        max_height = max(max_height, cut - last_cut)
        last_cut = cut
    max_height = max(max_height, height - last_cut)

    max_width = 0
    last_cut = 0
    for cut in width_cuts:
        max_width = max(max_width, cut - last_cut)
        last_cut = cut
    max_width = max(max_width, width - last_cut)

    largest_piece = max_height * max_width
    return largest_piece


##### 왜 안돼냐 ######

def cut_paper(W, H, paper): # 종이 자르기
    max_area = 0 # 젤 큰 면적
    # new_area = []
    
    for i in range(W): # 가로 길이 돌아
        for j in range(H): # 세로 길이 돌아
            area = W * H # 갱신할 새로운 면적
            area2 = W * H # 갱신할 새로운 면적 2
            if paper[i][j[0]] == 0: # 0이면 가로
                width = paper[i][j[1]] # 그 다음 숫자가 자를 가로 번호(길이)
                area -= (width * H) # 면적은 전체 면적 - 잘라진 면적1
                area2 -= (abs(W - width) * H) # 면적은 전체 면적 - 잘라진 면적 2 
                max_area = max(area, area2, max_area) # 최대 면적 갱신

            elif paper[i][j[0]] == 1: # 1이면 세로                                                                
                height = paper[i][j[1]]
                area -= (height * W)
                area2 -= (abs(W - height) * W)
                max_area = max(area, area2, max_area)

    return max_area

W, H = map(int, input().split())
N = int(input())
paper = [list(map, int(input().split())) for _ in range(N)]

print(cut_paper(W, H, paper))