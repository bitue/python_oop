def hash_dic (words):
    dict_words ={}
    for word in words :
        res = ''.join(sorted(word))
        try :
            if dict_words[res] :
                if word in dict_words[res] :
                    pass
                else :
                    dict_words[res].append(word)

            # else :
            #     dict_words[res].append(word)
        except:
            dict_words[res] = [word]
    
    # print(dict_words)
    arr = []
    for i in dict_words:
        arr.append(dict_words[i])
    print(arr)



hash_dic(['eat', 'ate', 'done', 'tea', 'soup', 'node', "bitue", "biteu", "am"])






        






    
   







       

