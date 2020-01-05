from .. import Provider as AutomotiveProvider


class Provider(AutomotiveProvider):
    # Currently this is my own work
    license_formats = (
        '? ### ??',
        '? ### ???',
        '?? ### ??',
        '?? ### ???',
        '? #### ??',
        '? #### ???',
        '?? #### ??',
        '?? #### ???',
    )
