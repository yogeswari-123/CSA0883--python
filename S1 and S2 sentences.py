def remove_common_words(S1, S2):
    
    words_S1 = S1.split()
    words_S2 = S2.split()

    set_S1 = set(words_S1)
    set_S2 = set(words_S2)
    common_words = set_S1 & set_S2


    filtered_S1 = [word for word in words_S1 if word not in common_words]
    filtered_S2 = [word for word in words_S2 if word not in common_words]

   
    result_S1 = " ".join(filtered_S1)
    result_S2 = " ".join(filtered_S2)

    return result_S1, result_S2


S1 = "sky is blue in color"
S2 = "Raj likes sky blue color"


result_S1, result_S2 = remove_common_words(S1, S2)
print(result_S1)  
print(result_S2)  
