def celsius_para_fahrenheit(temp_em_celsius):
    temp_em_fahrenheit = 1.8 * temp_em_celsius + 32
    return temp_em_fahrenheit


def fahrenheit_para_celsius(temp_em_fahrenheit):
    temp_em_celsius = (temp_em_fahrenheit - 32) / 1.8
    return temp_em_celsius

if __name__ == '__main__':
    print('{} ºF'.format(celsius_para_fahrenheit(10)))
    print('{} ºC'.format(fahrenheit_para_celsius(212)))