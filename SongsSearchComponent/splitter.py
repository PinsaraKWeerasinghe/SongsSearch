import sys
sys.path.insert(0, "/media/pinsara/Education/ACADEMIC_FILES/SEM_7/DM/sinling")

from sinling import word_splitter

def process_word(sentence):
    raw_list = sentence.split()
    temp_list = [] 
    for raw_word in raw_list:
        if len(raw_word) <10:
            temp_list.append(raw_word)
            continue
        result = word_splitter.split(raw_word)
        temp_list.append(result['base'])
        temp_list.append(result['affix'])
    final_query = " "
    for piece in temp_list:
        final_query = final_query+" "+piece  
    return temp_list,final_query

    