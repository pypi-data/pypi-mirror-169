import re
import os
import sys
import spacy

# These patterns are used for replacing the unwanted patterns
# from the given text input.
common_patterns = {
    'pattern_1': '.',
    'pattern_2': ' ',
    'pattern_3': '',
    'pattern_4': '\'',
    'pattern_5': 'and'
}

# These patterns are used for removing HTML tags and attributes.
html_patterns = {
    'pattern_1': r'<.*?>',
    'pattern_2': r'(&nbsp;|&ensp;|&emsp;|&gt;)',
    'pattern_3': r'&amp;'
}

# This variable contains the name of the Spacy trained model that is 
# used for Named Entity Recognition tasks within the individual functions.
SPACY_LARGE_MODEL = "en_core_web_lg"

# SpaCy model installation package location
SYS_LOC = os.path.dirname(sys.executable)
FINAL_LOC = str(SYS_LOC).replace("Scripts","Lib")+"\\site-packages\\en_core_web_lg"

# Downloading SpaCy model
if not os.path.exists(FINAL_LOC):
    spacy.cli.download(SPACY_LARGE_MODEL)
    
# Spacy nlp object for NER tasks
nlp = spacy.load(SPACY_LARGE_MODEL)

# This list consists of Named Entity Recognition tags used within the 
# individual functions.
spacy_NER_tags = ['PERSON', 'NORP', 'FAC', 'ORG', 'GPE', 'LOC', 'ORDINAL']

# This variable contains the pattern that is used for removing postal codes 
# from the given text input.
us_postal_code_pattern = r'(?<=[\w\s])\d{6}(?=\.?\n)'

# This dictionary contains the parameters and patterns that are required for
# fixing ASCII encoding decoding errors.
encode_decode_vars = {
    "encode_type": 'ascii',
    "error_type": 'replace',
    "decode_type": 'ascii',
    "pattern_1": r'\?+',
    "pattern_2": r'\s+',
}

# This variable contains the pattern for removing bullets from the given text input.
bullet_pattern = r'^\*|^-'

# This variable contains the pattern for removing URL from the given text input.
url_pattern = r'((http|https):/+\S+)|(www\.\S+\.\S{2,9})'

# This variable contains the pattern for removing bullets from the given text input.
hexcode_pattern = r'[^\x00-\x7f]'

# This variable contains the pattern for removing escape sequences from the given text input.
escape_seq_pattern = r'\\[a-z]'

# This variable contains the pattern for removing contact numbers from the given text input.
contact_numb_pattern = r'\+?\d?[\s-]?\(?\d{3}\)?[\.\s-]?\d{3}[\.\s-]?\d{4}'

# This variable contains the pattern for removing email id from the given text input.
email_data_pattern = r'\S*@\S*\s?'

# This variable contains the pattern for removing social-media tags from the given text input.
socialmedia_pattern = r'\s?(@|#)\S+'

# This dictionary contains the patterns for removing specific contractions from the given text input.
contraction_patterns = {
    'pattern_1': r'n\'t',
    'pattern_2': r'\'re',
    'pattern_3': r'\'s',
    'pattern_4': r'\'d',
    'pattern_5': r'\'ll',
    'pattern_6': r'\'t',
    'pattern_7': r'\'ve',
    'pattern_8': r'\'m'
}

# This list contains the expanded form of certain contractions.
expanded_contractions = [' not', ' are', ' is',
                         ' would', ' will', ' not', ' have', ' am']

# This list contains the unicode for various symbols and emojis from the given text input.
emojis = "["\
    u"\U0001F600-\U0001F64F"\
    u"\U0001F300-\U0001F5FF"\
    u"\U0001F680-\U0001F6FF"\
    u"\U0001F1E0-\U0001F1FF"\
    u"\U00002500-\U00002BEF"\
    u"\U00002702-\U000027B0"\
    u"\U00002702-\U000027B0"\
    u"\U000024C2-\U0001F251"\
    u"\U0001f926-\U0001f937"\
    u"\U00010000-\U0010ffff"\
    u"\u2640-\u2642"\
    u"\u2600-\u2B55"\
    u"\u200d"\
    u"\u23cf"\
    u"\u23e9"\
    u"\u231a"\
    u"\ufe0f"\
    u"\u3030"\
    "]+"

# The following two variables contain the parameters for compiling the pattern to remove emojis and symbols.
emoji_flag = re.UNICODE  # for compiling the regex pattern.
emoji_rstring = r''  # for creating r-string out of the given text input.

# This dictionary contains the patterns for removing punctuations and preserving certain specific
# patterns like date, dollars, fullstops etc from the text input.
punct_patterns = {
    'pattern_1': r'(?<![\d\w])-(?![\d\w])',
    'pattern_2': r'-(?=\w)',
    'pattern_3': r'((?<!\d)/)',
    'pattern_4': r'(?<![\d\.,])\%',
    'pattern_5': r'\$(?!\d+)',
    'pattern_6': r'(?<![\w])\.|(?<![\w])\:',
    'pattern_7': r'\((?![\w])|(?<![\w])\)'
}

# This list contains the punctuations to be removed.
punct_list = [
    '!', '"', '#', '&', "'", '*', '+', ',',
    ':', ';', '<', '=', '>', '?', '@',
    '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~',
]

# This variable contains the pattern for removing adjacent additional whitespaces.
extra_spaces = r'\s{2,}'

# This dictionary consists of the parameters for defining the Log folder structure.
generate_directory = {
    "dir_structure": None,
    "basefolder": "logfiles",
    "file_start": "text_cleaner"
}

# This variable is used for getting the current working directory path.
curr_directory = os.getcwd()
