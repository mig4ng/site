# config.py - Vite's configuration script

title = 'icyphox'
author = ''
header = """
        <a href="/">home</a>
        <a href="/blog">blog</a>
        <a href="/reading">reading</a>
        <a href="https://twitter.com/icyphox">twitter</a>
        <a href="/about">about</a>
"""
footer = """<a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
        <img class="footimgs" src="/static/cc.svg">
        </a>
        <a href="https://webring.xxiivv.com/#random" target="_blank">
        <img class="footimgs" alt="xxiivv webring" src="/static/webring.svg">
        </a>
        """
template = 'text.html'  # default is index.html
post_build = ['./bin/rss.py']
