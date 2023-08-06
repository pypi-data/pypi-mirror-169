import pytest
from ngtextpreprocess.text_processing import *


# testing clean_html


@pytest.mark.parametrize("text, result", [
    ("<p>", ""),
    ("</p>", ""),
    ("<a href=#>", ""),
    ("<div class='test' ></div>", ""),
    ("&amp;<div class='test' ></div>", "and"),
    ("<div class='test' ></div>&nbsp;", ""),
    ("<div class='test' ></div>&ensp;<div class='test' ></div>", ""),
    ("&emsp;<div class='test' ></div>&emsp;", ""),
])
def test_clean_html(text, result):
    assert clean_html(text) == result

# testing remove_name


@pytest.mark.parametrize("text, result", [
    ("George started his business", "  started his business"),
    ("Jason  and Thomas manages 3 ", " and   manages 3 "),
    ("managed by Michael", "managed by  ")
])
def test_remove_name(text, result):
    assert remove_name(text) == result

# testing remove_address


@pytest.mark.parametrize("text, result", [
    ("5th Street", ""),
    ("Mumbai, India", ", "),
    ("1st Floor, SKMS Buildings, Mumbai, Maharashtra", ", , "),
    ("1st Floor, SKMS Buildings, Mumbai, Maharashtra 400001.", ", , ."),
])
def test_remove_address(text, result):
    assert remove_address(text) == result

# testing fix_encoding_decoding_errors


@pytest.mark.parametrize("text, result", [
     ("â€”", ""),
     ("â€™", ""),
     ("â€œ", ""),
     ("€™", ""),
     ("â", ""),
     ("€œ", "")
])
def test_fix_encoding_decoding_errors(text, result):
    assert fix_encoding_decoding_errors(text) == result

# testing remove_bullets


@pytest.mark.parametrize("text, result", [
    ("*", ""),
    ("* This", " This"),
    ("-", ""),
    ("- This", " This")
])
def test_remove_bullets(text, result):
    assert remove_bullets(text) == result

# testing remove_url


@pytest.mark.parametrize("text, result", [
    ("www.google.com", ""),
    ("https://google.com", ""),
    ("http://google.com", ""),
    ("http://www.google.com", ""),
    ("https://www.google.com", "")
])
def test_remove_url(text, result):
    assert remove_url(text) == result

# testing replace_hexcodes


@pytest.mark.parametrize("text, result", [
    ("\x0A", "\n"),
    ("\x09", "\t"),
    ("\x33", "3"),
    ("\x3d", "="),
    ("\x4a", "J"),
    ("\x67", "g"),
    ("\x7c", "|")
])
def test_replace_hexcodes(text, result):
    assert replace_hexcodes(text) == result

# testing remove_contact_number


@pytest.mark.parametrize("text, result", [
    ("2124567890", ""),
    ("212-456-7890", ""),
    ("(212)456-7890", ""),
    ("(212)-456-7890", ""),
    ("212.456.7890", ""),
    ("212 456 7890", ""),
    ("+12124567890", ""),
    ("+1 212.456.7890", ""),
    ("+212-456-7890", ""),
    ("1-212-456-7890", "")
])
def test_remove_contact_number(text, result):
    assert remove_contact_number(text) == result

# testing clean_email_data


@pytest.mark.parametrize("text, result", [
    ("john001_doe002@ngoogle.com", ""),
    ("johndoe003@ngoogle.co.in", ""),
    ("john004.doe005@ngoogle.com", "")
])
def test_clean_email_data(text, result):
    assert clean_email_data(text) == result

# testing clean_socialmedia_tags


@pytest.mark.parametrize("text, result", [
    ("@john007", ""),
    (" @john007", ""),
    ("#john007", ""),
    (" #john007", "")
])
def test_clean_socialmedia_tags(text, result):
    assert clean_socialmedia_tags(text) == result

# testing expand_domain_specific_shortforms


