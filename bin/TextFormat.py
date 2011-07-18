#!/usr/bin/python

import subprocess

class TextFormatter:
    def __init__(self,lynx='/usr/bin/lynx'):
        self.lynx = lynx

    def html2text(self, html_source):
        "Expects unicode; returns unicode"
        return subprocess.Popen([self.lynx,
                      '-dump',
                      '-stdin',
                      '-nolist'],
                      stdin=subprocess.PIPE,
                      stdout=subprocess.PIPE).communicate(input=html_source)

if __name__ == "__main__":
    test = TextFormatter()
    print test.html2text("<html><body><p>This is a test.</p><p>You should have a 303 with you.</p></body></html>")[0]
