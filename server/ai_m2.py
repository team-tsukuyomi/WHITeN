﻿import sys
import random
import json
from wikipedia import page, PageError, DisambiguationError
from os import getcwd, system, scandir
from urllib.error import *
from requests.exceptions import *
from googlesearch import search as sch
import os
from pyowm import *
from time import *
from random import randint
from jokeapi import Jokes # Import the Jokes class
import asyncio
from math import *
import rivescript as rs
__author__ = ["Prabhakar Dev"]
input_text = input
print('importing modules..')
try:
    # import recog                         #comment this line for text input
    input = recog.predict
except BaseException as e:
    print(e.args)
print('setting up...')

# owm=OWM(key)
# owm=owm.weather_manager()
sadface = "😔 😟 ☹ 🥺 😢 😭 😞 😣 😖 😓 😩 😫".split()
# speak=speech.setup_speech()

system('@echo off')


def degrees(temp):
    t = int(temp)
    return str(round(5/9*(t-32)))


def concat(strings):
    c = ''
    for string in strings:
        c += str(string)
    return c


def s_print(strings, extras=[]):
    for txt in strings:
        print(txt)
    return ("\n".join(map(str, strings+extras)))
    #speak(concat(strings).replace('\n','. '))
    # pop(concat(strings+extras).replace("\n","."))

async def print_joke():
        j = await Jokes()
        joke = await j.get_joke(blacklist=['nsfw','racist','religious','political','explicit'])
        if joke["type"] == "single":
            return s_print([joke["joke"]])
        else:
            return s_print([joke["setup"],joke["delivery"]])

def search3(topic):
    try:
        return s_print(['###Here are links:- '], [*list(map(lambda x: "- ["+x+"]("+x+")", sch(topic, stop=5)))])
    except (ConnectionError, URLError):
        return s_print(['#Unable to Connect'])
    except RuntimeError:
        return search(topic)


def search2(topic):
    try:
        return s_print(['###Here are links:- '], ['\n'.join(map(lambda x: "- ["+x+"]("+x+")", sch(topic, stop=10)))])
    except (ConnectionError, URLError):
        return s_print(['#Unable to Connect'])
    except RuntimeError:
        return search3(topic)


def search(topic):
    try:
        p = page(topic)
        cont = p.summary
        if len(cont) > 1000:
            cont = cont[:1000]+"..."
        return (s_print(["#"+p.title, cont, f"[{p.title}]({p.url})"]), p.images[0])
    except PageError:
        return search2(topic)
    except DisambiguationError:
        return search2(topic)
    except ConnectionError:
        return search2(topic)


x = rs.RiveScript(True, log=".txt")
# a=App()
code = open('assistant/ai2.rive','rb')
x.stream(code.read().decode('utf-8'))
x.sort_replies()
inp = ''
s_print(['Hello, Human!'])


def reply(inp, stdscr=None, label=None):
    inp = inp.replace('don\'t', 'do not').replace('can\'t', 'cannot').replace(
        '\'ld', ' would').replace('\'ll', 'will').replace('dont', 'do not').replace('cant', 'cannot')
    if 'calculate' in inp.lower():
        if inp.endswith(".."):
            return s_print(['Your answer is:- ', eval(inp[inp.index('e')+1:len(inp)].replace('.', ''))])
        else:
            return s_print(['Your answer is:- ', eval(inp[inp.index('e')+1:len(inp)])])
    if 'flip a coin' in inp.lower():
        ht = ['heads', 'tails']
        if 'times' in inp.lower():
            n = int(inp[inp.index('n')+1:inp.index('t')].strip())
            h = randint(1, n)
            return s_print(['the results are:', h, ' heads and ', n-h, ' tails'])
        else:
            return s_print(['It is a '+ht[randint(0, 1)]])
    elif 'what is the weather' in inp.lower():
        try:
            obs = owm.weather_at_place('Ranchi,IN')
            ret = json.loads(obs.to_JSON())['Weather']
            print(ret)
            return s_print(['In my city, the weather conditions will most likely be ', ret['detailed_status'], '\nTemperature will remain around ', ret["temperature"]["temp"], ' Kelvin ', 'Humidity ', ret['humidity'], '%. Winds will blow at ', ret['wind']['speed'], ' metres per second at ', ret['wind']['deg'], '\u00b0 from North'])
        except ConnectionError as e:
            print(e.args)
            return s_print(['NO CONNECTION.\nI cant check the weather without a connection'])
    elif 'tell me a joke' in inp.lower().strip():
        if label is not None:
            label.setText('<h2>Getting jokes</h2>')
            label.repaint()
        return asyncio.run(print_joke())
    elif 'search' in inp.lower() or 'google' in inp.lower():
        if stdscr is not None:
            for i in range(20):
                stdscr.move(i, 0)
                stdscr.clrtoeol()
            stdscr.addstr(0, 0, "getting the results")
            stdscr.refresh()
        if label is not None:
            label.setText("<h1>getting the results</h1>")
            label.repaint()
        if 'search' in inp.lower():
            if 'for' in inp.lower():
                t = inp[inp.index('r', inp.index('f'))+1:len(inp)]
                return search(t)
            else:
                t = inp[inp.index('h')+1:len(inp)]
                return search(t)
        else:
            if 'for ' in inp.lower():
                t = inp[inp.index('r ', inp.index('f'))+1:len(inp)]
                return search(t)
            else:
                t = inp[inp.index('e')+1:len(inp)]
                return search(t)
    elif (('who is' in inp.lower()) or ('what is' in inp.lower()) or ('where is' in inp.lower())) and not ('your' in inp.lower() or 'this project' in inp.lower()):
        s_print(['getting the results...', 'click OK to continue'])
        y = inp[inp.index('s')+1:len(inp)]
        return search2(y)
    elif (('who are' in inp.lower()) or ('what are' in inp.lower()) or ('where are' in inp.lower())) and not ('you' in inp.lower() or 'this project' in inp.lower()):
        s_print(['getting the results...', 'click OK to continue'])
        y = inp[inp.index('e')+1:len(inp)]
        return search2(y)
    elif inp.strip() in sadface:
        return s_print(['# Dont be sad', '*smile*', '😃'])
    else:
        out = x.reply('user', inp.lower())
        if out == 'code 404':
            if label is not None:
                label.setText("<h2>I didnt understand what you said, so i am searching it...</h2>")
                label.repaint()
            return search3(inp)
        else:
            return s_print([*out.split('\n')])
