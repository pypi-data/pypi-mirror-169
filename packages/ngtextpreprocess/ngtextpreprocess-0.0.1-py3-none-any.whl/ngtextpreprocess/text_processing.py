import contractions
from autocorrect import Speller
from ngtextpreprocess.replacement_dictionary import *
from ngtextpreprocess.global_params import *


"""This module consists of individual functions that can be used
    for processing the raw text input.
"""


def clean_html(text_doc):
    """This function removes all the HTML tags, attributes
        and HTML indendations from the given text input.

        :param text_doc: Input text document
        :type text_doc: str
        :return: Text document without HTML tags,
            attributes and indendations
        :rtype: str
    """
    # handling html tags
    text_doc = re.sub(
        html_patterns['pattern_1'],
        common_patterns['pattern_3'], text_doc)

    # handling indendations
    text_doc = re.sub(
        html_patterns['pattern_2'],
        common_patterns['pattern_3'], text_doc)

    # replacing ampersand
    text_doc = text_doc.replace(
        html_patterns['pattern_3'],
        common_patterns['pattern_5'])
    return text_doc


def remove_name(text_doc):
    """This function removes personal names from the given
        text input using Named Entity Recognition technique.

        This function uses Spacy library and 'en_core_web_lg' model
        for performing Named Entity Recognition.

        :param text_doc: Input text document
        :type text_doc: str
        :return: Text document without personal names
        :rtype: str
    """
    # getting document entities for identifying 'PERSON'
    doc = nlp(text_doc)
    doc_ents = [(ent.text, ent.label_) for ent in doc.ents]

    # obtaining all words of 'PERSON' tag for removal
    replace_text = []

    for item in doc_ents:
        if item[1] == spacy_NER_tags[0]:
            replace_text.append(item[0])

    for i in replace_text:
        text_doc = text_doc.replace(
            i, common_patterns['pattern_2'])
    return text_doc


def remove_address(text_doc):
    """ This function removes contact addresses from the given
        text input using Named Entity Recognition technique.

        This function uses Spacy library and 'en_core_web_lg' model
        for performing Named Entity Recognition.

        :param text_doc: Input text document
        :type text_doc: str
        :return: Text document without addresses including
            location number, location name, geographical name
            and postal codes
        :rtype: str
    """
    # getting document entities for identifying addresses
    doc = nlp(text_doc)
    doc_ents = [(ent.text, ent.label_) for ent in doc.ents]

    replace_text = []
    location_ents = spacy_NER_tags[1:6]

    # replacing US postalcodes
    text_doc = re.sub(
        us_postal_code_pattern,
        common_patterns['pattern_3'], text_doc)

    # removing locations
    for item in doc_ents:
        if item[1] in location_ents:
            replace_text.append(item[0])

    # removing ordinal numbers linked to locations. eg: 5th in 5th street
    for i in range(len(doc_ents)):
        if (doc_ents[i][1] in location_ents and
                doc_ents[i-1][1] == spacy_NER_tags[6]):
            replace_text.append(doc_ents[i-1][0])

    for item in replace_text:
        text_doc = text_doc.replace(
            item, common_patterns['pattern_3'])
    return text_doc


def fix_encoding_decoding_errors(text_doc):
    """This function removes the errors arising due to
        ASCII encoding and decoding conversion processes.

        This function uses Python Contractions library for
        fixing general English contraction words.

        :param text_doc: Input text document
        :type text_doc: str
        :return: Text document without ASCII symbols.
        :rtype: str
    """
    decoded_text = text_doc.encode(
        'ascii', errors='replace').decode('ascii')

    # replacing error terms with apostrophes
    processed_text = re.sub(
        encode_decode_vars['pattern_1'],
        common_patterns['pattern_4'], decoded_text)

    # removing all apostrophes
    processed_text = re.sub(
        common_patterns['pattern_4'],
        common_patterns['pattern_3'], processed_text)
    text_doc = contractions.fix(processed_text)

    # replacing multiple whitespaces with a single space
    text_doc = re.sub(
        encode_decode_vars['pattern_2'],
        common_patterns['pattern_2'], text_doc)
    return text_doc


def remove_bullets(text_doc):
    """This function removes bullets from the given
        input text.

        :param text_doc: Input text document
        :type text_doc: str
        :return: Text document without ASCII symbols.
        :rtype: str
    """
    text_doc = re.sub(
        bullet_pattern,
        common_patterns['pattern_3'], text_doc)
    return text_doc


def remove_url(text_doc):
    """This function removes any URL data including
        the ones starting with or a a combination of
        http, https and www

        :param text_doc: Input text document
        :type text_doc: str
        :return: Text document without URLs
        :rtype: str
    """
    text_doc = re.sub(url_pattern,
                      common_patterns['pattern_3'], text_doc)
    return text_doc


def replace_hexcodes(text_doc):
    """This function replaces hexcodes to readable
        text characters or whitespaces.

        :param text_doc: Input text document
        :type text_doc: str
        :return: Text document without hexcodes
        :rtype: str
    """
    # removing hexcodes
    text_doc = re.sub(
        hexcode_pattern,
        common_patterns['pattern_3'], text_doc)

    # replacing escape sequences with whitespace
    text_doc = re.sub(
        escape_seq_pattern,
        common_patterns['pattern_2'], text_doc)
    return text_doc


def remove_contact_number(text_doc):
    """This function removes (US based format) contact numbers
        including landline and mobile numbers.

        :param text_doc: Input text document
        :type text_doc: str
        :return: Text document without contact numbers
        :rtype: str
    """
    text_doc = re.sub(
        contact_numb_pattern,
        common_patterns['pattern_3'], text_doc)
    return text_doc


