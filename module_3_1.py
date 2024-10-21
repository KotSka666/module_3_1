calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    len_ = len(string)
    upper_ = string.upper()
    lower_ = string.lower()
    return len_, upper_, lower_

def is_contains(string, list_search):
    count_calls()
    if any([string.upper() == i.upper() for i in list_search]):
        return True
    else:
        return f'{False}'

print(string_info("Привет"))
print(is_contains("Пока", ["123", "хай", "покА"]))
print(calls)

print(string_info("Привет"))
print(is_contains("Пока", ["123", "хай"]))
print(calls)