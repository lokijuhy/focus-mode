import requests
from subprocess import Popen, PIPE


def hide_app(app):
    hide_apple_script = '''
        tell application "Finder"
            if exists application process "{0}" then
              set visible of application process "{0}" to false
            end if
        end tell
    '''

    script = hide_apple_script.format(app)
    p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE, encoding='utf8')
    stdout, stderr = p.communicate(script)
    if p.returncode != 0:
        print(p.returncode, stdout, stderr)


def snooze_slack_workspace(time, token):
    snooze_api_url = 'https://slack.com/api/dnd.setSnooze?num_minutes={}&pretty=1'.format(time)
    headers = {'Authorization': 'access_token {}'.format(token)}
    data = [('token', token)]

    response = requests.post(snooze_api_url, headers=headers, data=data)

    if '"ok": true' not in response.text:
        print(response)