def clean_email_data(text_doc):
    """This function removes e-mail id's from the given
        text input.

        :param text_doc: Input text document
        :type text_doc: str
        :return: Text document without e-mail id's
        :rtype: str
    """
    text_doc = re.sub(
        email_data_pattern,
        common_patterns['pattern_3'], text_doc)
    return text_doc


def clean_socialmedia_tags(text_doc):
    """This function removes mentions and hashtags
        from the given text input.

        :param text_doc: Input text document
        :type text_doc: str
        :return: Text document without mentions and hashtags
        :rtype: str
    """
    text_doc = re.sub(socialmedia_pattern,
                      common_patterns['pattern_3'], text_doc)
    return text_doc


def expand_domain_specific_shortforms(text_doc):
    """This function expands domain specific short form words
        from the given text input.

        :param text_doc: Input text document
        :type text_doc: str
        :return: Text document with expanded shortforms.
        :rtype: str
    """
    replace_dict = financial_replacement_dict

    for i in replace_dict.keys():
        for idx, val in enumerate(text_doc.split()):
            if i == val.lower():
                text_doc = text_doc.replace(
                    text_doc.split()[idx],
                    replace_dict[i])
    return text_doc


def expand_general_shortforms(text_doc):
    """This function expands general short form words
        from the given text input.

        :param text_doc: Input text document
        :type text_doc: str
        :return: Text document with expanded shortforms.
        :rtype: str
    """
    replace_dict = general_replacement_dict

    for i in replace_dict.keys():
        for idx, val in enumerate(text_doc.split()):
            if i == val.lower():
                text_doc = text_doc.replace(
                    text_doc.split()[idx], replace_dict[i])
    return text_doc


def fix_contractions(text_doc):
    """This function expands the English contractions
        to its proper grammatical form.

        :param text_doc: Input text document
        :type text_doc: str
        :return: Text document without contractions.
        :rtype: str
    """
    # replacing n't
    text_doc = re.sub(
        contraction_patterns['pattern_1'],
        expanded_contractions[0], text_doc)

    # replacing 're
    text_doc = re.sub(
        contraction_patterns['pattern_2'],
        expanded_contractions[1], text_doc)

    # replacing 's
    text_doc = re.sub(
        contraction_patterns['pattern_3'],
        expanded_contractions[2], text_doc)

    # replacing 'd
    text_doc = re.sub(
        contraction_patterns['pattern_4'],
        expanded_contractions[3], text_doc)

    # replacing 'll
    text_doc = re.sub(
        contraction_patterns['pattern_5'],
        expanded_contractions[4], text_doc)

    # replacing 't
    text_doc = re.sub(
        contraction_patterns['pattern_6'],
        expanded_contractions[5], text_doc)

    # replacing 've
    text_doc = re.sub(
        contraction_patterns['pattern_7'],
        expanded_contractions[6], text_doc)

    # replacing 'm
    text_doc = re.sub(
        contraction_patterns['pattern_8'],
        expanded_contractions[7], text_doc)
    return text_doc


def remove_symbols_emojis(text_doc):
    """This function removes emojis and other symbols
        in the given text input.

        :param text_doc: Input text document
        :type text_doc: str
        :return: Text document without emojis and symbols
        :rtype: str
    """
    emoji_pattern = re.compile(emojis, flags=emoji_flag)

    text_doc = emoji_pattern.sub(emoji_rstring, text_doc)
    return text_doc


def replace_punctuations(text_doc):
    """This function repaces punctuations with whitespaces.

        :param text_doc: Input text document
        :type text_doc: str
        :return: Text document with punctuations replaced by whitespace
        :rtype: str
    """
    # replacing - other than in between numbers and words
    text_doc = re.sub(
        punct_patterns['pattern_1'],
        common_patterns['pattern_2']*3, text_doc)

    # replacing hyphens followed by first word of a sentence
    text_doc = re.sub(
        punct_patterns['pattern_2'],
        common_patterns['pattern_2'], text_doc)

    # handling /
    text_doc = re.sub(
        punct_patterns['pattern_3'],
        common_patterns['pattern_2'], text_doc)

    # replacing "%" other than numerical percentages
    text_doc = re.sub(
        punct_patterns['pattern_4'],
        common_patterns['pattern_3'], text_doc)

    # replacing $ other than dollar values
    text_doc = re.sub(
        punct_patterns['pattern_5'],
        common_patterns['pattern_3'], text_doc)

    # # replacing . and : other than at word endings
    text_doc = re.sub(
        punct_patterns['pattern_6'],
        common_patterns['pattern_3'], text_doc)

    # # replacing isolated parenthesis
    text_doc = re.sub(
        punct_patterns['pattern_7'],
        common_patterns['pattern_3'], text_doc)

    # replacing from list of punctuations
    for word in text_doc:
        if word in punct_list:
            text_doc = text_doc.replace(
                word, common_patterns['pattern_2'])
    return text_doc


def remove_extra_spaces(text_doc):
    """This function removes additional whitespaces in the
        given text input.

        :param text_doc: Input text document
        :type text_doc: str
        :return: Text document without multiple adjacent whitespaces
        :rtype: str
    """
    text_doc = re.sub(extra_spaces, common_patterns['pattern_2'], text_doc)
    return text_doc


def fix_spelling(text_doc):
    """This function fixes spelling errors from the given text input.
        This function uses Autocorrect library for performing spell check.

        :param text_doc: Input text document
        :type text_doc: str
        :return: Text document without spelling errors
        :rtype: str
    """
    corrected_w = []

    spell = Speller()

    for w in text_doc.split():
        w = spell(w)
        corrected_w.append(w)

    text_doc = ' '.join(corrected_w)
    return text_doc
