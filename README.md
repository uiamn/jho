# JHO

A bot that sends out a reply when it finds a Tweet that does not conform to JIS Z8301:2008 Annex G.

## Getting Started
### setup
1. Submit a Twitter developer application to get a consumer key and a consumer secret key.
2. Modify the `src/.env` as follows:
```
CK=<your consumer key>
CSK=<your consumer secret key>
AT=<the access token of the account you want to make into a bot>
ATS=<the access token secret of the bot>
```
3. Follow the user who sends you a reply with that bot.

### using Docker
```
$ docker-compose up
```
When you input the above command, it acquires 200 tweets for the first time, and after the second and subsequent times, it acquires up to 200 tweets that were posted after the previous command. After that, we will make a judgment and reply.

### not using Docker
TODO

NOTE: In both cases, it is recommended that you use cron to run the program at regular intervals.

## License
MIT
