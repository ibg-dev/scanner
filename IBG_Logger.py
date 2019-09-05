#!/usr/bin/python3

import logging
from logging import handlers

receipent_email = "YOUR EMAIL HERE"
sender_email = "APP SERVICE EMAIL HERE"

class TlsSMTPHandler(logging.handlers.SMTPHandler):
    def emit(self, record):
        """
        Emit a record.
        Format the record and send it to the specified addressees.
        """
        try:
            import smtplib
            try:
                from email.utils import formatdate
            except ImportError:
                formatdate = self.date_time
            port = self.mailport
            if not port:
                port = smtplib.SMTP_PORT
            smtp = smtplib.SMTP(self.mailhost, port)
            msg = self.format(record)
            msg = "From: %s\r\nTo: %s\r\nSubject: %s\r\nDate: %s\r\n\r\n%s" % (
                self.fromaddr,
                self.toaddrs,
                self.getSubject(record),
                formatdate(), msg)
            if self.username:
                smtp.ehlo()  # for tls add this line
                smtp.starttls()  # for tls add this line
                smtp.ehlo()  # for tls add this line
                smtp.login(self.username, self.password)
            smtp.sendmail(self.fromaddr, self.toaddrs, msg)
            smtp.quit()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)

logger = logging.getLogger(__name__)
logger.setLevel('INFO')

log_console_handler = logging.StreamHandler()
log_file_handler = logging.FileHandler('app.log')
log_smtp_handler = TlsSMTPHandler(("smtp-relay.gmail.com", 587), sender_email, receipent_email, 'IBG Logger Notification :(')

log_console_handler.setLevel(logging.INFO)
log_file_handler.setLevel(logging.WARNING)
log_smtp_handler.setLevel(logging.CRITICAL)

log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

log_console_handler.setFormatter(log_formatter)
log_file_handler.setFormatter(log_formatter)
log_smtp_handler.setFormatter(log_formatter)

logger.addHandler(log_console_handler)
logger.addHandler(log_file_handler)
logger.addHandler(log_smtp_handler)

#Sample Usage

#import IBG_Logger

#IBG_Logger.logger.info("This is an info log. This should be only on console")
#IBG_Logger.logger.warning("This is an warning log. This should be both in the log file and console")
#IBG_Logger.logger.error("This is a error log. This should be both in the log file and console")
#IBG_Logger.logger.critical("This is a critical log. This should be both on the console, in the log file and also in the email")
