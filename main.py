import argparse
from scripts.youtube_utilities import download
from scripts.redirects import trace

import os

if __name__ == "__main__":
    # Setting up Main Argument Parser
    main_parser = argparse.ArgumentParser(description="A set of python web utility scripts")
    main_parser.add_argument("-v",'--version', action='version', version='kuws V0.0.1')

    # Setting up the main subparser
    subparsers = main_parser.add_subparsers(help="Available commands found below, for more info on a command use: python main.py <command> -h")

    """Code below handles 'youtube' command in the main script
    i.e. >python main.py youtube
    """
    youtube_parser = subparsers.add_parser('youtube', argument_default='-m',
        help='Allows you to interact with youtube videos')
    youtube_parser.add_argument('-d', "--download", 
        help='usage: python main.py youtube -d <url>; Lets you download a specified youtube video', nargs='?', dest="download_url")

    youtube_parser.add_argument('-p', "--path", default=".",
        help='usage: python main.py youtube -d <url> -p /downloads; Lets you set a path to download', nargs='?', dest="download_path")
    


    """Code below handles 'redirects' command in the main script
    i.e. >python main.py youtube
    """
    redirects_parser = subparsers.add_parser('redirects', argument_default='-u',
        help='Allows you to trace redirects and get other information')

    redirects_parser.add_argument('-u', "--url", 
        help='usage: python main.py redirects -u <url>; Lets you see the trace for a url', nargs='?', dest="trace_url")
        
    # Obligatory argument parsing, setting arguments to args for later use


    args = main_parser.parse_args()

    try:
        if args.trace_url:
            trace(args.trace_url, print_response=True)
    except AttributeError: #For some ungodly reason argparse throws a hissy fit for daring to check namespace variables
        pass
    except Exception as identifier:
        print("Exception in URL trace with error: {}".format(identifier))

    #TODO: Write youtube parsing download parsing properly
    # try:
    #     if (args.download_url and not args.download_path): # If no -p was specified
    #         print("video will be downloaded to script source folder: {}".format(os.getcwd()))
    #         download(args.download_url[0], '.')
    #     else:
    #         print("video will be downloaded to specified directory: {}".format(args.download_path[0]))
    #         download(args.download_url[0], args.download_path[0])
    # except AttributeError: #For some ungodly reason argparse throws a hissy fit for daring to check namespace variables
    #     pass
    # except Exception as identifier:
    #     print("exception in download path with error: {}".format(identifier))