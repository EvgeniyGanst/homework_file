import json
from pprint import pprint
from collections import Counter

def read_json(file_path, word_min_len=6, top_words_amt=10):
    """
    функция для чтения файла с новостями.
    """
    with open(file_path, encoding='utf=8') as f:
        json_data = json.load(f)


    dict_news = json_data["rss"]["channel"]["items"]
    new_list = []
    for rows in dict_news:
        row = rows["description"]
        new_list.append(row)

    news_str = " ".join(new_list)#делаем из списка строку
    news_list = news_str.split()#разбиваем строку в список слов

    list_word_len = []
    for i in news_list:
        if len(i) > word_min_len:
            list_word_len.append(i)
    new_cnt = Counter(list_word_len).most_common(top_words_amt)
    top_word = list(dict(new_cnt).keys())
    return top_word
    
    
    
if __name__ == '__main__':
    print(read_json(r'D:\homework_file\newsafr.json'))
