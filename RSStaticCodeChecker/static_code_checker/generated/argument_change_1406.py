import lib.lib as lib
import json
def easyCheck(s):
    return "QueryBeamSetInfo" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["Filter"]
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
    from bases import score_Case
    steps += 1
    score_temp = lib.score_generic(d, "QueryBeamSetInfo")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value"), "[]")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value"), "TreatmentPlans")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_Case.get_score(d.get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"Case.TreatmentPlans.[]\", \"params\": [\"Filter\"], \"method\": \"QueryBeamSetInfo\", \"description\": \"QueryBeamSetInfo(..)\\r\\n  Returns info on all beam sets on a treatment plan.\\r\\n  Example:\\r\\n    To return info on all beam sets with the exact name \\r\\n    'BeamSet1' in a treatment plan:\\r\\n    info = treatmentPlan.QueryBeamSetInfo(Filter = {'Name': \\r\\n    '^BeamSet1$'}\\r\\n  Parameters:\\r\\n    Filter - Filter using regular expressions.  \\r\\n                  Possible keys:\\r\\n                     *Id\\r\\n                     *Name\\r\\n                     *ApprovalStatus\\r\\n                     *IsImmutable\\r\\n                     *IsClinical\\r\\n                     *HasDose\\r\\n                     *DoseAlgorithm\\r\\n                     *AlgorithmVersion\\r\\n  Returns:\\r\\n    List of beam set information.\\r\\n\"}")