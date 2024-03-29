import flask
import os
import pandas as pd

#create an instance of Flask
app = flask.Flask('Earthquake Model Deployment')
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/')
def home():
    metadata = pd.read_csv('data_temp.csv')
    data_station = {}
    for idx_ in range(len(metadata)):
        each_station = {}
        station_ = metadata.loc[idx_, 'Station']
        station_location_ = metadata.loc[idx_, 'Station Name']
        lat_ = metadata.loc[idx_, 'Station_Latitude']
        long_ = metadata.loc[idx_, 'Station_Longitude']
        elevation_ = metadata.loc[idx_, 'Elevation']

        each_station.update({
            'Station':station_,
            'Station Location':station_location_,
            'Latitude':lat_,
            'Longitude':long_,
            'Elevation':elevation_
        })
        data_station.update({int(idx_+1):each_station})

        if int(idx_+1)==30:
            break
    return flask.jsonify(data_station)

if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 8080)),host='0.0.0.0',debug=True)
