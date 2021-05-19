import re
from pdfminer.high_level import extract_text
import spacy
from spacy.matcher import Matcher
from spacy_langdetect import LanguageDetector
from spacy.language import Language
import pandas as pd

import difflib

nlp = spacy.load('en_core_web_md')
matcher = Matcher(nlp.vocab)


def create_lang_detector(nlp, name):
    return LanguageDetector()


Language.factory("language_detector", func=create_lang_detector)
nlp.add_pipe("language_detector", last=True)


def text_from_pdf(pdf_file):
    return extract_text(pdf_file)


def extract_names(text):
    doc = nlp(text)

    if doc._.language['language'] == 'en':
        nlp_new = spacy.load('en_core_web_md')
    else:
        nlp_new = spacy.load('pl_core_news_md')

    nlp_text = nlp_new(text)

    pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]
    matcher.add('NAME', [pattern])
    matches = matcher(nlp_text)

    for match_id, start, end in matches:
        span = nlp_text[start:end]
        return span.text


def extract_phone_number(text):
    phone = re.findall(re.compile(
        r'(?:(?:\+?([1-9]|[0-9][0-9]|[0-9][0-9][0-9])\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8]['
        r'02-9])\s*\)|([0-9][1-9]|[0-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9]['
        r'02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?'),
        text)

    if phone:
        number = ''.join(phone[0])
        if len(number) > 10:
            return '+' + number
        else:
            return number


def extract_email(text):
    email = re.findall("([^@|\s]+@[^@]+\.[^@|\s]+)", text)
    if email:
        try:
            return email[0].split()[0].strip(';')
        except IndexError:
            return None


def extract_skills(text):
    doc = nlp(text)
    tokens = [token.text for token in doc if not token.is_stop]
    data = pd.read_csv("skills_example.csv", sep=';')
    skills = list(data.columns.values)

    for i in range(len(skills)):
        skills[i] = skills[i].lower()

    skill_set = []
    for token in tokens:
        if token.lower() in skills:
            skill_set.append(token)

    for i in range(0, len(tokens)):
        pom_token = ''
        if i < len(tokens) - 3:
            for j in range(i, i + 3):
                if pom_token != '':
                    pom_token = pom_token + ' ' + tokens[j]
                else:
                    pom_token = tokens[j]
                if pom_token.lower() in skills:
                    skill_set.append(pom_token)
                    skills.remove(pom_token.lower())
                    pom_token = ''

                for s in skills:
                    clean_token = ''.join(e for e in pom_token.lower() if (e.isalnum()))
                    seq = difflib.SequenceMatcher(None, clean_token, s.lower())
                    d = seq.ratio()
                    if (d > 0.85) & (s not in skill_set):
                        skill_set.append(s)

    return [i.capitalize() for i in set([i.lower() for i in skill_set])]


def extract_from_CV(CV_dokumnet):
    CV_text = text_from_pdf(CV_dokumnet)
    names = extract_names(CV_text)
    name = names.split()[0]
    surname = names.split()[1]
    phone = extract_phone_number(CV_text)
    mail = extract_email(CV_text)
    return [name, surname, phone, mail]