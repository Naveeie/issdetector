from flask import Flask,redirect, url_for,render_template
import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder

app = Flask(__name__)

def iss():
  # Setup the world map in turtle module
  screen = turtle.Screen()
  screen.setup(1200, 700)
  screen.setworldcoordinates(-180, -90, 180, 90)

  # load the world map image
  screen.bgpic("mapg.gif")
  screen.register_shape("issg.gif")
  iss = turtle.Turtle()
  iss.shape("issg.gif")
  iss.setheading(45)
  iss.penup()

  while True:
      # load the current status of the ISS in real-time
      url = "http://api.open-notify.org/iss-now.json"
      response = urllib.request.urlopen(url)
      result = json.loads(response.read())

      # Extract the ISS location
      location = result["iss_position"]
      lat = location['latitude']
      lon = location['longitude']

      # Ouput lon and lat to the terminal
      lat = float(lat)
      lon = float(lon)
      # print("\nLatitude: " + str(lat))
      # print("\nLongitude: " + str(lon))

      # Update the ISS location on the map
      iss.goto(lon, lat)

      # Refresh each 5 seconds
      time.sleep(5)
@app.route('/')
def hello_world():
    # return render_template('index.html')
    return iss()


if __name__ == '__main__':
  app.run(debug=True)