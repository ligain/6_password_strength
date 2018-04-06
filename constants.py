PASSWORD_GRADES = (
    ('very strong', 128),
    ('strong', 64),
    ('medium', 56),
    ('weak', 0)
)

SCORE_STEP = 10

RESULT_TEMPLATE = '''
Your password: {password} 
is {password_grade} and has score: {password_score} 
out of {score_step}
'''