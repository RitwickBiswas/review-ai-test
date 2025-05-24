def twoSum(nums: list[int], target: int) -> list[int]:
        index_map = {}
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in index_map:
                return [index_map[compliment], i]
            index_map[num] = i

if __name__ == "__main__": 
    nums = [3, 2, 4]
    target = 6
    result = twoSum(nums=nums, target=target)
    print(f"Indices: {result}")  # Outputs: Indices: [1, 2]