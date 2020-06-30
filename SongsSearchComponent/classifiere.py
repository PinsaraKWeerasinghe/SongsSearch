
movie_list = ['චිත්‍රපට','සිනමා']
music_list = [ 'සංගීතමය', 'සංගීතවත්','අධ්‍යක්ෂණය', 'සංගීත']
genre_list = ['පැරණි', 'පොප්ස්','පොප්','පරණ','ක්ලැසික්','ක්ලැසි','ඉල්ලීම','චිත්‍රපට','නව']
artist_list = ['කීව', 'කී', 'ගායනා කරන', 'ගයන', 'ගායනා','‌ගේ', 'හඩින්', 'කියනා', 'කිව්ව', 'කිව්', 'කිව', 'ගායනය', 'ගායනා කළා', 'ගායනා කල', 'ගැයූ']
creater_list = ['ලියා', 'ලියූ', 'ලිව්ව', 'ලිව්', 'රචනා',  'ලියා ඇති', 'රචිත', 'ලියන ලද','ලියන', 'හදපු', 'පද', 'රචනය', 'හැදූ', 'හැදුව', 'ලියන', 'ලියන්න','ලීව', 'ලියපු', 'ලියා ඇත', 'ලිඛිත']
super_list = ['සුපිරි', 'නියම', 'පට්ට','ඉහළම', 'හොඳ', 'හොඳම', 'එලකිරි', 'එළකිරි', 'සුප්පර්', 'සුප්රකට', 'ඉහල',  'වැඩිපුර', 'වැඩිපුරම', 'සුප්‍රකට', 'ජනප්රිය', 'ජනප්රියම', 'ජනප්‍රිය', 'ජනප්‍රියම', 'ප්‍රකට', 'ප්‍රසිද්ධ']



def classify_query(token_list,default_amount,raw_string):
    nothing_special = True
    result = get_base_result()
    result['total'] = {
        'total':default_amount,
        'rating':False
    }
   
    result,nothing_special = classify_list(token_list,result,nothing_special)

    result = mark_nothing_special(result,nothing_special)

    result = check_rating(result,raw_string)

    result_amount = 0
    for token in token_list:
        if (token.isnumeric()):
            if (int(token)<default_amount):
                result['total']['total'] = int(token)
            else:
                result['total']['total'] = default_amount
        break
    
    return result
    

def classify_list(token_list,result_obj,nothing_special):
    result = result_obj
    for token in token_list:
        if token in movie_list:
            nothing_special = False
            result['movie'] = True
            result['genere'] = True
        elif token in genre_list:
            nothing_special = False
            result['genere'] = True
        elif token in music_list:
            nothing_special = False
            result['music by'] = True
        elif token in artist_list:
            nothing_special = False
            result['artist'] = True
        elif token in creater_list:
            nothing_special = False
            result['lyrics by'] = True
    return result,nothing_special

def  mark_nothing_special(result,nothing_special):
    if (nothing_special):
        result['name'] = True
        result['lyrics'] = True
    return result

def check_rating(result,raw_string):
    for rating_word in super_list:
        if rating_word in raw_string:
            result['total']['rating'] = True
            break
    return result

def get_base_result():
    RESULT = {
        'name':False,
        'lyrics':False,
        'movie':False,
        'artist':False,
        'genere':False,
        'music by':False,
        'lyrics by':False,
        'total':0
    }
    return RESULT