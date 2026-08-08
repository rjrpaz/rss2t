"""Entry point for `python -m rss2t`."""
import argparse

from rss2t import app

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--show-url',
        action='store_true',
        help='Print the URL of each feed as it is being processed',
    )
    args = parser.parse_args()

    app.run(show_url=args.show_url)
