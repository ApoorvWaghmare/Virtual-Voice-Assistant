from ChatBot import Chat

set_pair= [["Hello|Hi|Hey",
            ["Hi, I am the virtual assistant here to guide you, May I know your name"]
           ],
           ["(.*) am (.*).",
            ["Hi %2 , what can i help %1 with?"]
           ],
           ["(.*) need help setting up my (account|password|id)",
            ["I will send %1 a set of instructions on your mobile phone. May I have your mobile number?"]
           ],
           ["Yes it is (.*)",
            ["Say YES to confirm the number entered is %1."]
           ],
           [",Yes|yes|YES",
            ["The instructions have been sent to your mobile phone. Anything else you would like my help with"]
           ],
           ["(No Thankyou|No|No Thanks|no thanks)",
            ["Glad to be of help"]
           ],
           ["quit",
            ["Bye, have a great day, stay home, stay safe"]
           ]
]


reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you",
}

chatBot = Chat(set_pair, reflections)

chatBot.converse()