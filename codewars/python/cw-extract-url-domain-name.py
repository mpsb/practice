'''
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
'''

def domain_name(url):
    split_url = url.split('.')

    if split_url[0] == 'www':
        return split_url[1]
    else:
        try:
            if split_url[0].split('//')[1] == 'www':
                return split_url[1]
            else:
                return split_url[0].split('//')[1]
        except IndexError:
            return split_url[0]