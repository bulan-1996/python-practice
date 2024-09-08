import re
from collections import Counter

"""
問題:単語の並べ替えによるパズル解決
与えられた文字が以下のルールに従って変換された文字列だと定義します。
1.各単語はランダムな順番でシャッフルされていますが、最初の最後の文字は元のままです。
2.単語の順序は保たれます。

実施内容
与えられたシャッフルされた文字列を、元の形に戻すプログラムを作成
正しい単語の形は、あらかじめ辞書(words.txtなど)として与える
この辞書には、可能なすべての正しい単語が含まれています
"""
def load_dictionary(file_path):
    """
    辞書ファイルから単語のリストを読み込む関数。
    :param file_path: 辞書ファイルのパス
    :return: 単語のリスト
    """
    # open(file_path, 'r'): 指定されたパス（file_path）にあるファイルを「読み込みモード（'r'）」で開く
    with open(file_path,'r') as f:
        return [line.strip() for line in f] #strip(): 文字列の前後にある空白文字や改行を削除する

def unscramble_word(scrambled_word, dictionary):
    """
    シャッフルされた単語を元の単語に復元する関数。
    :param scrambled_word: シャッフルされた単語
    :param dictionary: 正しい単語のリスト
    :return: 元の単語（辞書に基づく）
    """
    # シャッフルされた部分
    scrambled_word_counter = Counter(scrambled_word) # collections.Counterで各文字の出現回数をカウント

    # 可能性のある単語を辞書から探す
    for word in dictionary:
        word_counter = Counter(word)
         # すべての要素がTrueであればTrueをリターン
         # scrambledにword_counterのすべての文字が含まれる場合
        if all(scrambled_word_counter[char] >= word_counter[char] for char in word_counter):
            return word

    return scrambled_word # 見つからない場合はそのまま返す

def unscramble_sentence(sentence, dictionary):
    """
    シャッフルされた文全体を復元する関数
    :param sentence: シャッフルされた文
    :param dictionary: 正しい単語のリスト
    :return: 復元された文
    """
    words = re.findall(r'\w+|\W+', sentence) # 単語と記号を保持するための正規表現
    unscramble_words = [] # 復元された単語を格納するリスト

    for word in words:
        # もし単語であれば(句読点でない場合)
        if word.isalpha():
            unscrambled_word  = unscramble_word(word, dictionary)
            unscramble_words.append(unscrambled_word )
        else:
            unscramble_words.append(word) # 句読点はそのまま追加
    # 復元された文字を返す
    return ''.join(unscramble_words)

if __name__ == '__main__':
    # 辞書をロード
    dictionary = load_dictionary('C:\Programe\python3\python-practice\src\\words.txt')

    # 入力されたシャッフルされた文
    sentence = 'hlelao wlrod!'

    # 文を復元
    restored_sentence = unscramble_sentence(sentence, dictionary)

    # 結果を表示
    print("復元された文:", restored_sentence)
