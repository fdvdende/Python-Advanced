import re

def query_parser(q):
    q = re.sub(r'"(.+?)"', lambda m: m[1].replace(' ', '_'), q)
    q = re.sub(r'( +)', ' ', q)    # replace multiple spaces with single space
    q = re.sub(r'(\s*(?:,|OR|or|\|)\s*)', '-OR-', q)      # replace comma with
    q = re.sub(r'(\s*(?: |AND|and|\&)\s*)', '-AND-', q)
    q = q.replace('_', ' ')
    keywords = q.split('-OR-')
    keywords = [tuple(keyword.split('-AND-')) if '-AND-' in keyword else keyword for keyword in keywords]
    return keywords

q = 'A or B'
q = 'A | B'
q = 'A, B'  # A or B

q = 'A and B'
q = 'A & B'
q = 'A B'   # A and B

q = '"A B"' # A B

q = 'A and "B C" or D and E'
q = 'A "B C", D E'

q = 'A or "B C" and D or E'
q = 'A, "B C" D, E'

# q = '(A or "B C") and (D or E)'
# q = '(A, "B C")     (D, E)'

query_parser(q)