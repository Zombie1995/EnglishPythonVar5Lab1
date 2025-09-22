import os
import time
import math
import re
from typing import List, Tuple

# ---------- Task 1: Lithuanian Flag ----------

def print_lithuania_flag(width: int = 36, stripe_height: int = 3) -> None:
    colors = [43, 42, 41]  # Yellow, Green, Red backgrounds
    for bg in colors:
        for _ in range(stripe_height):
            print(f"\033[{bg}m" + " " * width + "\033[0m")


# ---------- Task 2: Repeating Pattern ----------

def print_pattern(rows: int = 24, cols: int = 24) -> None:
    # подобранное значение радиуса
    radius = min(rows, cols) // 2 - 2
    # Рисует в верхних четвертях, поэтому смещаем на полтора вниз, чтобы было в центре
    center_y = rows / 1.5
    center_x = cols // 2

    # Функции, возвращают bool если точка (x,y) должна быть раскрашена
    # <= NUM отвечает примерно за толщину линии
    def draw_q1(y, x):
        return x >= center_x and y < center_y and abs(math.hypot(x - center_x, y - center_y) - radius) <= 0.5

    def draw_q2(y, x):
        return x < center_x and y < center_y and abs(math.hypot(x - center_x, y - center_y) - radius) <= 0.5

    # Последовательно вызывать функции для каждой четверти
    for y in range(rows):
        line = []
        for x in range(cols):
            # Проверяем по порядку: Q1, Q2, Q3, Q4
            if draw_q1(y, x + 10):
                line.append('\033[31m#\033[0m')  # Q1 - Red
            elif draw_q2(y, x - 10):
                line.append('\033[32m#\033[0m')  # Q2 - Green
            else:
                line.append(' ')
        print(''.join(line))




# ---------- Task 3: Function graph y = |x| in 1st quadrant ----------

def print_function_graph(height: int = 12, width: int = 24) -> None:
    """Plot y = |x| in first quadrant with axes."""
    for row in range(height):
        line = []
        for col in range(width):
            if row == height - 1 - col:  # диагональная линия y = x
                line.append("\033[31m*\033[0m")  # красная звёздочка
            elif col == 0:  # ось Y
                line.append("\033[36m|\033[0m")  # голубая вертикальная линия
            elif row == height - 1:  # ось X (нижняя строка)
                line.append("\033[36m-\033[0m")  # голубая горизонтальная линия
            else:
                line.append(' ')
        print(''.join(line))
    print("График y = |x| в первом квадранте")

# ---------- Task 4: Percentage ratio chart ----------

def parse_numbers_from_lines(path: str) -> List[float]:
    """
    Извлечение float с каждой строки в файле.
    """
    if not os.path.exists(path):
        print(f"Sequence file '{path}' not found.")
        return []
    
    numbers: List[float] = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, 1):
                line = line.strip()
                
                # Пропускаем пустые строки
                if not line:
                    continue
                
                try:
                    # Пытаемся преобразовать строку в float
                    number = float(line)
                    numbers.append(number)
                except ValueError:
                    # Если строка не является числом, выводим предупреждение и пропускаем
                    print(f"Warning: Line {line_number} contains invalid number: '{line}'")
                    continue
    
    except IOError as e:
        print(f"Error reading file '{path}': {e}")
        return []
    
    return numbers

def parse_sequence_file(path: str) -> List[float]:
    """Обертка на всякий случай"""
    return parse_numbers_from_lines(path)

def compute_even_odd_absolute_averages(nums: List[float]) -> Tuple[float, float]:
    if not nums:
        return 0.0, 0.0
    odd_vals = [nums[i] for i in range(0, len(nums), 2)]      # odd positions
    even_vals = [nums[i] for i in range(1, len(nums), 2)]     # even positions
    avg_odd = abs(sum(odd_vals) / len(odd_vals)) if odd_vals else 0.0
    avg_even = abs(sum(even_vals) / len(even_vals)) if even_vals else 0.0
    return avg_odd, avg_even

def print_percentage_ratio_chart(path: str = "sequence.txt", bar_width: int = 40) -> None:
    nums = parse_sequence_file(path)
    avg_odd, avg_even = compute_even_odd_absolute_averages(nums)
    total = avg_odd + avg_even
    if total == 0:
        print("Cannot build chart (sum of absolute averages is zero or no data).")
        return
    pct_odd = avg_odd / total * 100
    pct_even = avg_even / total * 100
    odd_bar = int(round(bar_width * pct_odd / 100))
    even_bar = int(round(bar_width * pct_even / 100))
    print("Absolute average values (odd vs even positions)")
    print(f"Odd positions avg : {avg_odd:.4f} ({pct_odd:5.1f}%)")
    print(f"Even positions avg: {avg_even:.4f} ({pct_even:5.1f}%)")
    print()
    print(f"Odd  : |\033[33m{'█' * odd_bar}\033[0m{' ' * (bar_width - odd_bar)}| {pct_odd:5.1f}%")
    print(f"Even : |\033[32m{'█' * even_bar}\033[0m{' ' * (bar_width - even_bar)}| {pct_even:5.1f}%")

# ---------- Additional Task: Simple animation (2-3 frames) ----------

def animate_something(frames: int = 3, loops: int = 3, delay: float = 0.1) -> None:
    """Простая анимация с тремя матрицами 5x5."""
    
    # Три разные матрицы
    matrices = [
        [
            ['🌟', '⭐', '✨', '💫', '🌠'],
            ['🔥', '💥', '⚡', '🌙', '☀️'],
            ['🌈', '🌸', '🌺', '🌻', '🌹'],
            ['🍎', '🍊', '🍋', '🍌', '🍇'],
            ['🎵', '🎶', '🎸', '🎹', '🎺']
        ],
        [
            ['A', 'B', 'C', 'D', 'E'],
            ['F', 'G', 'H', 'I', 'J'],
            ['K', 'L', 'M', 'N', 'O'],
            ['P', 'Q', 'R', 'S', 'T'],
            ['U', 'V', 'W', 'X', 'Y']
        ],
        [
            ['1', '2', '3', '4', '5'],
            ['6', '7', '8', '9', '0'],
            ['@', '#', '$', '%', '&'],
            ['+', '-', '*', '/', '='],
            ['!', '?', '.', ',', ';']
        ]
    ]
    
    titles = ["ЭМОДЖИ", "БУКВЫ", "СИМВОЛЫ"]
    
    for loop in range(loops):
        for frame in range(frames):
            # Очищаем экран
            os.system('cls' if os.name == 'nt' else 'clear')
            
            # Выводим текущую матрицу
            for row in matrices[frame]:
                print("  " + " ".join(row))
            
            print()
            time.sleep(delay)


if __name__ == "__main__":
    print("--- Lithuanian Flag ---")
    print_lithuania_flag()
    print()
    print("--- Pattern (quarters of circle) ---")
    print_pattern()
    print()
    print("--- Function Graph y=|x| (first quadrant) ---")
    print_function_graph()
    print()
    print("--- Percentage Ratio Chart (sequence.txt) ---")
    print_percentage_ratio_chart()
    print()
    input("Press Enter to start animation...")
    animate_something()
