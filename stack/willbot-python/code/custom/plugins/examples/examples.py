from will.plugin import WillPlugin
import requests
from lxml import html
from lxml.etree import tostring
import random
import re
import time
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings

class ExamplesPlugin(WillPlugin):

    @hear("mybot is awesome")
    def hear_mybot_love(self, message):

        self.say("Hey....I love you too.", message=message)

    def get_packt_book_of_the_day_name(self):

        r = requests.get('https://www.packtpub.com/packt/offers/free-learning')
        tree = html.fromstring(r.content)
        book = tree.xpath('//*[@id="deal-of-the-day"]/div/div/div[2]/div[2]/h2')
        return re.sub('<[^<]+?>', '', tostring(book[0]))

    @hear("packt book of the day")
    def hear_packt_book_of_the_day(self, message):

        context = {
            "book": self.get_packt_book_of_the_day_name()
        }

        self.say(rendered_template("dkcwd_packt_book_of_the_day.html", context), message=message, html=True, notify=True)

    @randomly(start_hour='9', end_hour='10', day_of_week="mon-sun", num_times_per_day=1)
    def packt_book_of_the_day_almost_over(self):

        context = {
            "book": self.get_packt_book_of_the_day_name()
        }

        self.say(rendered_template("dkcwd_packt_book_of_the_day_almost_over.html", context), html=True, notify=True)

    @randomly(start_hour='12', end_hour='13', day_of_week="mon-sun", num_times_per_day=1)
    def packt_book_of_the_day_new_available(self):

        context = {
            "book": self.get_packt_book_of_the_day_name()
        }

        self.say(rendered_template("dkcwd_packt_book_of_the_day_new_available.html", context), html=True, notify=True)

    @hear("timezones|what time|time in|what is the time")
    def hear_dkcwd_team_timezones(self, message):

        context = {
            "date": time.strftime('%Y%m%d')
        }

        self.say(rendered_template("dkcwd_team_timezone_times.html", context), message=message, html=True, notify=True)

    @hear("(escalation) (process|procedure)|escalation process|(how|who) do (i|we) escalate")
    def hear_dkcwd_team_escalation_process(self, message):

        context = {
            "link": 'some web address',
            "text": 'Here is the link to the escalation process'
        }

        self.say(rendered_template("dkcwd_generic_team_link.html", context), message=message, html=True, notify=True)

    @hear("('s|s) (mother|mom|mum)('s|s) (mobile|number|phone|cell)")
    def hear_dkcwd_mom_number(self, message):

        context = {
            "link": 'https://www.youtube.com/watch?v=AhYP7HSKiGc',
            "text": 'Here is the only link you need'
        }

        self.say(rendered_template("dkcwd_generic_team_link.html", context), message=message, html=True, notify=True)

    def get_dkcwd_team_jokes(self):

        return [
            {
                'question': 'What do you call a fake noodle?',
                'answer': 'An Impasta'
            },
            {
                'question': 'What is the difference between a guitar and a fish?',
                'answer': 'You cannot tuna fish'
            },
            {
                'question': 'What do you call an alligator in a vest?',
                'answer': 'An Investigator'
            },
            {
                'question': 'Did you hear about the race between the lettuce and the tomato?',
                'answer': 'The lettuce was a "head" and the tomato was trying to "ketchup'
            },
            {
                'question': 'Did you hear about the hungry clock?',
                'answer': 'It went back four seconds'
            },
            {
                'question': 'What do you get from a pampered cow?',
                'answer': 'Spoiled milk'
            },
            {
                'question': 'If Mississippi bought Virginia a New Jersey, what would Delaware?',
                'answer': 'Idaho... Alaska'
            },
            {
                'question': 'What do you call an elephant which does not matter?',
                'answer': 'An irrelephant'
            },
            {
                'question': 'What do lawyers wear to court?',
                'answer': 'Lawsuits'
            },
            {
                'question': 'What do you call a fat psychic?',
                'answer': 'A four chin teller'
            },
            {
                'question': 'Did you hear about the shampoo shortage in Jamaica?',
                'answer': 'Some people say it is dread-full'
            },
            {
                'question': 'What do you call a three-footed aardvark?',
                'answer': 'A yardvark'
            },
            {
                'question': 'How do you drown a Hipster?',
                'answer': 'In the mainstream'
            },
            {
                'question': 'What do you call a man with no body and just a nose?',
                'answer': 'Nobody nose'
            },
            {
                'question': 'What is the first bet that most people make in their lives?',
                'answer': 'The "alpha" bet'
            },
            {
                'question': 'What do you call cheese that is not yours?',
                'answer': 'Nacho cheese'
            }
        ]

    @hear("joke")
    def hear_dkcwd_team_joke(self, message):

        joke = random.choice(self.get_dkcwd_team_jokes())

        joke_question = joke['question']
        joke_answer = joke['answer']

        context = {
            "joke_question": joke_question,
            "joke_answer": joke_answer
        }

        self.say(rendered_template("dkcwd_team_joke.html", context), message=message, html=True, notify=True)

    @randomly(start_hour='03', end_hour='13', day_of_week="tue-sat", num_times_per_day=1)
    def dkcwd_team_random_joke(self):

        joke = random.choice(self.get_dkcwd_team_jokes())

        joke_question = joke['question']
        joke_answer = joke['answer']

        context = {
            "joke_question": joke_question,
            "joke_answer": joke_answer
        }

        self.say(rendered_template("dkcwd_team_joke.html", context), mhtml=True, notify=True)
