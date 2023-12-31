import argparse
from command_timer import CommandTimer, CommandTimerArugument

__author__ = 'customtea (https://github.com/customtea/)'
__version__ = '1.0.0'
__program__ = 'cmdtimer'

def version():
    return f'{__program__} ver:{__version__} Created By {__author__}'

def getOption():
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument( '--ring',
        action='store_true',
        default=None,
        help='Sounding Chime')

    parent_parser.add_argument( '--silent',
        action='store_true',
        default=None,
        help='No Sound')

    parent_parser.add_argument( '--repeat',
        action='store_true',
        default=False,
        help='Repeat Timer')

    parent_parser.add_argument( '--sound',
        nargs='?',
        metavar="File Name",
        type=str,
        default=None,
        help='Select Sound File')

    parent_parser.add_argument( '--scount',
        nargs='?',
        metavar="Count",
        type=int,
        default=3,
        help='Sound Count')

    parent_parser.add_argument( '--progress',
        action='store_true',
        default=None,
        help='Terminal Progress Bar')

    parent_parser.add_argument( '--gui',
        action='store_true',
        default=None,
        help='GUI Progress Bar')

    parser = argparse.ArgumentParser(description="Commndline Timer")
    subparsers = parser.add_subparsers(title="Timer Mode", help="Mode", dest="mode", required=True)

    timer_parser = subparsers.add_parser("timer", help="Default Normal Timer", parents=[parent_parser])
    game_parser = subparsers.add_parser("game", help="Set Timer from prod mass in game (like Idle Game)", parents=[parent_parser])
    alarm_parser = subparsers.add_parser("alarm", help="[Not Implement] Set Timer from DateTime", parents=[parent_parser])
    cron_parser = subparsers.add_parser("cron", help="[Not Implement] Set Timer Like 'Cron' Table", parents=[parent_parser])

    timer_parser.add_argument( '--sec',
        nargs='?',
        type=int,
        metavar="seccond",
        default=0,
        help='Seccond')
    timer_parser.add_argument( '--min',
        nargs='?',
        type=int,
        metavar="minutes",
        default=0,
        help='Minutes')
    timer_parser.add_argument( '--hour',
        nargs='?',
        type=int,
        metavar="hour",
        default=0,
        help='Hour')

    game_parser.add_argument('--prod',
                            nargs='?',
                            type=float,
                            metavar="Production",
                            default=1,
                            help='Production Rate / sec')

    game_parser.add_argument('--mass',
                            nargs='?',
                            type=float,
                            metavar="Mass",
                            default=10,
                            help='Target Production Mass')

    parser.add_argument('--version', action='version', version=f"{version()}")
    return parser.parse_args()




if __name__ == '__main__':
    pargs = CommandTimerArugument()
    args = getOption()
    pargs.fromargparse(args)
    timer: CommandTimer
    if args.gui:
        from gui_bar_command_timer import GUIBarCommandTimer
        timer = GUIBarCommandTimer(pargs)
    elif args.progress:
        from terminal_bar_command_timer import TerminalBarCommandTimer
        timer = TerminalBarCommandTimer(pargs)
    else:
        timer = CommandTimer(pargs)
    timer.run()