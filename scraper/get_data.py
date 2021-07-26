import numpy as np

def get_price(listing):
    try:
        #price = listing.find("span",{"class":"rui__sc-62xokl-0 dgVFTR"}).text
        #price = int(price.replace(",", "").replace("$", ""))
        price = listing.select("[data-label=pc-price]")[0].get_text()
        return price
    except:
        return np.nan


def get_beds(listing):
    try:
        bed = listing.select("[data-label=pc-meta-beds]")[0].get_text()
        return bed
    except:
        return np.nan
    

def get_baths(listing):
    try:
        baths = listing.select("[data-label=pc-meta-baths]")[0].get_text()
        return baths
    except:
        return np.nan
    

def get_sqft(listing):
    try:
        sqft = listing.select("[data-label=pc-meta-sqft]")[0].get_text()
        return sqft
    except:
        return np.nan


def get_sqftlot(listing):
    try:
        sqftlot = listing.select("[data-label=pc-meta-sqftlot]")[0].get_text()
        return sqftlot
    except:
        return np.nan


def get_broker(listing):
    try:
        broker = listing.select("[data-label=pc-brokered]")[0].get_text()
        return broker
    except:
        return np.nan


def get_address(listing):
    try:
        address = listing.select("[data-label=pc-address]")[0].get_text()
        return address
    except:
        return np.nan