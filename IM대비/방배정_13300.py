def calculate_rooms_needed(num_students, max_per_room, students):
    # 학생 정보를 성별과 학년별로 분류
    groups = {}
    for gender in [0, 1]:  # 0: 여학생, 1: 남학생
        for grade in range(1, 7):  # 학년 1부터 6까지
            groups[(gender, grade)] = 0

    # 학생 수 세기
    for student in students:
        gender, grade = student
        groups[(gender, grade)] += 1

    # 방의 수 계산
    total_rooms = 0
    for (gender, grade), count in groups.items():
        if count > 0:
            rooms = (count + max_per_room - 1) // max_per_room
            total_rooms += rooms

    return total_rooms

num_students, max_per_room = map(int, input().split())
students = []
for _ in range(num_students):
    gender, grade = map(int, input().split())
    students.append((gender, grade))

result = calculate_rooms_needed(num_students, max_per_room, students)
print(result)