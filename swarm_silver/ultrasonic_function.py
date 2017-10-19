
def mesure_distance(sensor,distance):

     if distance == 'distance':
         sensor.mode ='US-DIST-CM'
         units = sensor.units

     mesure = sensor.value() / 10  # convert mm to cm

     return mesure