@pytest.mark.parametrize("text, result", [
    ("ar/ap", "accounts-receivable/accounts-payable"),
    ("ai", "artificial-intelligence"),
    ("bk/reconciliation", "bookkeeping/reconciliation"),
    ("d2c", "direct-to-consumer"),
    ("erp", "enterprise-resource-planning"),
    ("pr", "prorated-revenue"),
    ("fcbk", "full-charge-book-keeping"),
    ("ap/ar", "accounts-payable/accounts-receivable"),
    ("A/P", "accounts-payable"),
    ("ar", "accounts-receivable"),
    ("a/r", "accounts-receivable"),
    ("a\\r", "accounts-receivable"),
    ("a-r", "accounts-receivable"),
    ("ap", "accounts-payable"),
    ("a/p", "accounts-payable"),
    ("a\\p", "accounts-payable"),
    ("a-p", "accounts-payable"),
    ("qbs", "quickbooks"),
    ("qb", "quickbooks"),
    ("qb-o", "quickbooks-online"),
    ("qb/o", "quickbooks-online"),
    ("qbo", "quickbooks-online"),
    ("ma", "mergers-and-acquisitions"),
    ("m&a", "mergers-and-acquisitions"),
    ("fpa", "financial-planning-and-analysis"),
    ("fp&a", "financial-planning-and-analysis"),
    ("fp", "financial-planning"),
    ("advisory/fp", "advisory/financial-planning"),
    ("vc", "venture-capital"),
    ("gl", "general-ledger"),
    ("bk", "bookkeeper"),
    ("p&l", "profit-and-loss"),
    ("p-l", "profit-and-loss"),
    ("cpa", "certified-public-accountant"),
    ("cpa/accounting", "certified-public accountant/accounting"),
    ("coa", "chart-of-accounts"),
    ("cfo", "chief-financial-officer"),
    ("cma", "certified-management-accountant"),
    ("m2m", "mark-to-market"),
    ("mcm", "master-content-management"),
    ("dba", "doing-business-as"),
    ("tx", "tax"),
    ("llc", "limited-liability-company"),
    ("llcs", "limited-liability-companies"),
    ("ppp", "paycheck-protection-program"),
    ("opp", "oppurtunity"),
    ("qbs", "quickbooks"),
    ("p+l", "profit-and-loss")
])
def test_expand_domain_specific_shortforms(text, result):
    assert expand_domain_specific_shortforms(text) == result

# testing expand_general_shortforms


@pytest.mark.parametrize("text, result", [
    ("FTEs", "Full-time-equivalents")
])
def test_expand_general_shortforms(text, result):
    assert expand_general_shortforms(text) == result

# testing fix_contractions


@pytest.mark.parametrize("text, result", [
    ("aren't", "are not"),
    ("you're awesome", "you are awesome"),
    ("he's good", "he is good"),
    ("she'd do that", "she would do that"),
    ("he'll get it", "he will get it"),
    ("he could've done that", "he could have done that"),
    ("I'm good", "I am good")
])
def test_fix_contractions(text, result):
    assert fix_contractions(text) == result

# testing remove_symbols_emojis


@pytest.mark.parametrize("text, result", [
    ("✌😎📚🎈🎄🎁🎭📕📃", ""),
    ("☮✝☪☦🛐🕎♋♓㊗🈴🉐❌🚳", "")

])
def test_remove_symbols_emojis(text, result):
    assert remove_symbols_emojis(text) == result

# testing replace_punctuations


@pytest.mark.parametrize("text, result", [
    ("99-101", "99 101"),
    ("191 - 200", "191     200"),
    ("yes - no", "yes     no"),
    ("-December", " December"),
    ("//", "  "),
    ("/////", "     "),
    ("/january", " january"),
    ("march/", "march "),
    ("\" ", "  "),
    ("clean! Statements!", "clean  Statements "),
    (" * + clean,  ,state .  ,  State", "     clean    state      State"),
    (" /state clean/ :state : State", "  state clean  state  State"),
    (";clean ; < > ?state =  State >", " clean        state    State  "),
    ("clean # @ [ ] Statements", "clean         Statements"),
    ("clean \\ ^ _ - Statements", "clean           Statements"),
    ("clean {  |  ~state  `  ~ } ", "clean        state         ")
])
def test_replace_punctuations(text, result):
    assert replace_punctuations(text) == result

# testing remove_extra_spaces


@pytest.mark.parametrize("text, result", [
    ("import   and     export", "import and export"),
    ("   annual    report   ", " annual report ")
])
def test_remove_extra_spaces(text, result):
    assert remove_extra_spaces(text) == result

# testing fix_spelling


@pytest.mark.parametrize("text, result", [
    ("busness", "business")
])
def test_fix_spelling(text, result):
    assert fix_spelling(text) == result
