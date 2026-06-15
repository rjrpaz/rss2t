# rss2t

Simple boot to use as a gateway between a RSS feeder and a Telegram channel.

I prefer to use multiple telegram channels with a single bot. Every RSS feed
can be forwarded to a specific channel. For example, you can group multiple
news feeds to a single news channel, multiple entertainment feeds to a
separated channel, etc.

Creation of public or private Telegram channel to upload the message goes
beyond the scope of this document. You can check some guidelines here:

[https://medium.com/@ljmocic/make-telegram-bot-for-notifying-about-new-rss-feed-items-4cfbcc37f4fd](https://medium.com/@ljmocic/make-telegram-bot-for-notifying-about-new-rss-feed-items-4cfbcc37f4fd)

- *token* is obtained after the bot's creation
- *channel id* can be obtained from channel information

Documentation about configparser module:
[https://docs.python.org/3/library/configparser.html](https://docs.python.org/3/library/configparser.html)

Check about html tags supported by the Telegram API here:
[https://core.telegram.org/bots/api#html-style](https://core.telegram.org/bots/api#html-style)

## Creating a Telegram channel for this bot

1. In Telegram, tap the pencil icon → **New Channel**. Choose a name and set
   the channel type to **Private**.

1. Open the channel → **Administrators** → **Add Admin** → search for
   `@rss2t_bot` and add it. Grant at least the **Post Messages** permission.

1. Get the channel's numeric ID. The easiest way is to call the `getUpdates`
   endpoint after the bot is an admin:

    ```bash
    curl "https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates"
    ```

    Look for a `channel_post` object — the value at `chat.id` is the channel
    ID. It will be a negative number starting with `-100`,
    e.g. `-1001234567890`.

    > If `getUpdates` returns nothing, post a message in the channel first so
    > the bot registers an update.

1. Add the channel to the `[CHANNELS]` section of `config.ini`:

    ```ini
    [CHANNELS]
    mychannel = -1001234567890
    ```

1. Verify the bot can post to it:

    ```bash
    python utils/send_test_message.py mychannel
    ```

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

1. Create a **config.ini** file to define credentials, channel IDs and RSS
   feeds (you can check **config.ini.sample** as a guideline).

    `DEFAULT` section should include **bot_token**:

    ```ini
    [DEFAULT]
    bot_token = use_real_token_from_your_bot
    ```

    `CHANNELS` section should include a **tag** for each Telegram channel
    along with its numeric **channel_id**:

    ```ini
    [CHANNELS]
    channel1 = channel_id_for_channel1
    channel2 = channel_id_for_channel2
    ```

    Remaining sections define RSS feeds. Each feed should look like this:

    ```ini
    [tag_for_this_rss_feed]
    last = 0
    url = rss_feed_url
    channel_id = ${CHANNELS:channel1}
    ```

    Every feed must have a unique tag. `channel_id` must reference a tag
    defined in the `CHANNELS` section.

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
