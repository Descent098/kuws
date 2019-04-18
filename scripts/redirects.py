"""Utilities to handle redirects and redirect histories, also some proxy info"""
import requests

ignored_domains = ["safelinks.protection.outlook.com", "can01.safelinks.protection.outlook.com"] # A list of domains to ignore in trace

def trace(url, print_response = False):
    """
    :param: url
    :type url: String

    """
    if ("https://" or "http://") in url: # Checks if protocols are present
        None
    else: # Add a protocol to URL
            url = "https://" + url

    try:
        trace = requests.get(url)
    except Exception as identifier:
        return(["Error while checking {} \nError Code: {}".format(url, identifier)])

    if trace.history:
        skip_ignored_domains(trace.history)
        if print_response == True:
            print("\nPrinting trace for {}".format(url))
        for level, redirect in enumerate(trace.history):
            if print_response == False:
                yield([level, redirect.url, redirect.status_code])
            else:
                print("Redirect level: {} \nURL:{} \nResponse Code: {}".format(level, redirect.url, redirect.status_code))
    else:
        return(["Request was not redirected"])

def skip_ignored_domains(response_trace):
    """
    :param: response_trace
    :type response_trace: List of responses
    :returns: The stripped list of responses
    :return_type: List of responses

    Takes a list of reponses and removes any responses that
    have domains that are in the ignored_domains variable"""
    for domain in ignored_domains:
        for count, response in enumerate(response_trace):
            if domain in response.url:
                response_trace.remove(response)
            else:
                continue
    return response_trace

if __name__ == "__main__":
    url_to_test = input("What URL should be traced?: ")