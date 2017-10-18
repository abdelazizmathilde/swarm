def mesure_position(sensor,mode):
    if mode == 'angle':
        sensor.mode = 'GYRO-ANG'
        units = sensor.units #choose the degres units
        mesure = sensor.value()

        return mesure
