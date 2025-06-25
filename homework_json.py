import json
from pprint import pprint

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


    news_str = " ".join(new_list)
    news_list = news_str.split()
    list_word_len = []
    for i in news_list:
        if len(i) > word_min_len:
            list_word_len.append(i)
    word_set = set(list_word_len)
    new_list_word = list(word_set)
    new_list_word.sort(key=len, reverse=True)
    pprint(new_list_word[0:top_words_amt])


if __name__ == '__main__':
    print(read_json(r'D:\homework_file\newsafr.json'))
