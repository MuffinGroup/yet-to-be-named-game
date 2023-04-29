from typing import Tuple

def parse_input(input_str: str) -> Tuple[str, int, int]:
    test_str = input_str.lower()
    components = test_str.split(" ")
    
    command = " ".join(components[0:-2])
    x, y = (int(components[-2]), int(components[-1]))
    
    return command, x, y

print(parse_input("/place gass 100 10"))