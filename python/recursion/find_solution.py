def find_solution(target):
    def find(current, history):
        if current == target:
            return history
        elif current > target:
            return False
        else:
            return find(current + 5, (history + 5)) or find(current * 3, (history * 3))

    return find(1, 1)

print(find_solution(24))
