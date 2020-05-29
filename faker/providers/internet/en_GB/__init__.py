from .. import Provider as InternetProvider


class Provider(InternetProvider):

    free_email_domains = (
        'gmail.com',
        'yahoo.com',
        'hotmail.com',
        'gmail.co.uk',
        'yahoo.co.uk',
        'hotmail.co.uk',
    )

    tlds = ('com', 'com', 'com', 'com', 'com', 'com', 'biz', 'info', 'net', 'org', 'co.uk')
