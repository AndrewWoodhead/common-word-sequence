import collections
import helpers
    
def main(n: "int" =100) -> "any":
    read_data = helpers.read_input()
    sanitized_text = helpers.sanitize_text_string(read_data)
    seq_count_dict = helpers.count_word_sequences(sanitized_text, 3)

    print(collections.Counter(seq_count_dict).most_common(n))

if __name__ == '__main__':
    main()