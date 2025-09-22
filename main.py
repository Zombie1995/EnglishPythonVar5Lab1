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

def print_pattern(rows: int = 24, cols: int = 24, start_quarter: int = 1) -> None:
    radius = min(rows, cols) // 2 - 2
    center_y = rows / 1.5
    center_x = cols // 2

    # Map quarter number to function and color
    def draw_q1(y, x):
        return x >= center_x and y < center_y and abs(math.hypot(x - center_x, y - center_y) - radius) <= 0.7

    def draw_q2(y, x):
        return x < center_x and y < center_y and abs(math.hypot(x - center_x, y - center_y) - radius) <= 0.7

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
            # В первом квадранте |x| = x, поэтому просто y = x
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

def parse_sequence_file(path: str) -> List[float]:
    if not os.path.exists(path):
        print(f"Sequence file '{path}' not found.")
        return []
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Split by whitespace or commas / semicolons
    tokens = re.split(r"[\s,;]+", content.strip())
    nums: List[float] = []
    for t in tokens:
        if not t:
            continue
        try:
            nums.append(float(t))
        except ValueError:
            pass  # ignore invalid tokens
    return nums

def compute_even_odd_absolute_averages(nums: List[float]) -> Tuple[float, float]:
    if not nums:
        return 0.0, 0.0
    odd_vals = [nums[i] for i in range(0, len(nums), 2)]      # 1-based odd positions
    even_vals = [nums[i] for i in range(1, len(nums), 2)]     # 1-based even positions
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

def animate_flag(frames: int = 3, loops: int = 3, width: int = 36, stripe_height: int = 3, delay: float = 0.25) -> None:
    """Simple waving animation of the Lithuanian flag using horizontal shifts."""
    colors = [43, 42, 41]
    shifts = [0, 2, 4][:frames]
    for _ in range(loops):
        for s in shifts:
            os.system('cls' if os.name == 'nt' else 'clear')
            for bg in colors:
                for h in range(stripe_height):
                    # create a sine-based offset per line for wavy look
                    offset = int(2 * math.sin((h + s) / 2))
                    left_pad = ' ' * ((s + offset) % 6)
                    print(left_pad + f"\033[{bg}m" + " " * width + "\033[0m")
            print("(Lithuania flag animation)")
            time.sleep(delay)

# ---------- Orchestration ----------

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
    animate_flag()
