# def reverse_string(s: str) -> str:
#     if s == "":
#         return ""
#     return reverse_string(s[1:]) + s[0]
#
#
# print(reverse_string("Привіт"))

#2
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


def hello():
    print("Привет!")


hello = repeat(3)(hello)

hello()

