import whois 

domain_name="colostate.edu"

def is_registered(domain_name):
    """
    Returns boolean indicating if 'domain_name' is registered
    """
    try: 
        w= whois.whois(domain_name)
    except Exception:
        return FALSE
    else:
        return bool(w.domain_name)

if is_registered(domain_name):
    whois_info = whois.whois(domain_name)
    print("Domain Registrar: ", whois_info.registrar)
    print("WHOIS Server: ", whois_info.whois_server)
    print("Creation Date: ", whois_info.creation_date)
    print("Expiration Date: ", whois_info.expiration_date)
