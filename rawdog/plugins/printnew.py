# printnew.py: email new entries to ourselves (or anyone we want)
# Copyright 2005, 2009 Ted T <http://perljam.net/>

import rawdoglib.rawdog
import rawdoglib.plugins
from rawdoglib.rawdog import encode_references
import smtplib
import datetime
from email.MIMEText import MIMEText


class Mailer:
    """email new articles"""

    def article_added(self, rawdog, config, article, now):
        """Handle new articles using the article_seen hook."""

        mail_str = ""

        # Return immediately if nobody to send to
        if (not self.mailto):
            return True

        feed = rawdog.feeds[article.feed]

        if article.entry_info.has_key('title'):
            mail_str += "%s\n" % article.entry_info['title']
        if article.entry_info.has_key('link'):
            mail_str += "%s\n\n" % article.entry_info['link']
        # mail_str += ' [' + feed.get_html_link(config) + ']'

        #if article.entry_info.has_key('description'):
        #    mail_str += "%s\n" % article.entry_info['description']
 
        msg = MIMEText(encode_references(mail_str))
        if article.entry_info.has_key('title'):
            msg['Subject'] = article.entry_info['title']
        else:
            msg['Subject'] = ""
        msg['To'] = self.mailto
        msg['From'] = self.mailfrom

        SENDMAIL = "/usr/sbin/sendmail" # sendmail location
        import os
        p = os.popen("%s -t" % SENDMAIL, "w")
        p.write(msg.as_string())
        sts = p.close()

        return True

    # We expect 'mailto' and 'mailfrom' to be in the config now.
    def config(self, config, name, value):
        if name == 'mailto':
            self.mailto = value
            return False
        elif name == 'mailfrom':
            self.mailfrom = value
            return False
        else:
            return True


mailer = Mailer()

# actually attach our hooks now.
rawdoglib.plugins.attach_hook("article_added", mailer.article_added)
rawdoglib.plugins.attach_hook("config_option", mailer.config)


