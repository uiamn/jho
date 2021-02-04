import re

KATAKANA_REGEX = re.compile(r'[\u30A1-\u30FF]+')
IGNORE_CHARS_REGEX = re.compile(r'[ァィゥェォャュョ]')

def is_conform(t: str) -> bool:
    """JISに適合してゐるかをチェックする関数

    Args:
        t (str): チェックしたい語

    Returns:
        bool: 適合してゐるかどうか 具体的には以下のいづれかを満たす場合にはTrueを返す
        * 最初が"ー"である(この条件を満たす場合には形態素解析にバグが無い限り"ー"のみからなる文字列のため)
        * 最後が"ー"ではない
        * カタカナからなる語ではない
        * 文字列長が3以下
        * tの音数が2音以下
        ただし音数とは，最後の長音を含めない総文字数-文字列に含まれる"ァィゥェォャュョ"の個数のことを云ふ
    """
    if len(t) == 0:
        return True

    return (
        t[0] == 'ー'
        or t[-1] != 'ー'
        or KATAKANA_REGEX.fullmatch(t) is None
        or len(t) <= 3
        or len(t) - len(IGNORE_CHARS_REGEX.findall(t)) <= 3
    )

if __name__ == "__main__":
    while w := input('input > '):
        print(is_conform(w))
