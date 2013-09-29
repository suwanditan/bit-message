"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": "002080629173148007EDF27C1E3E9701",
            "answer": ["26 Aug 2002 19:37:41 GMT +2", 7, "message"]
        },
        {
            "input": "00317050201171820FD3323BDC0ED341C4303DEC3E8700",
            "answer": ["05 Jul 2013 02:11:17 GMT +7", 15, "Selamat Datang!"]
        },
        {
            "input": "000130925161956915C8729E054A82C26D50DA0D7296EFA0EC5BBE06",
            "answer": ["29 Mar 2010 15:16:59 GMT -4", 21, "Hey, I am in New York"]
        },
        {
            "input": "08071010101010611F04180441043A043B044E04470435043D043804350020043F043E04340442043204350440043604340430043504420020043F0440043004320438043B043E",
            "answer": ["01 Jan 1970 01:01:01 GMT +4", 31, "Исключение подтверждает правило"]
        },
        {
            "input": "088310913041804C23805E4E0D82E5805E4E4B002C805E4E4B4E0D82E5898B4E4B002C898B4E4B4E0D82E577E54E4B002C77E54E4B4E0D82E5884C4E4B002C5B7881F365BC884C4E4B800C6B6277E3 ",
            "answer": ["19 Jan 2038 03:14:08 GMT -11", 35, "聞不若聞之,聞之不若見之,見之不若知之,知之不若行之,學至於行之而止矣"]
        },
        {
            "input": "04704072126132480B42F66E6AF67572205E5F5E",
            "answer": ["27 Apr 2007 21:16:23 GMT -1", 11, "Bönjöur ^_^"]
        },
        {
            "input": "08212092911273630630533093306b3061306f0021",
            "answer": ["29 Feb 2012 19:21:37 GMT +9", 6, "こんにちは!"]
        },
        {
            "input": "089021138034432B06C548B155D558C138C6940021",
            "answer": ["31 Dec 2009 08:43:34 GMT -8", 6, "안녕하세요!"]
        }
    ],
    "Extra": [
        {
            "input": "08908080909391230795776C5F5F8C6D6A63A8524D6D6A",
            "answer": ["08 Aug 2009 09:39:19 GMT +8", 7, "長江後浪推前浪"]
        },
        {
            "input": "089990712210858C21039103C503C403AC002003BC03BF03C5002003C603B103AF03BD03BF03BD03C403B103B9002003B103BB03B103BC03C003BF03C503C103BD03AD03B603B903BA03B1",
            "answer": ["17 Sep 1999 22:01:58 GMT -12", 33, "Αυτά μου φαίνονται αλαμπουρνέζικα"]
        },
        {
            "input":
                "009901912263916B30ED341D742C93EB6C32A8EE2683B4E5341DB47EB7DB74503BEC06DDCB693AA8053A96E5EDB01B340FE7E7",
            "answer": ["19 Oct 1999 22:36:19 GMT -9", 48, "mit Geduld und Zeit kommt man weit - German says"]
        },
        {
            "input": "08211130800174611D0417043D04300442044C0020043A0430043A002004410432043E043803010020043F044F0442044C0020043F04300301043B044C044604350432",
            "answer": ["03 Nov 2012 08:10:47 GMT +4", 29, "Знать как свои́ пять па́льцев"]
        },
        {
            "input": "049910925192744A1242FB682074726F6A696369206D696C756A65",
            "answer": ["29 Jan 1999 15:29:47 GMT -6", 18, "Bûh trojici miluje"]
        },
        {
            "input": "00306031205215442FCC321D44479741E3301DF4AED3416F33888E2E83C4E133A8052ABACFECF41C0D4A93D3EFF61CE4FD7A01",
            "answer": ["13 Jun 2003 02:25:51 GMT +11", 47, "Let the cat out of the bag - English idioms ^_^"]
        },
        {
            "input": "0896211332959508290445043E04420435043B04380020043A0430043A0020043B0443044704480435002C002004300020043F043E043B044304470438043B043E0441044C0020043A0430043A0020043204410435043304340430",
            "answer": ["31 Dec 2069 23:59:59 GMT +0", 41, "хотели как лучше, а получилось как всегда"]
        },
        {
            "input": "00153041916535845FA2F0399C76CFE9203ABA0C1AB3DFE3B508949E83E86F50984E2FB7E17410FD0D22BF41F377BB4C47A7DD6750780E3287E77450780E82BFE7F3B4985D06D5E7F5309B9D0789CBE6B7BC0C0A83C8E530999D769701",
            "answer": ["14 Mar 2051 19:56:53 GMT +12", 95,
                       "\"against the clock\" is to attempt to do something as fast as possible usually before a deadline"]
        }
    ]
}
