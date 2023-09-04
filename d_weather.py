from typing import List

def get_weather_randomness(temperatures: List[int]) -> int:
    # Здесь реализация вашего решения
    haos_days = 0
    if len(temperatures) == 1:
        haos_days = 1
    else:
        for index in range(1, len(temperatures) - 1):
            if temperatures[index] > temperatures [index - 1] and temperatures[index] > temperatures [index + 1]:
                haos_days +=1
        if temperatures[0] > temperatures[1]:
            haos_days +=1
        if temperatures[-1] > temperatures[-2]:
            haos_days +=1
    return haos_days

def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures

temperatures = read_input()
print(get_weather_randomness(temperatures))