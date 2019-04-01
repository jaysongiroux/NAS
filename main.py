import subprocess
import os
import platform
import webbrowser
try:
    import rumps
except:
    pass


def files():
    exists = os.path.isfile("login.txt")
    if exists:
        with open("login.txt") as f:
            credentials = [x.strip().split(":") for x in f.readlines()]
        for username, password in credentials:
            return credentials[0][0],credentials[0][1]
    else:
        print("file not there")


def osacommand(command):
    os.system(command)


def windowsmount():
    subprocess.call(r'net use y: \\traphouse\storage /user:USERNAME PASSWORD', shell=True)
    subprocess.call(r'net use z: \\traphouse\jason /user:USERNAME PASSWORD', shell=True)


if platform.system() == "Darwin":
    class mount(rumps.App):
        @rumps.clicked("MOUNT STORAGE")
        def mountstorage(self, _):
            os.system(mount_storage)

        @rumps.clicked("MOUNT USER")
        def mountuser(self, sender):
            osacommand(mount_user)

        @rumps.clicked("PLEX")
        def PLEX(self, _):
            webbrowser.get(chrome_path).open(PLEX_URL)

        @rumps.clicked("UNMOUNT all")
        def UNSTORAGE(self, _):
            osacommand(unmount_storage)
            osacommand(unmount_user)


credentials = files()
username = credentials[0]
userquotes="\""+credentials[0]+"\""
password= credentials[1]

mount_storage = """osascript -e 'mount volume "smb://{0}:{1}@TRAPHOUSE/STORAGE"'""".format(username,password)
mount_user = """osascript -e 'mount volume "smb://{0}:{1}@TRAPHOUSE/{0}"' """.format(username,password)

unmount_storage = """osascript -e '
tell application "Finder"
   eject disk "storage"
end tell
'"""

unmount_user = """osascript -e '
tell application "Finder"
   eject disk {0}
end tell
'""".format(userquotes)

PLEX_URL = "https://app.plex.tv/desktop"

chrome_path = "open -a /Applications/Google\ Chrome.app %s" #mac

if platform.system() == "Darwin":
    mount("NAS").run()
else:
    windowsmount()
