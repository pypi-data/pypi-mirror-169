

_SENTINEL = object()

class ProxyAttrMixins:
    def __init__(self):
        # Do nothing: just prevent the proxied class` __init__ from being run
        pass
    
    def _inner_get(self, attrname):
        bound_getattr = super().__getattribute__
        try:
            proxied = bound_getattr("proxied")
        except AttributeError:
            # No associated object to proxy to!
            # just pass an try to retrieve the attribute from `self`
            pass
        else: # no AttributeError: there is a proxied object        
            associated_attr = getattr(proxied, attrname, _SENTINEL)
            if associated_attr is not _SENTINEL:
                # if object is a callable: it is a method. A mehtod in the derived class should
                # be called if it exists, and just otherwise in the proxied object:
                if callable(associated_attr):
                    try:
                        own_method = bound_getattr(attrname)
                    except AttributeError: 
                        pass
                    else:
                        return "own", own_method
                return "proxy", associated_attr
        # if there is no proxied object, or if the proxied does not have the desired attribute,
        # return the regular instance attribute:
        return "own", bound_getattr(attrname)
        
        
    def __getattribute__(self, attrname):
        bound_getattr = super().__getattribute__
        whose, attr = bound_getattr("_inner_get")(attrname)
        return attr
    
    def __setattr__(self, attrname, value):
        bound_getattr = super().__getattribute__
        try:
            whose, attr = bound_getattr("_inner_get")(attrname)
        except AttributeError:
            whose = "own"
        if whose !=  "own":
            proxied = bound_getattr("proxied")
            return setattr(proxied, attrname, value)
        super().__setattr__(attrname, value)
        