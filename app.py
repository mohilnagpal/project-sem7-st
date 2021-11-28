from bs4 import BeautifulSoup
import requests
import pandas as pd 
from flask import Flask, render_template
# from Backendpy.textiles import tex_sec
# from Backendpy.automobile import auto_sec
# from Backendpy.agro_pro import agroproducts
# from Backendpy.airlines import airlines
# from Backendpy.alcoholic_beverages import alchoholbev
# from Backendpy.building_products import buildingpro
# from Backendpy.cements import cement_sec
# from Backendpy.construction import const_sec
# from Backendpy.electricals import electricals
# from Backendpy.fmcg_foods import fmcgfoods
# from Backendpy.fmcg_products import products
# from Backendpy.fmcg_tobacco import tobacco
# from Backendpy.it import infotech
# from Backendpy.logistics import logi_sec
# from Backendpy.paints import paints
# from Backendpy.petroleum import petroleum
# from Backendpy.pharma import pharma_sec
# from Backendpy.power_generation import power
# from Backendpy.renewable_energy import ren
# from Backendpy.restaurant_cafe import rest
# from Backendpy.retail import retail
# from Backendpy.tel_equip import teleq
# from Backendpy.telecom_sector import tel
# from Backendpy.fertilizers import fertilizers


from Backendpy.textiles import function_textile
from Backendpy.automobile import function_automobile
from Backendpy.agro_pro import function_agropro
from Backendpy.airlines import function_airlines
from Backendpy.alcoholic_beverages import function_alchohol
from Backendpy.building_products import function_building
from Backendpy.cements import function_cement
from Backendpy.construction import function_construction
from Backendpy.electricals import function_electricals
from Backendpy.fmcg_foods import function_foods
from Backendpy.fmcg_products import function_products
from Backendpy.fmcg_tobacco import function_tobacco
from Backendpy.it import function_it
from Backendpy.logistics import function_logistics
from Backendpy.paints import function_paints
from Backendpy.petroleum import function_petroleum
from Backendpy.pharma import function_pharma
from Backendpy.power_generation import function_power
from Backendpy.renewable_energy import function_renewable
from Backendpy.restaurant_cafe import function_restauraunt
from Backendpy.retail import function_departmental
from Backendpy.tel_equip import function_teleq
from Backendpy.telecom_sector import function_telecom
from Backendpy.fertilizers import function_fertilizers
from Backendpy.banks_function import function_banks

from Backendpy.safe_play_portfolio import function_safeplay
from Backendpy.all_weather_portfolio import function_allweather
from Backendpy.buy_right_portfolio import function_buyright


list_textile=function_textile()
list_auto=function_automobile()
list_agropro=function_agropro()
list_airlines=function_airlines()
list_alcohol=function_alchohol()
list_building=function_building()
list_cements=function_cement()
list_construction=function_construction()
list_electricals=function_electricals()
list_foods=function_foods()
list_products= function_products()
list_tobacco = function_tobacco()
list_it = function_it()
list_logistics = function_logistics()
list_paints = function_paints()
list_petroleum = function_petroleum()
list_pharma = function_pharma()
list_power = function_power()
list_renewable = function_renewable()
list_restaurant = function_restauraunt()
list_retail = function_departmental()
list_telequip = function_teleq()
list_telecom = function_telecom()
list_fertilizers = function_fertilizers()
list_bank=function_banks()
list_safeplay=function_safeplay()
list_allweather= function_allweather()
list_buyright=function_buyright()


app = Flask(__name__)


@app.route('/automobile.html')
def automobile():
    return render_template('automobile.html', autolist=list_auto)

@app.route('/textiles.html')
def textiles():
    return render_template('textiles.html', textlist=list_textile)

@app.route('/Agroproducts.html')
def agroproducts():
    return render_template('Agroproducts.html', agrolist=list_agropro)

@app.route('/airlines.html')
def airlines():
    return render_template('airlines.html', airlist=list_airlines)

@app.route('/alchohol.html')
def alchohol():
    return render_template('alchohol.html', alclist=list_alcohol)

@app.route('/Buildingproducts.html')
def building_products():
    return render_template('Buildingproducts.html', bullist=list_building)

@app.route('/cements.html')
def cements():
    return render_template('cements.html', cemlist=list_cements)

@app.route('/construction.html')
def construction():
    return render_template('construction.html', constlist=list_construction)

@app.route('/electricalpro.html')
def electricals():
    return render_template('electricalpro.html', eleclist=list_electricals)

@app.route('/fmcgfoods.html')
def foods():
    return render_template('fmcgfoods.html', foodlist=list_foods)

@app.route('/fmcgproducts.html')
def products():
    return render_template('fmcgproducts.html', prolist=list_products)

@app.route('/fmcgtobacco.html')
def tobacco():
    return render_template('fmcgtobacco.html', toblist=list_tobacco)

@app.route('/ITconsulting.html')
def itcon():
    return render_template('ITconsulting.html', itlist=list_it)

@app.route('/logistics.html')
def logistics():
    return render_template('logistics.html', loglist=list_logistics)

@app.route('/paints.html')
def paints():
    return render_template('paints.html', painlist=list_paints)

@app.route('/petroleum.html')
def petroleum():
    return render_template('petroleum.html', petrolist=list_petroleum)

@app.route('/pharmaceuticals.html')
def pharmaceuticals():
    return render_template('pharmaceuticals.html', pharmalist=list_pharma)

@app.route('/powergeneration.html')
def powergeneration():
    return render_template('powergeneration.html', powerlist=list_power)

@app.route('/renewable.html')
def renewable():
    return render_template('renewable.html', renewlist=list_renewable)

@app.route('/departmental.html')
def retail():
    return render_template('departmental.html', retailist=list_retail)

@app.route('/telequip.html')
def telecom_equip():
    return render_template('telequip.html', equip=list_telequip)

@app.route('/telsector.html')
def telecom_sec():
    return render_template('telsector.html', telseclist=list_telecom)

@app.route('/agrofertilizers.html')
def fertillizers():
    return render_template('agrofertilizers.html', fertlist=list_fertilizers)

@app.route('/restaurants.html')
def restaurant():
    return render_template('restaurants.html', restlist=list_restaurant)

@app.route('/banks.html')
def bank():
    return render_template('banks.html', banklist=list_bank)

@app.route('/')
def safeplay():
    return render_template('index.html', safeplay=list_safeplay, allweather=list_allweather,buyright=list_buyright)



# @app.route('/')
# def hello_world():
#     return render_template('index.html')

if __name__=="__main__":
    app.run()

