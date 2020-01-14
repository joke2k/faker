from .. import Provider as AutomotiveProvider


class Provider(AutomotiveProvider):
    # from
    # https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Poland
    license_formats = (
        '?? #####',
        '?? ####?',
        '?? ###??',
        '?? #?###',
        '?? #??##',
        '??? ?###',
        '??? ##??',
        '??? #?##',
        '??? ##?#',
        '??? #??#',
        '??? ??##',
        '??? #####',
        '??? ####?',
        '??? ###??',
    )

    def license_plate_regex_formats(self):
        return [plate.replace('?', '[A-Z]').replace('#', '[0-9]') for plate in self.license_formats]
