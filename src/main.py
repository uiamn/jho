import MeCab
import tweepy
import dotenv
import os
from typing import List

from is_conform import is_conform

# global variables
DEBUG = False
LTI_FILEPATH = os.path.join(os.path.dirname(__file__), 'LATEST_TWEET_ID')

# MeCab
mcb = MeCab.Tagger(
    '-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd'
)

# env
dotenv.load_dotenv(verbose=True)
dotenv.load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

# twitter
auth = tweepy.OAuthHandler(os.environ.get('CK'), os.environ.get('CSK'))
auth.set_access_token(os.environ.get('AT'), os.environ.get('ATS'))
api = tweepy.API(auth)


def main() -> None:
    if DEBUG:
        s = '0'
        while s != '':
            s = input('DEBUG MODE > ')
            print(detect_and_correct(s))
    else:
        tl: List[tweepy.Status] = get_timeline()
        for t in tl:
            tweet = t.text
            if tweet[:4] == 'RT @':
                continue
            res = detect_and_correct(tweet)
            if len(res) > 0:
                reply(t, res)


def get_timeline() -> List[tweepy.Status]:
    if os.path.isfile(LTI_FILEPATH):
        with open(LTI_FILEPATH) as f:
            latest_tweet_id = int(f.readline().replace('\n', ''))
    else:
        latest_tweet_id = None

    if DEBUG:
        tl = api.home_timeline(count=200)
        for t in tl:
            print(t.text)
    else:
        if latest_tweet_id is None:
            tl = api.home_timeline(count=200)
        else:
            tl = api.home_timeline(since_id=latest_tweet_id, count=200)

    # update LATEST_TWEET_ID
    if len(tl) > 0:
        with open(LTI_FILEPATH, 'w') as f:
            f.write(str(tl[0].id))

    return tl


def detect_and_correct(tweet: str) -> List[str]:
    tweet = tweet.replace(' ', '.')
    p = mcb.parse(tweet)
    p = p.split('\n')[:-2]
    p = [a.replace('\t', ',').split(',') for a in p]

    res = []

    for i, line in enumerate(p):
        if not is_conform(w := line[0]):
            while w[-1] in ['ー', '〜', '-', '~']:
                w = w[:-1]
            res.append(w)
        elif i >= 2 and line[0] == 'ー':
            # 検索避け用の記号を検出する
            if p[i-1][0] in [',', '.', '_', '|', "'", ' ']:
                res.append(p[i-2][0])

    return res


def reply(status: tweepy.Status, res: List[str]) -> None:
    """指摘するリプライを飛ばします

    Args:
        status (tweepy.Status): 元のtweetのstatus
        res (List[str]): 指摘する内容
    """
    tweet = f'@{status.author.screen_name} JISなら{"，".join(sorted(set(res), key=res.index))}では？🤔🤔🤔'
    api.update_status(status=tweet, in_reply_to_status_id=status.id)


if __name__ == "__main__":
    main()
