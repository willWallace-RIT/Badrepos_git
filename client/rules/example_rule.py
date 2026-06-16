def run(pkgbuild):
    if "_branch=main" in pkgbuild:
        return [{
            "severity":"warning",
            "message":"Mutable branch detected"
        }]

    return []
