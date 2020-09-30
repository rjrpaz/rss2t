# rss2t

Simple boot to use as a gateway between a RSS feeder and a Telegram channel.

Creation of public or private Telegram channel to upload the message goes beyond the scope of this document. You can check some guidelines here:

[https://medium.com/@ljmocic/make-telegram-bot-for-notifying-about-new-rss-feed-items-4cfbcc37f4fd](https://medium.com/@ljmocic/make-telegram-bot-for-notifying-about-new-rss-feed-items-4cfbcc37f4fd)

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

1. Create a **config.ini** file to define the RSS feeds (you can check **config.ini.sample** as a guideline to create your own file).

    Each RSS feed should be defined like this:

    ```bash
    [tag_for_this_rss_feed]
    last = 0
    url = rss_feed_url
    ```

    Each feed should have its own tag.

1. Run the module like the following:

    ```bash
    python -m rss2t
    ```
