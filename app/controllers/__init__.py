import pkgutil


METHODS = {'GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'COPY', 'HEAD', 'OPTIONS', 'LINK', 'UNLINK', 'PURGE', 'LOCK',
           'UNLOCK', 'PROPFIND', 'VIEW'}


class Controllers:

    class __OnlyOne:

        # ======================================================
        #           the code goes here
        # =======================================================

        def __init__(self):
            self.val = None
            self.rules = []

        def __str__(self):
            return 'self' + self.val

        def register(self, rule, view_name, view_func):
            r = {"rule": rule, "view_name": view_name, "view_func": view_func}

            self.rules.append(r)

        def register_methods(
            self,
            rule,
            view_name,
            view_func,
                methods=None
        ):
            if methods is None:
                methods = METHODS
            r = {"rule": rule, "view_name": view_name, "view_func": view_func, "methods": methods}

            self.rules.append(r)

        def grab(self, app):
            for r in self.rules:
                if "methods" not in r.keys():
                    app.add_url_rule(r["rule"], r["view_name"], r["view_func"])
                else:
                    app.add_url_rule(r["rule"], r["view_name"],
                                     r["view_func"], methods=r["methods"])

        # =================================================================
        #           the code goes up there
        # ==================================================================

    instance = None

    def __new__(cls):  # __new__ always a classmethod
        if not Controllers.instance:
            Controllers.instance = Controllers.__OnlyOne()
        return Controllers.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)


# import all the modules in folder
__all__ = []
for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
    __all__.append(module_name)
    _module = loader.find_module(module_name).load_module(module_name)
    globals()[module_name] = _module
