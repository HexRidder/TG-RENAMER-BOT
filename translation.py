from sample_config import Config

class Translation(object):
    START_TEXT = """<b>Hello <b>{}</b>,
    
I'm A Simple File Renamer Bot With Permanent Thumbnail support!💯

Send me any Telegram file and select rename option.

Click /help for more details....

You must subscribe our channel in order to use me😇<b>"""
    RENAME_403_ERR = "Sorry. You are not permitted to rename this file."
    ABS_TEXT = " Please don't be selfish."
    UPGRADE_TEXT = "There is no upgrade plan till now it will be added in future"
    DOWNLOAD_START_VIDEO = "Downloading to my server.....📥"
    DOWNLOAD_START = "Downloading to my server.....📥"
    UPLOAD_START_VIDEO = "Uploading as video.....📤"
    UPLOAD_START = "Uploading as File.....📤"
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations.I can't do anything for that 🤷‍♂️."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "**Thank you for Using [Nexon Project's](https://t.me/NexonHex) bot.**"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds.\nUploaded in {} seconds."
    NOT_AUTH_USER_TEXT = "Please /upgrade your subscription."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Free Users can only upload: {}\nPlease /upgrade your subscription.\nIf you think this is a bug, please contact <a href='https://t.me/NexonHex_grp'>Support Group</a>"
    SAVED_CUSTOM_THUMB_NAIL = "Custom File thumbnail saved ✅️ . This image will be deleted with in 24hr"
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    SAVED_RECVD_DOC_FILE = "Document Downloaded Successfully."
    CUSTOM_CAPTION_UL_FILE = "@NexonHex"
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    HELP_USER = """<b>Hey.. It's not that complicated😅

Follow These steps..
    
⚡ Send an image and it will be saved as your permanent Thumbnail

⚡ Now send your file

⚡ Select rename option and enter your new name ( extension is not required )

NOTE : You must join our channel in order to use me<b>"""
    REPLY_TO_DOC_FOR_RENAME_FILE = "🤦‍♂️ Reply to a Telegram media to `/rename New Name.extension` with custom thumbnail support.\n\n(For uploading as file).\n\nSee /help for mor information. "
    REPLY_TO_DOC_FOR_RENAME_VIDEO = "🤦‍♂️ Reply to a Telegram media to `/rename_video New Name.extension` with custom thumbnail support.\n\n(For uploading as video).\n\nSee /help for mor information."
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction."
    FREE_USER_LIMIT_Q_SZE = """Cannot Process.
Free users only 1 request per 30 minutes.
/upgrade or Try 1800 seconds later."""
    IFLONG_FILE_NAME = """File Name limit allowed by Telegram is {alimit} characters.
The given file name has {num} characters.

<b>Essays Not allowed in Telegram file name!</b>
©️ <code>@RenamerNxbot</code>
Please short your file name and try again!"""

    About = """Hi __{}__,

**📝 Language:** Python 3

**🧰 Framework:** Pyrogram

**👨‍💻 Developer:** [Hexrider](https://t.me/Hexrider)

**📮 Channel:** [Nexon Project's](https://t.me/NexonHex)

**👥 Group:** [Nexon Support](https://t.me/Nexonhex_grp)

**💻 Source Code:**[Press Me](https://github.com/Hexridder/Nexon-Bot)"""
