import requests
import argparse
import ast
import turtle
import time


def astros(website):
    r = requests.get(website)
    d = ast.literal_eval(r.text)
    astronauts = d.get("people")
    for moonman in astronauts:
        print "{}, {}".format(moonman.get("name"), moonman.get("craft"))
    print "Number of astronauts, {}".format(d.get("number"))


def pos(website):
    r = requests.get(website)
    d = ast.literal_eval(r.text)
    location = d.get("iss_position")
    lat = location.get("latitude")
    lon = location.get("longitude")
    print ("Latitude: {}, Longitude: {}, Time: {}"
           .format(lat, lon, d.get("timestamp")))
    iss = "iss.gif"
    t = turtle.Turtle()
    s = turtle.Screen()
    s.setup(720, 360)
    s.bgpic("map.gif")
    s.addshape(iss)
    t.shape(iss)
    t.penup()
    t.setposition((720 * (float(lon)/360)), (360 * (float(lat)/180)))
    t.pendown()
    klat = "39.765840"
    klon = "-86.157620"
    p = requests.get('http://api.open-notify.org/iss-pass.json?lat='
                     + klat + "&lon=" + klon)
    passd = ast.literal_eval(p.text)
    response = passd.get("response")
    next_pass = time.ctime(response[0].get("risetime"))
    dot = turtle.Turtle()
    dot.penup()
    dot.setposition((720 * (float(klon)/360)), (360 * (float(klat)/180)))
    dot.pendown()
    dot.dot(5, "yellow")
    dot.write(next_pass, font=("Arial", 16, "normal"))
    turtle.mainloop()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--astros', help="""Find what astronauts are
                         currently in space""")
    parser.add_argument('--position', help=""""Find the position of
                        the ISS""")
    args = parser.parse_args()
    if args.astros:
        astros(args.astros)
    elif args.position:
        pos(args.position)


if __name__ == "__main__":
    main()
