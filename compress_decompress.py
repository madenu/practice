# Compression / Decompression
# https://techdevguide.withgoogle.com/resources/former-interview-question-compression-and-decompression/#!

def decompress(in_str):
    if "[" in in_str:
        open_bracket = in_str.find("[")
        repeat = int(in_str[:open_bracket])

        next_open_bracket = in_str.find("[", open_bracket + 1)
        next_close_bracket = in_str.find("]")
        last_close_bracket = in_str.rfind("]")
        matching_close_bracket = next_close_bracket
        if next_open_bracket < next_close_bracket:
            matching_close_bracket = last_close_bracket

        target_str = in_str[open_bracket + 1:matching_close_bracket]
        leftover_str = in_str[matching_close_bracket + 1:] if matching_close_bracket < len(in_str) else ""
        return (repeat * decompress(target_str)) + decompress(leftover_str)

    return in_str



if __name__ == "__main__":
    test_str = "3[abc]15[b]2[0]"
    test_str_2 = "2[3[a]b]"
    test_str_3 = "2[10[3[2[ab]c]d]]"
    print(decompress(test_str))
    print(decompress(test_str_2))
    print(decompress(test_str_3))
