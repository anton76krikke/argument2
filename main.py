
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


from ast import Num
from os import name


def greet(name, msg="hello!"):
    """
    This function greets to
    the person with the
    provided message.

    If the message is not provided,
    it defaults to "Good
    morning!"
    """

    print(msg + ', ' + name)


greet("doc")
greet("bob", "whats up")


body = {
    'sun': 2.74,
    'jupiter': 24.9,
    'neptune': 11.2,
    'earth': 9.82598,
    'uranus': 8.9,
    'venus': 8.9,
    'mars': 3.7,
    'mercury': 3.7,
    'moon': 1.6,
    'pluto': 0.6

}


def force(mass, body='earth'):
    body_afgerond = round(body, 1)
    force = body_afgerond * mass
    return force


l = force(2, body['earth'])
print('de zwaartekracht= ', l)


def pull(m1, m2, d):
    pull = 6.674*10**-11 * ((m1*m2)/(d**2))
    return pull


print('de kracht in newton is ', pull(800, 1500, 3))
