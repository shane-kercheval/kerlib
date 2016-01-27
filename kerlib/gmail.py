import smtplib
import logging
import datetime


def send_email(username,
               password,
               subject,
               email_text,
               to_addresses,
               cc_addresses=list(),
               bcc_addresses=list(),
               test=False):
    # Sends a gmail email.
    if len(to_addresses) == 0:
        raise ValueError("'to_addresses' can't be empty.")
    if type(to_addresses) is not list:
        raise TypeError("to_addresses needs to be a list, but is a " +
                        type(to_addresses).__name__)
    if type(cc_addresses) is not list:
        raise TypeError("cc_addresses needs to be a list, but is a " +
                        type(cc_addresses).__name__)
    if type(bcc_addresses) is not list:
        raise TypeError("bcc_addresses needs to be a list, but is a " +
                        type(bcc_addresses).__name__)

    if not test:
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.ehlo()
        session.starttls()
        session.login(username, password)

    if len(cc_addresses) > 0:
        headers = "\n".join(["from: " + username,
                             "subject: " + subject,
                             "to: " + ", ".join(to_addresses),
                             "cc: " + ", ".join(cc_addresses),
                             "mime-version: 1.0",
                             "content-type: text/html"])
    else:
        headers = "\n".join(["from: " + username,
                             "subject: " + subject,
                             "to: " + ", ".join(to_addresses),
                             "mime-version: 1.0",
                             "content-type: text/html"])

    content = headers + "\n" + email_text
    send_to = list()
    send_to.extend(to_addresses)
    send_to.extend(cc_addresses)
    send_to.extend(bcc_addresses)

    logging.info("-----send_email (test={}; time='{}')"
                 .format(test, datetime.datetime.now()))
    logging.info("content: " + content)
    logging.info("sendto: " + ", ".join(send_to))
    logging.info("-----end send_email--------")

    if test:
        return content + "\n" + ", ".join(send_to)
    elif session is not None:
        session.sendmail(username, send_to, content)
        return True
    else:
        raise ValueError("'to_addresses' can't be empty.")
