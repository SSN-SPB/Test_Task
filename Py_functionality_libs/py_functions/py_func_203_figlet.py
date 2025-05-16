from pyfiglet import Figlet

# from pyfiglet import Figlet, FigletFont


"""
It takes ASCII text and renders it in ASCII art fonts
(like the title above, which
is the 'block' font).
"""
"""
like below
#      #            #                  #
#                   #                 # #
#     ##     ###   ###          ##    #
#      #    ##      #          #  #  ###
#      #      ##    #          #  #   #
####  ###   ###      ##         ##    #

  #                #
 # #               #
 #     ##   ###   ###    ###
###   #  #  #  #   #    ##
 #    #  #  #  #   #      ##
 #     ##   #  #    ##  ###


"""


def print_figlet():
    # selected_font = Figlet(font="5x7")
    # selected_font = Figlet(font="slant")
    selected_font = Figlet(font="zig_zag_")
    selected_font = Figlet(font="6x10")
    print(selected_font.renderText("List of fonts"))
    # for x in FigletFont.getFonts():
    #     print(x)


def main():
    print_figlet()


if __name__ == "__main__":
    main()
