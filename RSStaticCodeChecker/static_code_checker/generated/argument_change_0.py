import lib.lib as lib
import json
def easyCheck(s):
    return "EditShowDoseVisualization" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["ShowDose","ShowInterpolated","ShowIsolines","ShowColorWash","ColorWashTransparency"]
    too_many = []
    for keyword in d.get("keywords", []):
        if keyword.get("arg") in args:
            args.remove(keyword.get("arg"))
        else:
            too_many.append(keyword.get("arg"))
    if not too_many and not args:
        return True
    return (0 if too_many else 3)
def prefixScore(d):
    import sys
    score = sys.maxint
    steps = 0
    if not d.get("_PyType") == "Call":
        return sys.maxint
    _d = d.get("func")
    score = dictMatchScore_0(_d)
    if score != sys.maxint:
        return score
    return sys.maxint
def dictMatchScore_0(d):
    import sys
    score = 0
    steps = 0
    from bases import score_Patient
    steps += 1
    score_temp = lib.score_generic(d, "EditShowDoseVisualization")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_Patient.get_score(d.get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"Patient\", \"params\": [\"ShowDose\", \"ShowInterpolated\", \"ShowIsolines\", \"ShowColorWash\", \"ColorWashTransparency\"], \"method\": \"EditShowDoseVisualization\", \"description\": \"EditShowDoseVisualization(..)\\r\\n  Setting dose related visualization settings.\\r\\n  Parameters:\\r\\n    ShowDose - True if dose shall be displayed.\\r\\n    ShowInterpolated - True if interpolated dose shall be \\r\\n      displayed.\\r\\n    ShowIsolines - True if iso dose lines shall be displayed.\\r\\n    ShowColorWash - True if dose with color wash shall be \\r\\n      displayed.\\r\\n    ColorWashTransparency - A value between [0.0 1.0] where \\r\\n      0.0 means no transparency and 1.0 means full transparency of \\r\\n      dose color wash.\\r\\n\"}")
