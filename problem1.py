def count_vowels_and_consonants(text: str) -> dict:
    unli = "aeiou"
    natija = {"unli":0, "undosh":0}
    for harf in text.lower():
        if harf.isalpha():
            if harf in unli:
                natija["unli"] += 1
            else:
                natija["undosh"] +=1
    return natija
print(count_vowels_and_consonants("Salom Dunyo!"))