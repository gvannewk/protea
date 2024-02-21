#Nothin here yet
import replicate

output = replicate.run(
    "andreasjansson/codellama-7b-instruct-gguf:f017a401d8f2f15896f8d9c8fb605d873ac521149394033b62e51aae13146113",
    input={
        "top_k": 10,
        "top_p": 0.95,
        "prompt": "Write a short program that counts the number of occurrences of a character in a string.",
        "grammar": "root        ::= \"```python\\ndef num_occurrences(c: str, s: str) -> int:\\n    \" code \"```\"\ncode        ::= [^`()]+",
        "max_tokens": 500,
        "temperature": 0.8,
        "mirostat_mode": "Disabled",
        "repeat_penalty": 1.1,
        "mirostat_entropy": 5,
        "presence_penalty": 0,
        "frequency_penalty": 0,
        "mirostat_learning_rate": 0.1
    }
)

# The andreasjansson/codellama-7b-instruct-gguf model can stream output as it's running.
# The predict method returns an iterator, and you can iterate over that output.
for item in output:
    # https://replicate.com/andreasjansson/codellama-7b-instruct-gguf/api#output-schema
    print(item, end="")