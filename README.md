# rss2t

Simple boot to use as a gateway between a RSS feeder and a Telegram channel.

I prefer to use multiple telegram channels with a single bot. Ever RSS can be forwarded to a specific channel. For example, you can group multiple news feeds to a single news channel, multiple entertainment feeds to a separated channel, etc.

Creation of public or private Telegram channel to upload the message goes beyond the scope of this document. You can check some guidelines here:

[https://medium.com/@ljmocic/make-telegram-bot-for-notifying-about-new-rss-feed-items-4cfbcc37f4fd](https://medium.com/@ljmocic/make-telegram-bot-for-notifying-about-new-rss-feed-items-4cfbcc37f4fd)

- *token* is obtained after the bot's creation
- *channel id* can be obtained from channel information

Documentation about configparser module: [https://docs.python.org/3/library/configparser.html](https://docs.python.org/3/library/configparser.html)

Check about html tags supported by the Telegram API here: [https://core.telegram.org/bots/api#html-style](https://core.telegram.org/bots/api#html-style)

## How to use this module

1. Clone this project

    ```bash
    git clone https://github.com/rjrpaz/rss2t.git
    ```

1. Change to project's directory

    ```bash
    cd rss2t.git
    ```

1. Install any requirements for this module:

    ```bash
    pip install -r requirements.txt
    ```

1. Create **local_settings.py** file. This file should include the info about the *bot token* and the *channel id*. Check file named **local_settings.py.sample** to use it as reference.

1. Create a **config.ini** file to define credentials, channel ID and RSS feeds (you can check **config.ini.sample** as a guideline to create your own file).

    'DEFAULT' section should include **bot_token**:

    ```bash
    [DEFAULT]
    bot_token = use_real_token_from_your_bot
    ```

    'CHANNELS' section should include **tag** for each telegram channel along with its **channel_id**:

    ```bash
    [CHANNELS]
    channel1 = channel_id_for_channel1
    channel2 = channel_id_for_channel2
       ...
    ```

    Remaining sections include information about RSS feeds. Each RSS channel should be defined like this:

    ```bash
    [tag_for_this_rss_feed]
    last = 0
    url = rss_feed_url
    channel_id = ${CHANNELS:channel1}
       ...
    ```

    Every feed should have a different tag. Also, channel_id should refer to the tag of the channel according to *CHANNELS* section.

1. Run the module like this:

    ```bash
    python -m rss2t
    ```

## Utils

### ./utils/add_feed.py

Allow to add a new feed to config.ini file. It requires three arguments:

- A name to be used as tag.
- Name of the channel according to the *CHANNELS* section in the ini file.
- An URL for the RSS feed.