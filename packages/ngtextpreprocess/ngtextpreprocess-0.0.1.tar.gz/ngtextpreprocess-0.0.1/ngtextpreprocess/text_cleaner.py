from ngtextpreprocess.text_processing import *
from ngtextpreprocess.make_directory import MakeDirectory
import logging


class CleanText:
    """This class is used as a text cleaning pipeline.
        The cleaning pipeline method within this class uses
        all the functions within the text_processing module
        to give the final cleaned output text.
    """

    def __init__(self, input_text):
        self.input_text = input_text

    def cleaning_pipeline(self,keep_logging=False,keep_clean_html=True,
    keep_expand_domain=True,keep_expand_general=True,keep_remove_name=True,
    keep_remove_address=True,keep_fix_encode_error=True,keep_remove_bullets=True,
    keep_remove_url=True,keep_replace_hexcodes=True,keep_remove_contact=True,
    keep_clean_email=True,keep_clean_socialmedia=True,keep_fix_contractions=True,
    keep_remove_symbols=True,keep_replace_punctuations=True,keep_remove_extraspace=True,
    keep_fix_spelling=True
    ):
        """This method performs multiple text cleaning operations
            and returns the cleaned output text.

            :param self: Inherited from class attributes

            :param keep_logging: To enable logging
            :type keep_logging: bool

            :param keep_clean_html: To enable clean_html
            :type keep_clean_html: bool

            :param keep_expand_domain: To enable expand_domain_specific_shortforms
            :type keep_expand_domain: bool

            :param keep_expand_general: To enable expand_general_shortforms
            :type keep_expand_general: bool

            :param keep_remove_name: To enable remove_name
            :type keep_remove_name: bool

            :param keep_remove_address: To enable remove_address
            :type keep_remove_address: bool

            :param keep_fix_encode_error: To enable fix_encode_decode_error
            :type keep_fix_encode_error: bool

            :param keep_remove_bullets: To enable remove_bullets
            :type keep_remove_bullets: bool

            :param keep_remove_url: To enable remove_url
            :type keep_remove_url: bool

            :param keep_replace_hexcodes: To enable replace_hexcodes
            :type keep_replace_hexcodes: bool

            :param keep_remove_contact: To enable remove_contact
            :type keep_remove_contact: bool

            :param keep_clean_email_data: To enable clean_email_data
            :type keep_clean_email_data: bool

            :param keep_socialmedia: To enable clean_socialmedia_tags
            :type keep_socialmedia: bool

            :param keep_fix_contractions: To enable fix_contractions
            :type keep_fix_contractions: bool

            :param keep_remove_symbols: To enable remove_symbols_emojis
            :type keep_remove_symbols: bool

            :param keep_replace_punctuations: To enable keep_replace_punctuations
            :type keep_replace_punctuations: bool

            :param keep_remove_extraspace: To enable remove_extra_spaces
            :type keep_remove_extraspace: bool

            :param keep_fix_spelling: To enable fix_spelling
            :type keep_fix_spelling: bool
            
            :return: Cleaned output text
            :rtype: str
        """
        processed_text = self.input_text

        # <<< With Logging >>>

        if keep_logging:
            # Creating logging file and instantiating logger
            md = MakeDirectory(
                dir_structure=generate_directory['dir_structure'],
                basefolder=generate_directory['basefolder'],
                file_start=generate_directory['file_start'])

            logfile_name = md.create_logging_file()

            logging.basicConfig(format='%(asctime)s : %(message)s',
                                filename=logfile_name,
                                level=logging.INFO)

            app_logger = logging.getLogger()

            app_logger.info("<< Initializing TEXT CLEANING >>")
            app_logger.info("< Initializing cleaning_pipeline >")

            # cleaning html
            if keep_clean_html:
                try:
                    app_logger.info("Cleaning html")
                    processed_text = clean_html(processed_text)
                    app_logger.info("Successfully cleaned html")
                except Exception:
                    app_logger.exception("Failed at cleaning html")
                    raise Exception()

            # Expanding domain specific short-forms.
            if keep_expand_domain:
                try:
                    app_logger.info("Expanding domain specific shortforms")
                    processed_text = expand_domain_specific_shortforms(
                        processed_text)
                    app_logger.info(
                        "Successfully expanded domain specific shortforms")
                except Exception:
                    app_logger.exception("Failed at \
                        expanding domain specific shortforms")
                    raise Exception()

            # expanding general shortforms
            if keep_expand_general:
                try:
                    app_logger.info("Expanding general shortforms")
                    processed_text = expand_general_shortforms(processed_text)
                    app_logger.info("Successfully expanded general shortforms")
                except Exception:
                    app_logger.exception("Failed at \
                        expanding general shortforms")
                    raise Exception()

            # removing personal names
            if keep_remove_name:
                try:
                    app_logger.info("Removing personal names")
                    processed_text = remove_name(processed_text)
                    app_logger.info("Successfully removed personal names")
                except Exception:
                    app_logger.exception("Failed at removing personal names")
                    raise Exception()

            # removing addresses
            if keep_remove_address:
                try:
                    app_logger.info("Removing addresses")
                    processed_text = remove_address(processed_text)
                    app_logger.info("Successfully removed addresses")
                except Exception:
                    app_logger.exception("Failed at removing addresses")
                    raise Exception()

            # fixing encoding-decoding errors
            if keep_fix_encode_error:
                try:
                    app_logger.info("Fixing encoding-decoding errors")
                    processed_text = fix_encoding_decoding_errors(
                        processed_text)
                    app_logger.info(
                        "Successfully fixed encoding-decoding errors")
                except Exception:
                    app_logger.exception("Failed at \
                        fixing encoding-decoding errors")
                    raise Exception()

            # removing bullets
            if keep_remove_bullets:
                try:
                    app_logger.info("Removing bullets")
                    processed_text = remove_bullets(processed_text)
                    app_logger.info("Successfully removed bullets")
                except Exception:
                    app_logger.exception("Failed at removing bullets")
                    raise Exception()

            # removing URL
            if keep_remove_url:
                try:
                    app_logger.info("Removing URL's")
                    processed_text = remove_url(processed_text)
                    app_logger.info("Successfully removed URL's")
                except Exception:
                    app_logger.exception("Failed at removing URL's")
                    raise Exception()

            # replacing hexcodes
            if keep_replace_hexcodes:
                try:
                    app_logger.info("Replacing hexcodes")
                    processed_text = replace_hexcodes(processed_text)
                    app_logger.info("Successfully replaced hexcodes")
                except Exception:
                    app_logger.exception("Failed at replacing hexcodes")
                    raise Exception()

            # removing contact number
            if keep_remove_contact:
                try:
                    app_logger.info("Removing contact number")
                    processed_text = remove_contact_number(processed_text)
                    app_logger.info("Successfully removed contact number")
                except Exception:
                    app_logger.exception("Failed at removing contact number")
                    raise Exception()

            # cleaning email id
            if keep_clean_email:
                try:
                    app_logger.info("Cleaning email id")
                    processed_text = clean_email_data(processed_text)
                    app_logger.info("Successfully cleaned email data")
                except Exception:
                    app_logger.exception("Failed at cleaning email data")
                    raise Exception()

            # cleaning social-media tags
            if keep_clean_socialmedia:
                try:
                    app_logger.info("Cleaning social media tags")
                    processed_text = clean_socialmedia_tags(processed_text)
                    app_logger.info("Successfully cleaned social media tags")
                except Exception:
                    app_logger.exception("Failed at \
                        cleaning social media tags")
                    raise Exception()

            # fixing contractions
            if keep_fix_contractions:
                try:
                    app_logger.info("Fixing contractions")
                    processed_text = fix_contractions(processed_text)
                    app_logger.info("Successfully fixed contractions")
                except Exception:
                    app_logger.exception("Failed at fixing contractions")
                    raise Exception()

            # removing symbols and emojis
            if keep_remove_symbols:
                try:
                    app_logger.info("Removing symbols and emojis")
                    processed_text = remove_symbols_emojis(processed_text)
                    app_logger.info("Successfully removed symbols and emojis")
                except Exception:
                    app_logger.exception("Failed at \
                        removing symbols and emojis")
                    raise Exception()

            # replacing punctuations
            if keep_replace_punctuations:
                try:
                    app_logger.info("Replacing punctuations")
                    processed_text = replace_punctuations(processed_text)
                    app_logger.info("Successfully replaced punctuations")
                except Exception:
                    app_logger.exception("Failed at replacing punctuations")
                    raise Exception()

            # removing extra spaces
            if keep_remove_extraspace:
                try:
                    app_logger.info("Removing extra spaces")
                    processed_text = remove_extra_spaces(processed_text)
                    app_logger.info("Successfully removed extra spaces")
                except Exception:
                    app_logger.exception("Failed at removing extra spaces")
                    raise Exception()

            # fixing spelling errors
            if keep_fix_spelling:
                try:
                    app_logger.info("Fixing spelling errors")
                    final_text = fix_spelling(processed_text)
                    app_logger.info("Successfully fixed spelling errors")
                except Exception:
                    app_logger.exception("Failed at fixing spelling errors")
                    raise Exception()

            app_logger.info("< Closing cleaning_pipeline >")
            app_logger.info("<< TEXT CLEANING SUCCESSFULLY COMPLETED >>")

        # <<< Without Logging >>>
        else:
            # cleaning html
            if keep_clean_html:
                try:
                    processed_text = clean_html(processed_text)
                except Exception:
                    raise Exception()

            # expanding domain specific short-forms
            if keep_expand_domain:
                try:
                    processed_text = expand_domain_specific_shortforms(
                        processed_text)
                except Exception:
                    raise Exception()

            # expanding general shortforms
            if keep_expand_general:
                try:
                    processed_text = expand_general_shortforms(processed_text)
                except Exception:
                    raise Exception()

            # removing personal names
            if keep_remove_name:
                try:
                    processed_text = remove_name(processed_text)
                except Exception:
                    raise Exception()

            # removing addresses
            if keep_remove_address:
                try:
                    processed_text = remove_address(processed_text)
                except Exception:
                    raise Exception()

            # fixing encoding-decoding errors
            if keep_fix_encode_error:
                try:
                    processed_text = fix_encoding_decoding_errors(
                        processed_text)
                except Exception:
                    raise Exception()

            # removing bullets
            if keep_remove_bullets:
                try:
                    processed_text = remove_bullets(processed_text)
                except Exception:
                    raise Exception()

            # removing URL
            if keep_remove_url:
                try:
                    processed_text = remove_url(processed_text)
                except Exception:
                    raise Exception()

            # replacing hexcodes
            if keep_replace_hexcodes:
                try:
                    processed_text = replace_hexcodes(processed_text)
                except Exception:
                    raise Exception()

            # removing contact number
            if keep_remove_contact:
                try:
                    processed_text = remove_contact_number(processed_text)
                except Exception:
                    raise Exception()

            # cleaning email id
            if keep_clean_email:
                try:
                    processed_text = clean_email_data(processed_text)
                except Exception:
                    raise Exception()

            # cleaning social-media tags
            if keep_clean_socialmedia:
                try:
                    processed_text = clean_socialmedia_tags(processed_text)
                except Exception:
                    raise Exception()

            # fixing contractions
            if keep_fix_contractions:
                try:
                    processed_text = fix_contractions(processed_text)
                except Exception:
                    raise Exception()

            # removing symbols and emojis
            if keep_remove_symbols:
                try:
                    processed_text = remove_symbols_emojis(processed_text)
                except Exception:
                    raise Exception()

            # replacing punctuations
            if keep_replace_punctuations:
                try:
                    processed_text = replace_punctuations(processed_text)
                except Exception:
                    raise Exception()

            # removing extra spaces
            if keep_remove_extraspace:
                try:
                    processed_text = remove_extra_spaces(processed_text)
                except Exception:
                    raise Exception()

            # fixing spelling errors
            if keep_fix_spelling:
                try:
                    final_text = fix_spelling(processed_text)
                except Exception:
                    if keep_fix_spelling:
                        raise Exception()

        return final_text
