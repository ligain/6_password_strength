import argparse
import math
import string

from constants import (
    PASSWORD_GRADES,
    SCORE_STEP,
    RESULT_TEMPLATE
)


def calc_possible_symbols(password):
    possible_symbols = 0
    symbols_variants = ['ascii_lowercase', 'ascii_uppercase',
                        'digits', 'punctuation']
    for symbols in symbols_variants:
        has_common_chars = bool(
            set(getattr(string, symbols)) & set(password)
        )
        if has_common_chars:
            possible_symbols += len(getattr(string, symbols))
    return possible_symbols


def get_password_strength(password):
    possible_symbols = calc_possible_symbols(password)
    return len(password) * math.log2(possible_symbols)


def get_password_grade(password_strength, password_grades=None):

    if not password_grades or not password_strength:
        return

    for grade, grade_limit in password_grades:
        if password_strength > grade_limit:
            return grade


def score_password_strength(password_strength,
                            password_grades=None, step=10):

    if not password_grades or not password_strength:
        return

    _, max_score = max(password_grades, key=lambda x: x[1])
    _, min_score = min(password_grades, key=lambda x: x[1])

    if password_strength > max_score:
        return 10

    delta = max_score - min_score

    score = round((step * password_strength) / delta)

    return score


def get_args():
    parser = argparse.ArgumentParser(
        description='Password strength checker'
    )
    parser.add_argument(
        '-p', '--password',
        help='password to analyze',
        type=str,
        required=True
    )
    return parser.parse_args()


if __name__ == '__main__':

    args = get_args()

    password_strength = get_password_strength(
        args.password
    )

    password_grade = get_password_grade(
        password_strength,
        password_grades=PASSWORD_GRADES
    )

    password_score = score_password_strength(
        password_strength,
        password_grades=PASSWORD_GRADES,
        step=SCORE_STEP
    )

    print(
        RESULT_TEMPLATE.format(
            password=args.password,
            password_grade=password_grade,
            password_score=password_score,
            score_step=SCORE_STEP
        )
    )

