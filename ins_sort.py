from copy import deepcopy
from random import randint

import numpy as np
import pandas as pd

arr_len = [10, 20, 40, 80, 160, 320, 640]


def bubble_sort(arr: list) -> (list, int, int):
    """
    Функция для сортировки заданного списка пузырьковой сортировкой.

    Возвращает отсортированный список, количество сравнений, количество перестановок.

    Args:
        arr: Список для сортировки

    Returns:
        Отсортированный список, количество сравнений, количество перестановок.
    """
    count_if = 0
    count_move = 0
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            count_if += 1
            if arr[j] > arr[j + 1]:
                count_move += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr, count_if, count_move


def ins_sort(arr: list) -> (list, int, int):
    """
    Функция для сортировки заданного списка сортировкой вставками.

    Возвращает отсортированный список, количество сравнений, количество перестановок.

    Args:
        arr: Список для сортировки

    Returns:
        Отсортированный список, количество сравнений, количество перестановок.
    """
    count_if = 0
    count_move = 0
    for idx in range(1, len(arr)):
        value = arr[idx]
        i = idx - 1
        while i >= 0:
            count_if += 1
            if arr[i] > value:
                count_move += 1
                arr[i + 1] = arr[i]
                i = i - 1
            else:
                break
        arr[i + 1] = value
    return arr, count_if, count_move


def sort_comp(arr_len: int) -> (int, int, int, int, int):
    arr = []
    for _ in range(arr_len):
        arr.append(randint(-100, 100))
    print("Исходный массив ", arr)
    print("======Количество элементов====== ", arr_len)
    bubble_arr, bubble_count_if, bubble_count_move = bubble_sort(deepcopy(arr))
    print("Пузырьковая сортировка", bubble_arr)
    print(f"Количество сравнений: {bubble_count_if} " f"Количество перестановок: {bubble_count_move}")
    ins_arr, ins_count_if, ins_count_move = ins_sort(deepcopy(arr))
    print("Сортировка вставками ", ins_arr)
    print(f"Количество сравнений: {ins_count_if} " f"Количество перестановок: {ins_count_move}")
    return arr_len, bubble_count_if, bubble_count_move, ins_count_if, ins_count_move