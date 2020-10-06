"""
Name: Nikit Parakh
Project 2 - Hybrid Sorting - Starter Code
CSE 331 Fall 2020
Professor Sebnem Onsay
"""
from typing import List, Any, Dict


def hybrid_sort(data: List[Any], threshold: int) -> None:
    """
    Wrapper function to call merge_sort. Takes in a list and threshold
    and sorts the list accordingly.
    """
    merge_sort(data, threshold)


def inversions_count(data: List[Any]) -> int:
    """
    This function calls merge_sort, which in conjunction with merge, calculates
    the number of inversions in a given list. Takes in a list of data, sorts it,
    and returns number of inversions
    """
    return merge_sort(data)


def merge(subarray1, subarray2, data, mid):
    """
    Merge two sorted Python Lists S1 and S2 into properly sized list S
    and calculates inversions while merging. Takes in the array and two subarrays,
    and the index of the point where the subarrays were created. While merging the
    list, pairs of items are compared to check if they are inverted, and are added
    to the count if so. The inversion count is returned.
    """
    inversions = i = j = 0
    while i+j < len(data):
        if j == len(subarray2) or (i < len(subarray1) and subarray1[i] <= subarray2[j]):
            data[i+j] = subarray1[i]
            i += 1
        else:
            inversions += mid - i
            data[i+j] = subarray2[j]
            j += 1
    return inversions


def merge_sort(data: List[Any], threshold: int = 0) -> int:
    """
    This function takes a list and a threshold, and sorts it accordngly.
    It runs recursively and splits the list in two at every call, sorts it using
    merge function and calculates the inversion count of the list. If threshold is given
    insertion sort is used whenever size of subarray is less than threshold for efficiency
    Returns number of total inversions by calculating inversions at each step.
    """
    length = len(data)
    if length < 2:
        return 0
    if length < threshold:
        insertion_sort(data)
        return 0
    inversions = 0
    mid = length // 2
    subarray1 = data[0:mid]
    subarray2 = data[mid:length]
    inversions += merge_sort(subarray1)
    inversions += merge_sort(subarray2)
    inversions += merge(subarray1, subarray2, data, mid)
    return inversions


def insertion_sort(data: List[Any]) -> None:
    """
    Loops over list to sort it using insertion. Checks if following element is
    larger than the preceding one, and swaps them. Does this for the entire list till
    it is sorted.
    """
    for i in range(1, len(data)):
        j = i
        while (j > 0) and (data[j] < data[j - 1]):
            data[j], data[j - 1] = data[j - 1], data[j]
            j -= 1


def find_match(user_interests: List[str], candidate_interests: Dict[str, List]) -> str:
    """
    This function takes in a users preferences as a list, and a dictionary
    of candidates and their preferences. It assigns every preference a rank (index
    in user_interests) and then uses those ranks to calculate how many inversions
    (out of place preferences) the candidates has. Returns the name of candidate with
    fewest inversions.
    """
    # assign every preference a rank
    user = {i: index for index, i in enumerate(user_interests)}
    inversion_dict = {}
    for key, value in candidate_interests.items():
        # for every candidate, use those ranks to create a list according
        # to the candidates preferences, and then calculate inversions
        candidate_rank_list = [user[i] for i in value]
        inversion_dict[key] = inversions_count(candidate_rank_list)
    # return name of candidate with fewest inversions
    return min(inversion_dict, key=lambda x: inversion_dict[x])
