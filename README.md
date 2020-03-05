# focus-mode

Hide distracting apps and snooze Slack messages across multiple workspaces.

Just run `focusmode` on the command line!

Defaults to snoozing notifications for 1 hour.
Run `focusmode 30` or any other number to specify number of minutes to snooze.

### App Hiding
App hiding only works on Mac! Apps are still running, they're just hidden as in Command-H.

By default, hides:
 - Mail
 - Slack
 - Skype for Business

Modify the `APPS_TO_HIDE` variable in `focusmode/command_line.py` to hide different apps.

### Slack Snoozing
Snoozes Slack notifications. Requires a Slack App, which the token registered as an environment variable.
See [this tutorial](https://medium.com/@jakebathman/setting-up-a-slack-app-for-use-with-ios-shortcuts-e8e16b15d0f3)
for how to create a Slack app and get its associated OAuth token.
Modify the `SLACK_WORKSPACES` variable in `focusmode/command_line.py` to match your workspace and token variable names.
