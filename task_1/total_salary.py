from pathlib import Path
from typing import Tuple

def total_salary(path: str) -> Tuple[float, float]:
    total, average = 0, 0

    try:
        with open(path, "r") as file:
            salary_lines = file.readlines()
            
            for salary_line in salary_lines:
                _, salary = salary_line.split(",")
                total += float(salary.strip())

        average = total / (len(salary_lines) or 1)
    except FileNotFoundError as error:
        print("Error: file not found, enter valid path")

    return (total, average)

salaries_path = f"{Path(__file__).absolute().parent}/salaries.txt"

total, average = total_salary(salaries_path)

print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

