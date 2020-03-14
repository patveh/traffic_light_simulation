from flask import Flask, render_template, request

app = Flask(__name__)

# the mode when the traffic light starts up, i.e. before anything is posted
mode = {'lights': [1], 'on': [500], 'blink': 1, 'minimum_duration_ms': 3000}

@app.route('/trafficlight', methods=['POST', 'GET'])
def activate_traffic_light():

    # global because a GET is made when html page is refreshed
    global mode
    
    refresh_interval = mode['minimum_duration_ms']

    if request.method == 'POST':
        mode = request.get_json()
        print(mode)
        # set the wait time needed for the posted light sequence to run 
        refresh_interval = mode['minimum_duration_ms']
    
    return render_template('traffic-light.html', mode=mode, refresh_interval=refresh_interval)
