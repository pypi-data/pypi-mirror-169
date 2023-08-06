import numpy as np

modelmeta = {
    'poly1':
    {
        'engine': 'bol_tail',
        'alias':
        [
            'linear', 'poly1', 'polynomial1',
        ],
        'description': '1 order polynomial',
        'func': 'functions.linear',
        'parname' :
        [
            r'$a$', r'$b$',
        ],
        'par' :
        [
            'a', 'b',
        ],
        'bestv':
        {
            'a' : 1,
            'b' : 0.,                             
        },
        'bounds':
        {
            'a' : [-np.inf, np.inf],
            'b' : [-np.inf, np.inf],                         
        },
    },
    'poly2':
    {
        'engine': 'bol_tail',
        'alias':
        [
            'poly2', 'polynomial2',
        ],
        'description': '2 order polynomial',
        'func': 'functions.poly2',
        'parname' :
        [
            r'$a$', r'$b$', r'$c$', 
        ],
        'par' :
        [
            'a', 'b', 'c',
        ],
        'bestv':
        {
            'a' : 1,
            'b' : 0.,
            'c' : 0.,
        },
        'bounds':
        {
            'a' : [-np.inf, np.inf],
            'b' : [-np.inf, np.inf],
            'c' : [-np.inf, np.inf],
        },
    },
    'poly3':
    {
        'engine': 'bol_tail',
        'alias':
        [
            'poly3', 'polynomial3',
        ],
        'description': '3 order polynomial',
        'func': 'functions.poly3',
        'parname' :
        [
            r'$a$', r'$b$', r'$c$', r'$d$', 
        ],
        'par' :
        [
            'a', 'b', 'c', 'd',
        ],
        'bestv':
        {
            'a' : 1,
            'b' : 0.,
            'c' : 0.,
            'd' : 0.,
        },
        'bounds':
        {
            'a' : [-np.inf, np.inf],
            'b' : [-np.inf, np.inf],
            'c' : [-np.inf, np.inf],
            'd' : [-np.inf, np.inf],
        },
    },
    'poly4':
    {
        'engine': 'bol_tail',
        'alias':
        [
            'poly4', 'polynomial4',
        ],
        'description': '4 order polynomial',
        'func': 'functions.poly4',
        'parname' :
        [
            r'$a$', r'$b$', r'$c$', r'$d$', r'$e$', 
        ],
        'par' :
        [
            'a', 'b', 'c', 'd', 'e',
        ],
        'bestv':
        {
            'a' : 1,
            'b' : 0.,
            'c' : 0.,
            'd' : 0.,
            'e' : 0.,
        },
        'bounds':
        {
            'a' : [-np.inf, np.inf],
            'b' : [-np.inf, np.inf],
            'c' : [-np.inf, np.inf],
            'd' : [-np.inf, np.inf],
            'e' : [-np.inf, np.inf],
        },
    },
    'poly5':
    {
        'engine': 'bol_tail',
        'alias':
        [
            'poly5', 'polynomial5',
        ],
        'description': '5 order polynomial',
        'func': 'functions.poly5',
        'parname' :
        [
            r'$a$', r'$b$', r'$c$', r'$d$', r'$e$', r'$f$', 
        ],
        'par' :
        [
            'a', 'b', 'c', 'd', 'e', 'f',
        ],
        'bestv':
        {
            'a' : 1,
            'b' : 0.,
            'c' : 0.,
            'd' : 0.,
            'e' : 0.,
            'f' : 0.,
        },
        'bounds':
        {
            'a' : [-np.inf, np.inf],
            'b' : [-np.inf, np.inf],
            'c' : [-np.inf, np.inf],
            'd' : [-np.inf, np.inf],
            'e' : [-np.inf, np.inf],
            'f' : [-np.inf, np.inf],
        },
    },
    'poly6':
    {
        'engine': 'bol_tail',
        'alias':
        [
            'poly6', 'polynomial6',
        ],
        'description': '6 order polynomial',
        'func': 'functions.poly6',
        'parname' :
        [
            r'$a$', r'$b$', r'$c$', r'$d$', r'$e$', r'$f$', r'$g$', 
        ],
        'par' :
        [
            'a', 'b', 'c', 'd', 'e', 'f', 'g',
        ],
        'bestv':
        {
            'a' : 1,
            'b' : 0.,
            'c' : 0.,
            'd' : 0.,
            'e' : 0.,
            'f' : 0.,
            'g' : 0.,
        },
        'bounds':
        {
            'a' : [-np.inf, np.inf],
            'b' : [-np.inf, np.inf],
            'c' : [-np.inf, np.inf],
            'd' : [-np.inf, np.inf],
            'e' : [-np.inf, np.inf],
            'f' : [-np.inf, np.inf],
            'g' : [-np.inf, np.inf],
        },
    },
}
