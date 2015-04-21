"""
╔╦╗┬┌┐┌┌─┐   ╦ ╦┬  ╦ ╦┬ ┬┌─┐┌┐┌┌─┐
║║║│││││ ┬───╚╦╝│  ╠═╣│ │├─┤││││ ┬
╩ ╩┴┘└┘└─┘    ╩ ┴  ╩ ╩└─┘┴ ┴┘└┘└─┘
"""
from agilearning import agilearner


@agilearner
def mingyi(**my):
    """ Learning Mixer """

    assert my["github"] == "http://github.com/anniehuang921"
    assert my["email"] == "anniehuang921@icloud.com"
    assert my["phone_number"] == "+886 911-261356"
    assert agilearning.VAT_ID == 24755908
