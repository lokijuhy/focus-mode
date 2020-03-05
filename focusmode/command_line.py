import argparse
import os

from focusmode.silencers import hide_app, snooze_slack_workspace


APPS_TO_HIDE = ['Mail', 'Slack', 'Skype for Business']
SLACK_WORKSPACES = {
    'kinkeads+': os.environ["SLACK_KINKEADS_LAURA_SNOOZER_TOKEN"],
}
DEFAULT_SNOOZE_TIME = 60


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('time', nargs='?', type=int, default=DEFAULT_SNOOZE_TIME,
                        help="Time duration for Do Not Disturb, in minutes")
    args = parser.parse_args()

    for app in APPS_TO_HIDE:
        hide_app(app)

    for workspace in SLACK_WORKSPACES:
        snooze_slack_workspace(args.time, SLACK_WORKSPACES[workspace])


if __name__ == '__main__':
    main()
