# Titanic

## What is this project?

The result of an assignment for [Masterschool](https://learn.masterschool.com/). ![NO IMAGE](https://img.shields.io/badge/Titanic-100-4574E0)

A terminal application access ship data.

## How to use?

> [!NOTE]
> Tested on `Python 3.13.3`

1. Open movies.py
2. Select your desired option:
    |cmd|arg|desc|
    |---|---|---|
    |help||Prints a list of the available commands.|
    |show_countries||Prints a list of all the countries of the ships, without duplicates. The countries should be ordered alphabetically.|
    |top_countries|num_countries:`int`|Prints a list of top countries with the most ships. For example, top_countries 5, prints a list of the 5 countries which have the most ships, along with the number of ships.|

## Masterschool Codio Description

## Titanic

### Overview
In this exercise we are exploring the data from MarineTraffic, you can find it in this [link](https://www.marinetraffic.com/en/data/?asset_type=vessels&columns=flag,shipname,photo,recognized_next_port,reported_eta,reported_destination,current_port,imo,ship_type,show_on_live_map,time_of_latest_position,lat_of_latest_position,lon_of_latest_position,notes).

The data from the website was magically exported to a JSON file, a convenient format for object serialization: 

serialization is basically converting objects to a format, like a text file (or JSON in our example), so we can save it to disk / send it in email / whatever we want, and then convert it again to objects in our Python program, for example.

In the exercise, we build a command line interface for analyzing the data of the ships.

### Data Description

We can find the data inside the file ships_data.json, which is opened for us. 

### Specification

#### Ship Data Structure

```json
{
"data":[
        {
            "SHIP_ID":"371681",
            "IMO":"9241061",
            "MMSI":"310627000",
            "CALLSIGN":"ZCEF6",
            "SHIPNAME":"QUEEN MARY 2",
            "TYPE_COLOR":"6",
            "LAST_POS":1630428117,
            "CODE2":"BM",
            "COUNTRY":"Bermuda",
            "COUNT_PHOTOS":"1579",
            "NEXT_PORT_NAME":"BREST",
            "NEXT_PORT_COUNTRY":"FR",
            "NEXT_PORT_ID":"501",
            "ETA":1630031400,
            "DESTINATION":"BREST",
            "TYPE_SUMMARY":"Passenger",
            "COURSE":"68",
            "LON":"-4.45233",
            "LAT":"48.38464",
            "TIMEZONE":"2",
            "ETA_OFFSET":"2",
            "SPEED":"0.0",
            "ETA_UPDATED":null,
            "DISTANCE_TO_GO":"0",
            "PORT_ID":"501",
            "CURRENT_PORT":"BREST",
            "CTA_ROUTE_FORECAST":"false"
        }
        ]
}
```