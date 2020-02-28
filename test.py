from flask import Flask, render_template, redirect, session
from forex_python.converter import CurrencyRates, CurrencyCodes

c = CurrencyRates()
s = CurrencyCodes()

rates = c.convert('USD','JYP', '')