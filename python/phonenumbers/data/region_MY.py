"""Auto-generated file, do not edit by hand. MY metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_MY = PhoneMetadata(id='MY', country_code=60, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[13-9]\\d{7,9}', possible_length=(8, 9, 10), possible_length_local_only=(6, 7)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:3[2-9]\\d|[4-9][2-9])\\d{6}', example_number='323456789', possible_length=(8, 9), possible_length_local_only=(6, 7)),
    mobile=PhoneNumberDesc(national_number_pattern='1(?:1[1-5]\\d{2}|[02-4679][2-9]\\d|59\\d{2}|8(?:1[23]|[2-9]\\d))\\d{5}', example_number='123456789', possible_length=(9, 10)),
    toll_free=PhoneNumberDesc(national_number_pattern='1[378]00\\d{6}', example_number='1300123456', possible_length=(10,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='1600\\d{6}', example_number='1600123456', possible_length=(10,)),
    voip=PhoneNumberDesc(national_number_pattern='154\\d{7}', example_number='1541234567', possible_length=(10,)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='([4-79])(\\d{3})(\\d{4})', format='\\1-\\2 \\3', leading_digits_pattern=['[4-79]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(3)(\\d{4})(\\d{4})', format='\\1-\\2 \\3', leading_digits_pattern=['3'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([18]\\d)(\\d{3})(\\d{3,4})', format='\\1-\\2 \\3', leading_digits_pattern=['1[02-46-9][1-9]|8'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(1)([36-8]00)(\\d{2})(\\d{4})', format='\\1-\\2-\\3-\\4', leading_digits_pattern=['1[36-8]0']),
        NumberFormat(pattern='(11)(\\d{4})(\\d{4})', format='\\1-\\2 \\3', leading_digits_pattern=['11'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(15[49])(\\d{3})(\\d{4})', format='\\1-\\2 \\3', leading_digits_pattern=['15'], national_prefix_formatting_rule='0\\1')],
    mobile_number_portable_region=True)
